from behave import *
from calculator import addition, subtraction, multiplication, division


@given('the calculator is initialized')
def step_given_calculator_initialized(context):
    context.result = None

@when('I add {a:d} and {b:d}')
def step_when_addition(context, a, b):
    context.result = addition(a,b)


@when('I subtract {a:d} from {b:d}')
def step_when_subtraction(context, a, b):
    context.result = subtraction(b,a)

@when('I multiply {a:d} and {b:d}')
def step_when_multiplication(context, a, b):
    context.result = multiplication(a,b)

@when('I divide {a:d} by {b:d}')
def step_when_division(context, a, b):
    context.result = division(a,b)

@then ('the result should be {expected_result}')
def step_then_result_should_be(context, expected_result):
    expected_result = int(expected_result)
    assert context.result == expected_result,\
    f"Expected {expected_result}, but get {context.result}"