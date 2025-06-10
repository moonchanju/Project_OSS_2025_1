# budget.py
import datetime
from expense import Expense  # Import the Expense class

class Budget:
    def __init__(self):
        self.expenses = []
        self.budgets = {}

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"{category} 예산이 {amount}원으로 설정되었습니다.\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

        spent = sum(e.amount for e in self.expenses if e.category == category)
        budget_limit = self.budgets.get(category)

        if budget_limit is not None and spent > budget_limit:
            print(f"⚠️ {category} 예산 {budget_limit}원을 초과했습니다! 지금까지 사용: {spent}원\n")
            print("[!] 예산을 초과했습니다. 어떻게 하시겠습니까?")
            print("1. 예산 늘리기")
            print("2. 마지막 지출 취소")
            print("3. 그냥 넘어가기")
            choice = input("선택 > ")

            if choice == "1":
                try:
                    new_amount = int(input(f"{category}의 새 예산 금액(원): "))
                    self.set_budget(category, new_amount)
                except ValueError:
                    print("잘못된 금액입니다.\n")
            elif choice == "2":
                self.expenses.pop()  # Remove the last added expense
                print("마지막 지출이 취소되었습니다.\n")
            elif choice == "3":
                print("그대로 유지합니다.\n")
            else:
                print("잘못된 선택입니다. 아무 동작도 하지 않습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        print("--- 전체 지출 내역 ---")
        for expense in self.expenses:
            print(expense) # Uses the __str__ method of the Expense class
        print("---------------------\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")