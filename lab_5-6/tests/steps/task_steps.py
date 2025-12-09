from behave import when, then

from ToDoList import SimpleTask


@when('I create a simple task "{description}"')
def step_impl(context, description):
    context.task = SimpleTask(description)

@then('task has description: "{correct_description}"')
def step_impl(context, correct_description):
    assert context.task.description == correct_description

