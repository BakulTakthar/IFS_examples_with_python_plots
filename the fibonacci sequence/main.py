import matplotlib.pyplot as plt

lim_arr = []
value_arr = []


def function_for_fibonacci(lim):
    start = 1
    current = 0
    for i in range(lim):
        lim_arr.append(i)
        value = current + start
        value_arr.append(value)
        current = value
    print(lim_arr)
    print(value_arr)

function_for_fibonacci(2000)
plt.scatter(lim_arr, value_arr)
plt.show()

