from behave import given, when, then

from Tasks.Tasks import SimpleTask


@when('I create a simple task "{description}"')
def step_impl(context, description):
    context.task = SimpleTask(description)

@then('task has description: "{correct_description}"')
def step_impl(context, correct_description):
    assert context.task.description == correct_description


@given('the same task "{description}"')
def step_impl(context, description):
    context.task = SimpleTask(description)

@when('I mark task as completed')
def step_impl(context):
    context.task.mark_as_completed()

@then('task gets completed')
def step_impl(context):
    assert context.task.is_completed() == True
