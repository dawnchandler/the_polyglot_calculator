#!/usr/bin/env python

from calculator.calculator.RpcClient import CalculatorRcpClient

print(' [*] Waiting for messages. To exit press CTRL+C')

calculator_rpc = CalculatorRcpClient('localhost', 'rpc_queue')

message = {'func_name': 'add', 'arg1': 5, 'arg2': 7}
print(f" [x] Requesting {message}")
response = calculator_rpc.call(message)
print(" [.] Got %r" % response)

message['arg2'] = 20
print(f" [x] Requesting {message}")
response = calculator_rpc.call(message)
print(" [.] Got %r" % response)
arg1 = int(3)
arg2 = int(4)
val = ("Got %r" % calculator_rpc.call({'func_name': 'add', 'arg1': arg1, 'arg2': arg2}))
print(val)
