

def use_for_state_fibonacci(num_range: int):
    fibonacci_seq = []
    for i in range(0, num_range):
        if i in [0,1]:
            fibonacci_seq.append(i)
        else:
            fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    print(f'{fibonacci_seq}')    


def use_comprehension_and_init_seq_fibonacci():
    init_seq = [0,1]
    [init_seq.append(init_seq[i-1] + init_seq[i-2]) for i in range(2,10)]
    print(f'{init_seq}')


def use_comprehension_fibonacci():
    fibonacci_seq = []
    fibonacci_seq = [i if i <= 1 else fibonacci_seq[i-1] + fibonacci_seq[i-2] for i in range(0,10)]


use_comprehension_fibonacci()