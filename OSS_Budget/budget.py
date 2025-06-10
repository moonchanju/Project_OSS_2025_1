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
            print(expense)
        print("---------------------\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def budget_summary(self):
        """
        Displays a summary of all set budgets,
        including how much has been spent and how much remains for each category.
        Also shows overall budget and spending totals.
        """
        print("--- 전체 예산 요약 ---")
        if not self.budgets:
            print("설정된 예산이 없습니다.\n")
            return

        total_budget_amount = 0
        total_spent_across_budgets = 0

        for category, limit in self.budgets.items():
            spent_in_category = sum(e.amount for e in self.expenses if e.category == category)
            remaining = limit - spent_in_category
            print(f"- {category}: 예산 {limit}원, 사용 {spent_in_category}원, 남은 금액 {remaining}원")
            total_budget_amount += limit
            total_spent_across_budgets += spent_in_category

        print("----------------------")
        print(f"총 설정 예산: {total_budget_amount}원")
        print(f"총 예산 사용 금액: {total_spent_across_budgets}원")
        print(f"총 남은 예산: {total_budget_amount - total_spent_across_budgets}원s\n")