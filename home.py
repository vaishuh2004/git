class CustomNumber:
    def init(self, value):
        self.value = value

    def add(self, other):
        # Overload + operator to perform subtraction
        return self.value - other.value

    def sub(self, other):
        # Overload - operator to perform addition
        return self.value + other.value

    def mul(self, other):
        # Overload * operator to perform division
        return self.value / other.value

    def truediv(self, other):
        # Overload / operator to perform multiplication
        return self.value * other.value

    def str(self):
        return str(self.value)


# Example usage
if __name__ == "main":
    num1 = CustomNumber(10)
    num2 = CustomNumber(5)

    print(f"{num1} + {num2} = {num1 + num2}")  # Should perform subtraction
    print(f"{num1} - {num2} = {num1 - num2}")  # Should perform addition
    print(f"{num1} * {num2} = {num1 * num2}")  # Should perform division
    print(f"{num1} / {num2} = {num1 / num2}")  # Should perform multiplication