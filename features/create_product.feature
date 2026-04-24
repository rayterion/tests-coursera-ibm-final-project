Feature: Create a product and store it in the database

Scenario Outline:
    When the user types in the name: <name>
        and clicks the "send" button
    Then the product listed appears on the screen
    
    Examples:
        | name    |
        | Apple   |
        | Ketchup |
        | Orange  |