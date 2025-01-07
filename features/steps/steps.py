from behave import *
from calculator import add, subtract, multiply, divide

@given(u'the Calculator is initialised')
def step_given_calc_init(context):
    context.driver = None

@when(u'I add 10 and 5')
def step_when_add(context):
    context.result = add(10, 5)
    
@when(u'I subtract 20 and 10')
def step_when_subtract(context):
    context.result = subtract(20, 10)
    
@when(u'I multiply 6 and 7')
def step_when_multiply(context):
    context.result = multiply(6, 7)
        
@when(u'I divide 10 and 2')
def step_when_divide(context):
    context.result = divide(10, 2)
    
@then(u'the result should be {expected}')
def step_when_result(context, expected):
    expected = int(expected)
    assert expected == context.result, \
        f"Expected {expected}, but got {context.result}"

@then(u'the result should not be {not_expected}')
def step_when_result(context, expected):
    not_expected = int(not_expected)
    assert not_expected == context.result, \
        f"Unexpected result {context.result}"