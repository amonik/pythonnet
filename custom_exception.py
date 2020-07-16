# Class inheriting ValueError class
class NotEnough(ValueError):
    def __init__(self, pay):
        super().__init__(f"You only make ${pay}, you need to make at "
                         f"least 20000.\nI am sorry you don't get a bonus...")
        self.pay = pay


class IsNegative(ArithmeticError):
    def __init__(self, pay):
        super().__init__(f"Warning your pay of ${pay} is negative!!!!")
        self.pay = pay
