import time

a = time.time()

for i in range(0, 10000):
    pass

print(time.time() - a)