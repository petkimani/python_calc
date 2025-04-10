import streamlit as st
import math

# Calculator class
class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    # Basic operations
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, operator, num2=None):
        if not isinstance(num1, (int, float)) or (num2 is not None and not isinstance(num2, (int, float))):
            raise TypeError("Inputs must be numbers.")
        if operator not in self.operations:
            raise ValueError(f"Operation '{operator}' not supported.")
        func = self.operations[operator]
        return func(num1) if num2 is None else func(num1, num2)

# Advanced operations
def exponentiation(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def logarithm(x):
    if x <= 0:
        raise ValueError("Logarithm is undefined for zero or negative numbers.")
    return math.log(x)

# Streamlit UI
st.title("🧮 Streamlit Calculator")
st.markdown("Supports: +, -, *, /, ^, sqrt, log")

calc = Calculator()
calc.add_operation('^', exponentiation)
calc.add_operation('sqrt', square_root)
calc.add_operation('log', logarithm)

# Operation selection
operation = st.selectbox("Choose an operation", list(calc.operations.keys()))

# Inputs
if operation in ['sqrt', 'log']:
    num1 = st.number_input("Enter a number", key="num1_unary")
    if st.button("Calculate"):
        try:
            result = calc.calculate(num1, operation)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")
else:
    num1 = st.number_input("Enter first number", key="num1_binary")
    num2 = st.number_input("Enter second number", key="num2_binary")
    if st.button("Calculate"):
        try:
            result = calc.calculate(num1, operation, num2)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")
