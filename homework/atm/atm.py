from account import Account as acnt


class Atm:
    def __init__(self, name: str, accounts: list[acnt]):
        self.name = name
        self.accounts = accounts

        print(f"ATM 시스템 '{self.name}'이(가) 초기화되었습니다.")
        for acct in self.accounts:
            color = "\033[32m" if acct.balance > 0 else "\033[31m"
            print(f"{color}계좌명: {acct.name}, 계좌번호: {acct.account_number}, PIN: {acct.pin}, 잔액: {self.format_korean_currency_large(acct.balance)}")
        print("\033[0m")  # Reset color

    def generate_accounts(self, name: list[str], account_number: list[int], pin: list[int], balance: list[float]) -> None:
        for n, an, p, b in zip(name, account_number, pin, balance):
            self.accounts.append(acnt(n, an, p, b))
                                 
    def get_account(self, account_number: int) -> acnt:
        if not isinstance(account_number, int):
            try:
                account_number = int(account_number)
            except ValueError:
                raise ValueError("계좌 번호는 숫자여야 합니다.")
        for acc in self.accounts:
            if int(acc.account_number) == account_number:
                return acc
        raise ValueError("해당 계좌를 찾을 수 없습니다.")

    def check_pin(self, account: acnt, pin: int) -> bool:
        if len(str(pin)) != 4:
            print("PIN 번호는 4자리 숫자여야 합니다.")
            return False
        if not isinstance(pin, int):
            try:
                pin = int(pin)
            except ValueError:
                print("PIN 번호는 숫자여야 합니다.")
                return False
         
        if int(account.pin) == pin:
            return True
        else:
            print("PIN 번호가 일치하지 않습니다. 다시 시도하세요.")
            return False

    def transfer(self, from_account: acnt, to_account: acnt, amount: float) -> None:
        print(f"{from_account.name} 계좌에서 {to_account.name} 계좌로 {self.format_korean_currency_large(amount)} 이체를 시도합니다.")
        if from_account.withdraw(amount):
            to_account.deposit(amount)
        else:
            raise ValueError("이체에 실패했습니다. 잔액이 부족합니다.")
    

    def format_korean_currency_large(self, amount):
        if not isinstance(amount, (int, float)):
            amount = float(amount)
        # 음수 처리
        is_negative = amount < 0
        amount = abs(int(amount))
        
        if amount == 0:
            return "0원"

        units = [
            ("해", 10**20),
            ("경", 10**16),
            ("조", 10**12),
            ("억", 10**8),
            ("만", 10**4),
            ("만", 10**4),
            ("", 1)
        ]

        result = []
        for unit_name, unit_value in units:
            unit_amount, amount = divmod(amount, unit_value)
            if unit_amount:
                result.append(f"{unit_amount:,}{unit_name}")

        formatted_amount = " ".join(result) + "원"
        
        # 음수인 경우 마이너스 부호 추가
        if is_negative:
            return "-" + formatted_amount
        
        return formatted_amount
    
    def choose_account(self, index:int) -> acnt:
        if not index.isdigit():
            raise ValueError("계좌 선택은 숫자로 입력해야 합니다.")
        index = int(index) - 1  # 사용자 입력은 1부터 시작하
        if 0 <= index < len(self.accounts):
            return self.accounts[index]
        else:
            raise IndexError(f"유효하지 않은 계좌 선택입니다. => [{index}]")
        
    def select_task(self, selected_account):
        tasks = {
            "0": "상태 조회",
            "1": "입금",
            "2": "출금",
            "3": "이체",
            "4": "잔액 조회",
            "5": "종료"
        }
        
        while True:
            print()
            for accnt in self.accounts:
                print(f"계좌명: {accnt.name}, 계좌번호: {str(accnt.account_number)}, 잔액: {self.format_korean_currency_large(accnt.balance)}")
            print()
            task = input("0-상태 조회, 1-입금, 2-출금, 3-이체, 4-잔액 조회, 5-종료: ")
            print("선택한 작업:", tasks.get(task, "유효하지 않은 작업"))
            print()
            if task == "0":
                print(selected_account.get_status())
            elif task == "1":
                amount = input("입금할 금액을 입력하세요: ")
                try:
                    if selected_account.deposit(amount):
                        print(f"{self.format_korean_currency_large(amount)}이(가) 입금되었습니다. 현재 잔액: {self.format_korean_currency_large(selected_account.balance)}\n")                        
                except ValueError as e:
                    print("입금에 실패했습니다.")
                    print(e)
            elif task == "2":
                amount = input("출금할 금액을 입력하세요: ")
                try:
                    if selected_account.withdraw(amount):
                        print(f"{self.format_korean_currency_large(amount)}이(가) 출금되었습니다. 현재 잔액: {self.format_korean_currency_large(selected_account.balance)}\n")
                except ValueError as e:
                    print("출금에 실패했습니다.")
                    print(e)
            elif task == "3":
                to_account_number = input("이체할 계좌 번호를 입력하세요: ")
                try:
                    to_account = self.get_account(to_account_number)
                except ValueError as e:
                    print(e)

                print(f"현재 잔액: {self.format_korean_currency_large(selected_account.balance)}")
                amount = input("이체할 금액을 입력하세요: ")
                try:
                    self.transfer(selected_account, to_account, amount)
                    print(f"{self.format_korean_currency_large(amount)}이(가) {to_account.name} 계좌로 이체되었습니다.\n현재 잔액: {self.format_korean_currency_large(selected_account.balance)}\n")
                except ValueError as e:
                    print(e)
            elif task == "4":
                print(f"현재 잔액: {self.format_korean_currency_large(selected_account.balance)}\n")
            elif task == "5":
                print("ATM 시스템을 종료합니다.")
                return
    
    def run(self):
        print(f"ATM 시스템 '{self.name}'이(가) 실행 중입니다.")
        # 여기에 ATM 시스템의 주요 로직을 추가할 수 있습니다.
        # 예: 사용자 입력 처리, 계좌 조회, 입출금 등
        # 현재는 단순히 초기화 메시지만 출력합니다.
        for i in range(5):
            print("ATM 시스템이 준비되었습니다. 계좌를 선택하세요.")
            for idx, acct in enumerate(self.accounts, start=1):
                print(f"[{idx}]-계좌명: {acct.name}, 계좌번호: {str(acct.account_number)}")
            try:
                selected_account = self.choose_account(input("선택 번호: "))
                break
            except (IndexError, ValueError) as e:
                print(e)
                if i == 4:
                    print("계좌 선택에 실패했습니다. ATM 시스템을 종료합니다.")
                    return
        
        print(f"선택한 계좌: {selected_account.name} ({selected_account.account_number}) ({selected_account.pin})")
        print("PIN 번호를 입력하세요.")
        # PIN 번호 확인
        for i in range(5):
            print(f"남은 인증 시도 횟수: {5-i}")
            if self.check_pin(selected_account, input("PIN 번호 입력: ")):
                print(f"{selected_account.name}님의 계좌에 접근할 수 있습니다.")
                print(f"잔액: {self.format_korean_currency_large(selected_account.balance)}")
                break
        if i == 4:
            print("인증에 실패했습니다. ATM 시스템을 종료합니다.")
            return

        print("원하는 작업을 선택하세요.")
        self.select_task(selected_account)

    
        