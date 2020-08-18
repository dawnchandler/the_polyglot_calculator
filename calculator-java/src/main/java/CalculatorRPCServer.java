import com.rabbitmq.client.*;
import org.apache.commons.lang3.time.StopWatch;
import org.json.JSONObject;

import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class CalculatorRPCServer {

    private static final String RPC_QUEUE_NAME = "rpc_queue";
    private static final String RABBITMQ_HOST_NAME = "calculator-rabbitmq";

    public static void main(String[] argv) throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost(RABBITMQ_HOST_NAME);
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            channel.queueDeclare(RPC_QUEUE_NAME, false, false, false, null);
            channel.queuePurge(RPC_QUEUE_NAME);

            channel.basicQos(1);

            System.out.println(" [x] Awaiting RPC requests");

            Object monitor = new Object();
            // JSONParser parser = new JSONParser();
            DeliverCallback deliverCallback = (consumerTag, delivery) -> {
                AMQP.BasicProperties replyProps = new AMQP.BasicProperties
                        .Builder()
                        .correlationId(delivery.getProperties().getCorrelationId())
                        .build();

                // Time the calculation:
                StopWatch watch = new StopWatch();
                watch.start();

                String response = "";
                try {
                    JSONObject message = new JSONObject(new String(delivery.getBody(), "UTF-8"));
                    Float result = Calculator.processMessage(message);
                    if (result == null) {
                        response = ("unable to determine what operation to perform");
                    } else {
                        response = result.toString();
                    }
                } catch (Exception e) {
                    response = ("experienced error " + e.toString());
                    System.out.println(response);
                } finally {
                    watch.stop();
                    JSONObject responseJson = new JSONObject();
                    responseJson.put("response", response);
                    responseJson.put("time" , watch.getNanoTime());
                    System.out.println("returning the response ["+responseJson+"]");
                    channel.basicPublish("", delivery.getProperties().getReplyTo(), replyProps, responseJson.toString().getBytes("UTF-8"));
                    channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
                    System.out.println("response returned");
                    // RabbitMq consumer worker thread notifies the RPC server owner thread
                    synchronized (monitor) {
                        monitor.notify();
                    }
                }
            };

            channel.basicConsume(RPC_QUEUE_NAME, false, deliverCallback, (consumerTag -> {
            }));
            // Wait and be prepared to consume the message from RPC client.
            while (true) {
                synchronized (monitor) {
                    try {
                        monitor.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }


}