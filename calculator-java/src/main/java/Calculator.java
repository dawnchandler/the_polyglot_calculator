import org.json.JSONObject;

public class Calculator {

    public static Float processMessage(JSONObject message){
        System.out.println("got the message " + message);
        if (message.get("operation").toString().equalsIgnoreCase("+")) {
            System.out.println("operation is add");
            return add(message.getFloat("arg1"), message.getFloat("arg2"));
        } else if (message.get("operation").toString().equalsIgnoreCase("-")) {
            System.out.println("operation is sub");
            return sub(message.getFloat("arg1"), message.getFloat("arg2"));
        } else if (message.get("operation").toString().equalsIgnoreCase("*")) {
            System.out.println("operation is mult");
            return mult(message.getFloat("arg1"), message.getFloat("arg2"));
        } else if (message.get("operation").toString().equalsIgnoreCase("/")) {
            System.out.println("operation is div");
            return div(message.getFloat("arg1"), message.getFloat("arg2"));
        } else if (message.get("operation").toString().equalsIgnoreCase("^")) {
            System.out.println("operation is exp");
            return exp(message.getFloat("arg1"), message.getFloat("arg2"));
        } else {
            return null;
        }
    }

    public static Float add(Float x, Float y){
        return x+y;
    }

    public static Float sub(Float x, Float y){
        return x-y;
    }

    public static Float mult(Float x, Float y){
        return x*y;
    }

    public static Float div(Float x, Float y){
        return x/y;
    }

    public static Float exp(Float x, Float y) {
        return (float) Math.pow(x, y);
    }
}
