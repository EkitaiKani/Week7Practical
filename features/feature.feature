Feature: Calculator
	Validate all arithmetic and trigonometric operations provided by the Calculator

	Background: Common steps
		Given the Calculator is initialised

	Scenario: Addition
		When I add 10 and 5
		Then the result should be 15

	Scenario: Substraction
		When I subtract 20 and 10
		Then the result should be 10

	Scenario: Multiplication
		When I multiply 6 and 7
		Then the result should be 42

	Scenario: Division
		When I divide 10 and 2
		Then the result should be 5
