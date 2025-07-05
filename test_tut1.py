import pytest

class MyCalculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("only numbers are allowed")
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def calculator(self, select, a, b):
        if select == "+":
            return self.add(a, b)
        elif select == "-":
            return self.sub(a, b)
        elif select == "*":
            return self.mul(a, b)
        elif select == "/":
            return self.div(a, b)
        else:
            return "Exiting Calculator"

if __name__ == "__main__":
    calc = MyCalculator()
    select = input("Enter the symbol +, -, *, / to perform operation: ")
    a = float(input("Enter a first number: "))
    b = float(input("Enter a second number: "))

    result = calc.calculator(select, a, b)
    print("Result: ", result)



class TestMathOperationsCalculator:
    calc = MyCalculator()

    def test_add(self):
        # Normal input numbers
        assert self.calc.add(2, 3) == 5, "Addition result for positive numbers" # Positive numbers
        assert self.calc.add(-1, -2) == -3 # Negative numbers
        assert self.calc.add(0, 0) == 0 # Netural numbers
        assert self.calc.add(-1, 1) == 0 # Mixed numbers

        # Invalid input type 
        with pytest.raises(TypeError):
            self.calc.add("3", 3)
        with pytest.raises(TypeError):
            self.calc.add(None, 2)
        with pytest.raises(TypeError):
            self.calc.add([], {})

        # Test with float numbers
        assert self.calc.add(2.0, 5.0) == 7.0, "Addition result for float positive numbers"
        assert self.calc.add(-3.0, -2.0) == -5.0
        assert self.calc.add(0.0, 0.0) == 0.0
        assert self.calc.add(3, 5.0) == 8.0 

        # Test with large numbers
        assert self.calc.add(10**15, 10**15) == 2 * 10**15

    def test_sub(self):
        assert self.calc.sub(5, 5) == 0
        assert self.calc.sub(0, 0) == 0
        assert self.calc.sub(-5, -5) == 0
        assert self.calc.sub(-1, 5) == -6
        assert self.calc.sub((-1), -9) == 8

        # Invalid input type 
        with pytest.raises(TypeError):
            self.calc.sub("3", 3)
        with pytest.raises(TypeError):
            self.calc.sub(None, 2)
        with pytest.raises(TypeError):
            self.calc.sub([], {})

        # Test with float numbers
        assert self.calc.sub(2.0, 5.0) == -3.0, "substraction result for float positive numbers"
        assert self.calc.sub(-3.0, -2.0) == -1.0
        assert self.calc.sub(0.0, 0.0) == 0.0
        assert self.calc.sub(3, 5.0) == -2.0 

        # Test with large numbers
        assert self.calc.sub(10**15, 10**15) == 0

    def test_mul(self):
        assert self.calc.mul(5, 5) == 25
        assert self.calc.mul(0, 0) == 0
        assert self.calc.mul(-5, -5) == 25
        assert self.calc.mul(-1, 5) == -5
        assert self.calc.mul((-1), -9) == 9

        # Invalid input type 
        with pytest.raises(TypeError):
            self.calc.mul("3", 3)
        with pytest.raises(TypeError):
            self.calc.mul(None, 2)
        with pytest.raises(TypeError):
            self.calc.mul([], {})

        # Test with float numbers
        assert self.calc.mul(2.0, 5.0) == 10.0, "substraction result for float positive numbers"
        assert self.calc.mul(-3.0, -2.0) == 6.0
        assert self.calc.mul(0.0, 0.0) == 0.0
        assert self.calc.mul(3, 5.0) == 15.0 

        # Test with large numbers
        assert self.calc.mul(10**15, 10**15) == 10**15 * 10**15

    def test_div(self):
        assert self.calc.div(10, 2) == 5
        assert self.calc.div(2, 10) == 0.2
        assert self.calc.div(-5, 10) == -0.5
        assert self.calc.div(-20, -30) == 0.6666666666666666
        assert self.calc.div(10, 0) == "Error: Division by zero"
        assert self.calc.div(0, 10) == 0.0
        
        # Invalid input type 
        with pytest.raises(TypeError):
            self.calc.div("3", 3)
        with pytest.raises(TypeError):
            self.calc.div(None, 2)
        with pytest.raises(TypeError):
            self.calc.div([], {})

        # Test with large numbers
        assert self.calc.div(10**15, 10**15) == 1.0

    def test_calculator(self):
        # Test addition
        assert self.calc.calculator("+", 2, 3) == 5

        # Test subtraction
        assert self.calc.calculator("-", 5, 3) == 2

        # Test multiplication
        assert self.calc.calculator("*", 4, 2) == 8

        # Test division
        assert self.calc.calculator("/", 10, 2) == 5.0

        # Test division by zero
        assert self.calc.calculator("/", 10, 0) == "Error: Division by zero"

        # Test invalid operator
        assert self.calc.calculator("%", 5, 2) == "Exiting Calculator"

'''
        source /d/virtualenvs/v1env/scripts/activate
        cd d:/pytest_tutorials
        pytest -vv -s -rp test_tut1.py

'''