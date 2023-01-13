from random import randint
from time import sleep

class Dice:

    def __init__(self):
        self.surface = [1,2,3,4,5,6]
        self.current_value = 0
    
    def roll_and_get_value(self):
        random_number = randint(0, 5)
        self.current_value = self.surface[random_number]
        return self.current_value
    def check_value_is_one(self):
        return self.current_value is 1

class User:

    def __init__(self):
        self.sub_sum = 0
        self.total_sum = 0
    
    def add_sub_num(self, value):
        self.sub_sum += value

    def accumulate_sub_sum_to_total_sum(self):
        self.total_sum += self.sub_sum
    
    def get_sub_sum(self):
        return self.sub_sum

    def get_total_sum(self):
        return self.total_sum

    def reset_sub_sum(self):
        self.sub_sum = 0
    
    def check_total_sum_is_over_fifyy(self):
        return self.total_sum >= 50
    
    def add_and_check_sub_sum_and_total_sum_is_over_fifty(self):
        return self.total_sum + self.sub_sum >= 50

class UserPlay:

    def __init__(self):
        self.dice = Dice()
        self.user = User()

    def start_play(self):
        self.user.reset_sub_sum()
        print('사용자가 플레이를 시작합니다.')
        print(f'사용자의 누적 합 >> {self.user.get_total_sum()}점')

        while True:
            button = input('Roll(r) or Stop(s) ? >')
            sleep(1)
            if button == 'r':
                dice_value = self.dice.roll_and_get_value()
                print(f'주사위를 굴려서 나온 숫자 >> {dice_value}')
                if self.dice.check_value_is_one():
                    print(f'주사위의 값이 1이 나와 컴퓨터에게 턴을 넘깁니다. 누적합: {self.user.get_total_sum()}')
                    self.user.reset_sub_sum()
                    return True
                else:
                    self.user.add_sub_num(dice_value)
                    print(f'Sub(Current) 누적합 >> {self.user.get_sub_sum()}') 
                    if self.user.add_and_check_sub_sum_and_total_sum_is_over_fifty():
                        self.user.accumulate_sub_sum_to_total_sum()
                        print(f'총 누적 합이 50이상입니다.\n 사용자의 승리로 게임을 종료합니다.! 총 누적 합 >> {self.user.get_total_sum()}')
                        return False
            elif button == 's':
                self.user.accumulate_sub_sum_to_total_sum()
                print(f'사용자의 턴이 종료되었습니다. 컴퓨터의 턴입니다. 사용자 누적 합 >> {self.user.get_total_sum()}')
                return True