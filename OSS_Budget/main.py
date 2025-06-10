# main.py
from budget import Budget  # Import the Budget class

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 예산 설정")
        print("5. 전체 예산 요약 보기") # New option
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리: ")
            description = input("내역: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            category = input("예산 설정할 카테고리: ")
            try:
                amount = int(input(f"{category} 예산 금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.set_budget(category, amount)

        elif choice == "5": # New logic for option 5
            budget.budget_summary()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()