from account import Account
from atm import Atm
import random
import time

def set_bankrupt_chance():
    for i in range(5):
        print(f"\033[0m파산 확률을 입력하세요. (1/N) N은 1 이상의 정수입니다. (예: 100)")
        print(f"입력 기회 5회 제한 [{i+1}/5] ")
        bankruptcy_probability = input("파산 확률 (1/N) N 입력: ")
        if bankruptcy_probability.isdigit():
            return bankruptcy_probability
        else:
            if i == 4:
                print("파산 확률 입력을 5번 실패했습니다. 프로그램을 종료합니다.")
                return
            print("파산 확률은 숫자로 입력해야 합니다.")
            
        

if __name__ == "__main__":
    print("ATM System main is called...")

    study_accounts = [
    Account("김연희", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("박재오", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("백상현", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("서지민", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("이건명", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("임정찬", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("최승혁", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}")))),
    Account("정규호", "{:014d}".format(random.randrange(1,(int(1e+14)-1))), "{:04d}".format(random.randrange(1,9999)), int(random.random() * float((f"1e{random.randrange(1,20)}"))))
    ]

    print("파산 확률을 입력하세요.")
    try:
        bankruptcy_probability = set_bankrupt_chance()
    except ValueError as e:
        print(e)
    print()
    print(f"[1/{bankruptcy_probability}] 의 확률로 개인이 파산합니다.")
    print()

    # 100분의 1 확률로 파산 상태 만들기
    for account in study_accounts:
        print(f"\033[0m{account.name}님 처리중....")
        time.sleep(random.randint(1,2))  # 1초 대기
        if random.random() < (1/float(bankruptcy_probability)):  # 1% 확률
            # 0원 또는 마이너스 값 중 랜덤 선택
            if random.random() < 0.5:
                account.balance = 0  # 0원
                print(f"\033[31m💸 {account.name}님은 파산하여 잔고가 0원이 되었습니다!")
            else:
                # 마이너스 값 (빚)
                debt_amount = random.random() * float((f"1e{random.randrange(1,20)}"))
                print(debt_amount)
                account.balance = 0
                account.balance = -debt_amount
                print(f"\033[31m💸 {account.name}님은 파산하여 {Atm.format_korean_currency_large(account, account.balance)}원의 빚을 지게 되었습니다!")
        else:
            print(f"\033[0m💰 {account.name}님의 잔고는 {Atm.format_korean_currency_large(account, account.balance)}원입니다.")

    print()
    print("\033[0m모든 계좌의 상태가 업데이트되었습니다. 임의의 순서로 ATM 계좌를 생성합니다.")
    print()
    
    # Account Objects 생성
    # ATM 시스템 초기화
    accounts = random.sample(study_accounts, 8)
    # for acct in accounts:
    #     print(f"Account Name: {acct.name}, Account Number: {acct.account_number}, PIN: {acct.pin}, Balance: {acct.balance}")
    
    python_study_atm = Atm("파이선 스터디 ATM", accounts)
    python_study_atm.run()

