import random

r  = random.randint(1,100)
count = 0
while True:
    count += 1 #count = count +1
    userGuess = input("請輸入數字: ")
    userGuess = int(userGuess)
    if userGuess == r:
        print('終於猜對了')       
        break
    elif userGuess > r:
        print('太大了  小一點')

    elif userGuess < r:
        print('太小了 大一點') 
print('總共猜了', count, '次')