
from budget import Budget


def main():
    budget = Budget()
def main():
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 예산 설정")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
          def main():
            budget.total_spent()

        elif choice == "4":
            category = input("예산 설정할 카테고리: ")
            try:
                amount = int(input(f"{category} 예산 금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
    
            budget.set_budget(category, amount)
             
        elif choice == "5":
            print("가계부를 종료합니다.")
               

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()