def print_fibonacci(length):
    if length <= 0:
        print([])
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < length:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print(fibonacci[:length])
