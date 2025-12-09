Feature: 
    As a progressive guy
    I want to create simple tasks
    To not forget about them

    Scenario: Creation simple task Cook dinner
        When I create a simple task "Cook dinner"
        Then task has description: "Cook dinner"
