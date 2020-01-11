import time

target = int(input("How long do you want to count for? (seconds) "))

i = 0
while i < target:
    print(str(i // 60) + ":" + str(i % 60))
    time.sleep(1)
    i += 1
