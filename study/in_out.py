def add_mul(choice, *args):
    
    if choice == "add":
        result = 0
        for i in args:
            result += i

    elif choice == "mul":
        result = 1
        for i in args:
            result *= i

    return result


print(add_mul("mul",1,2,3,4,5,6,7,9))



def vartest(a):
    a = a + 1

vartest(3)

print(a)