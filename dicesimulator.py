import random
while True:
    print('''
    1 Roll dice
    2. To exit''')
    user = int(input("What do you want to do?\n"))
    if user ==1:
        number = random.randint(1,6)
        print(number)
    else:
        break
