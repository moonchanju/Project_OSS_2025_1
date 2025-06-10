class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
     def __init__(self, date, category, description, amount):
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"