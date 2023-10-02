import matplotlib.pyplot as plt


def IterativeFibonacci(n):
    iterations = 0
    if n == 0 or n == 1:
        iterations += 1
        return {"fibonacci-number": n, "index": n, "iterations": iterations}
    else:
        f0 = 0
        f1 = 1
        f2 = f1 + f0
        iterations += 1
        for i in range(2, n+1):
            iterations += 1
            f2 = f1 + f0
            f0 = f1
            f1 = f2
        return {"fibonacci-number": f2, "index": n, "iterations": iterations}


def RecursiveFibonacci(n, recursive_calls=0):
    if n == 0 or n == 1:
        recursive_calls += 1
        return {"fibonacci_number": 1, "index": n, "recursive_calls": recursive_calls}
    else:
        f0 = RecursiveFibonacci(n-1, recursive_calls)
        f1 = RecursiveFibonacci(n-2, recursive_calls)
        f2 = f1["fibonacci_number"] + f0["fibonacci_number"]
        # this +1 indicates the call of itself
        recursive_calls = f1["recursive_calls"] + f0["recursive_calls"] + 1
        return {"fibonacci_number": f2, "index": n, "recursive_calls": recursive_calls}


# Main Execution
print(RecursiveFibonacci(4))

recursive_data = []
iterative_data = []
for i in range(0, 31, 10):
    print(i)
    iterative_data.append(IterativeFibonacci(i))
    recursive_data.append(RecursiveFibonacci(i))


print("Iterative fibonacci :-")
print(iterative_data)
print("Recursive fibonacci :-")
print(recursive_data)


# For ploting purpose getting more data
recursive_data.clear()
iterative_data.clear()

for i in range(0, 31):
    iterative_data.append(IterativeFibonacci(i))
    recursive_data.append(RecursiveFibonacci(i))

plt.plot(range(0, 31), list(
    map(lambda x: x["iterations"], iterative_data)))
plt.plot(range(0, 31), list(
    map(lambda x: x["recursive_calls"], recursive_data)))

plt.show()
