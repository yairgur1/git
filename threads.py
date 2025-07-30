import threading

count = 0
loop = 100000

def plus():
    global count, loop
    for i in range(loop):
        count += 1
        print("Current count:", count)

    print("Final count:", count)

def minus():
    global count, loop
    for i in range(loop):
        count -= 1
        print("Current count:", count)

    print("Final count:", count)

t1 = threading.Thread(target = plus)
t2 = threading.Thread(target = minus)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads have finished execution, final count is: ", count)
