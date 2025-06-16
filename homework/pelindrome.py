import re

def pelindrome(message: str)-> bool:
    print(f"\n\n{'Pelindrome Check START':=^50}".upper())
    if len(message.strip())==0:
        print("Please Insert Strings\n")
        return
        
    lw_message = message.lower()
    print(f"0. 문자열 소문자로 변환:\n{lw_message}\n")
    only_str = re.sub(r"[^A-Za-zㄱ-ㅎㅏ-ㅡ|가-힣]",'',lw_message)
    print(f"1. 문자열만 남기기:\n{only_str}\n")
    
    reversed_str = only_str[::-1]  #  reversed(only_str)
    print(f"2. 문자열 뒤집기:\n{reversed_str}\n")

    print(f"only_str == reversed_str : {only_str == reversed_str}")
    if only_str == reversed_str:
        print("✅ It's a pelindrome!!\n" \
        f"origin :          {only_str}\n"
        f"reversed :        {reversed_str}\n")
    else: 
        print("❌ It's not a pelindrome!!\n" \
        f"origin :          {only_str}\n"
        f"reversed :        {reversed_str}\n")

    print(f"\n{'Pelindrome Check END':=^50}".upper())


pelindrome_desc = pelindrome_desc = """
=======================================
🧠 1. 팰린드롬(Palindrome)의 개념
---------------------------------------
문자열을 거꾸로 뒤집어도 똑같은 값이라면 팰린드롬입니다.

=======================================
📚 2. 재미있는 예시
=======================================

🔤 영어 예시 (Palindrome words or sentences)

[단어]
- level, madam, civic, radar  ➜ 거꾸로 읽어도 동일

[문장]
- A man, a plan, a canal, Panama  
  ➜ 공백, 대소문자, 구두점 제거 시 팰린드롬

[숫자]
- 12321, 4554  ➜ 숫자도 팰린드롬이 될 수 있음

※ 예시 문장 전처리:
"A man, a plan, a canal, Panama"
→ "amanaplanacanalpanama"

---------------------------------------

🇰🇷 한글 예시 (재미있는 회문)

- "토마토"       ➜ 거꾸로도 "토마토"
- "별똥별"       ➜ 회문!
- "기러기"       ➜ 유명한 회문 동물 이름
- "스위스"       ➜ (swiss)도 회문이에요
- "여보 안경 안보여" ➜ 공백 제거 시 회문

=======================================
🧪 Palindrome 검사할 문자열을 입력해주세요 : 

"""

    
target_str = input(pelindrome_desc)
pelindrome(target_str)

