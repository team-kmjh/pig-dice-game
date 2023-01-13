from random import randint
from time import sleep

dice_num  = randint(1, 6+1)
user_result = 0
user_total_result = 0
goal = 10

def roll_dice():
    dice_num = randint(1, 6+1)
    return dice_num

print('Welcome! We start pig-dice-game')
sleep(1)
button = input("Enter 'r' button > ")

if button != 'r':
    print('Enter correct button')
elif button == 'r':    
    while True:
        if button == 'r':
            dice_num = roll_dice()
            print('dice_num =',dice_num)
            if dice_num != 1:
                user_result += dice_num
                print('Your current result =', user_result)
                if user_total_result + user_result >= goal:
                    print('You Win!!')
                    break
                button = input('Roll(r) or Stop(s) ? >')
            else:
                user_result = 0
                break
        elif button == 's':
            break
        
    user_total_result += user_result
    print('Your total result =',user_total_result)