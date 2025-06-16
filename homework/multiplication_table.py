# multiplication table, times table, 파이썬 구구단 홈워크

def case_comprehension_for_state():
    multiplication_table = [(i,j) for i in range(1,10) for j in range(1,10)]

    for i,j in multiplication_table:
        print(f"{i} X {j} = {i*j}")  

def case_comprehension():
    [print(f"{i} X {j} = {i*j}") for i in range(1,10) for j in range(1,10)]


case_comprehension()