import re
import time

from django.shortcuts import render
from django.conf import settings


def calculate_and_time(f, arg1, arg2):
    RES = 0
    TIME = 1
    res = f(arg1, arg2)
    return res[RES], res[TIME]


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def peek(stack):
    if stack:
        return stack[-1]
    return None


def apply_operator_and_time(operators, values, is_java):

    op = operators.pop()
    right = values.pop()
    left = values.pop()

    if is_java:
        java_result = settings.CALCULATOR_RPC.call({'operation': op, 'arg1': left, 'arg2': right})
        values.append(java_result['response'])
        return java_result['time']

    else: # C++
        if op == '+':
            (cpp_result, cpp_execution_time) = calculate_and_time(settings.MY_LIB.add, left, right)
        elif op == '-':
            (cpp_result, cpp_execution_time) = calculate_and_time(settings.MY_LIB.sub, left, right)
        elif op == '*':
            (cpp_result, cpp_execution_time) = calculate_and_time(settings.MY_LIB.mult, left, right)
        elif op == '/':
            (cpp_result, cpp_execution_time) = calculate_and_time(settings.MY_LIB.divide, left, right)
        elif op == '^':
            (cpp_result, cpp_execution_time) = calculate_and_time(settings.MY_LIB.power, left, right)
        values.append(cpp_result)
        return cpp_execution_time


def greater_precedence(op1, op2):
    precedences = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    return precedences[op1] > precedences[op2]


def evaluate(expression, is_java):

    # Check string validity:
    for char in expression:
        if char not in "+-*/^1234567890.() ":
            raise Exception("Invalid symbol entered into calculator.")
            return None

    # Express negative numbers without unary minus:
    expression = expression.replace(' ', '')
    expression = expression.replace('(-', '(0-')

    # Tokenize string into numbers and operators:
    tokens = re.findall("[+-/*^()]|\d+\.\d+|\d+", expression)
    values = []
    operators = []

    # Shunting yard algorithm:
    total_execution_time = 0
    for token in tokens:
        if is_number(token):
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                total_execution_time += apply_operator_and_time(operators, values, is_java)
                top = peek(operators)
            operators.pop()  # Discard the '('
        elif token in '+-*/^': # Operator
            top = peek(operators)
            while top is not None and top not in "()" and greater_precedence(top, token):
                total_execution_time += apply_operator_and_time(operators, values, is_java)
                top = peek(operators)
            operators.append(token)
        else:
            raise Exception("Invalid symbol entered into calculator.")
            return None

    # Postfix evaluation:
    while peek(operators) is not None:
        total_execution_time += apply_operator_and_time(operators, values, is_java)

    return (values[0], total_execution_time)


def calculate(calc_string, is_java):
    try:
        start = time.time()
        (result, execution_time) = evaluate(calc_string, is_java)
        end = time.time()
        overall_time = end - start
        return (result, execution_time, overall_time)
    except Exception:
        raise


def perform_calculation(request):
    context = {}

    if 'calculation' in request.POST:
        calc_string = request.POST['calculation']

        try:
            (cpp_result, cpp_execution_time, cpp_overall_time) = calculate(calc_string, is_java=False)
            (java_result, java_execution_time, java_overall_time) = calculate(calc_string, is_java=True)
        except Exception:
            cpp_result, java_result = "Invalid input.", "Invalid input."
            cpp_execution_time, cpp_overall_time, java_execution_time, java_overall_time = (0 for _ in range(4))

        DECIMAL_PLACES = 4
        context = {
            'prev_calculation' : calc_string,
            'cpp_result': cpp_result,
            'cpp_execution_time': round(cpp_execution_time * 1000, DECIMAL_PLACES), # * 1000 converts seconds to milliseconds.
            'cpp_overall_time': round(cpp_overall_time * 1000, DECIMAL_PLACES),
            'java_result': java_result,
            'java_execution_time': round(java_execution_time / 1000000.0, DECIMAL_PLACES), # / 1M converts nanoseconds to milliseconds.
            'java_overall_time': round(java_overall_time * 1000, DECIMAL_PLACES),
        }

    return render(request, 'calculator/calculate.html', context)
