from random import randint
import time

class Dice:
    
    def __init__(self):
        self.surface = [1, 2, 3, 4, 5, 6]
        self.current_value = 0
    
    def roll_and_get_value(self):
        random_number = randint(0, 5)
        self.current_value = self.surface[random_number]
        return self.current_value
    
    def check_value_is_one(self):
        return self.current_value is 1   
    

class Computer:
    
    def __init__(self):
        self.sub_sum = 0
        self.total_sum = 0
        
    def add_sub_sum(self, value):
        self.sub_sum += value
        
    def accumulate_sub_sum_to_total_sum(self):
        self.total_sum += self.sub_sum
        
    def get_sub_sum(self):
        return self.sub_sum
    
    def get_total_sum(self):
        return self.total_sum
    
    def reset_sub_sum(self):
        self.sub_sum = 0
    
    def check_total_sum_is_over_fifty(self):
        return self.total_sum >= 50
    
    def add_and_check_sub_sum_and_total_sum_is_over_fifty(self):
        return self.total_sum + self.sub_sum >= 50
    
class ComputerAutoPlay:
    
    def __init__(self):
        self.dice = Dice()
        self.computer = Computer()
        
    def start_auto_play(self):
        self.computer.reset_sub_sum()
        print("컴퓨터가 자동으로 플레이를 시작합니다.")
        print(f"컴퓨터의 총 누적 합 >> {self.computer.get_total_sum()}점")
        
        how_many_times = randint(1, 15)
        current_number_of_times = 1
        
        while current_number_of_times <= how_many_times:
            print(f"{current_number_of_times}번째 주사위 굴리는 중...")
            time.sleep(0.8)
            
            dice_value = self.dice.roll_and_get_value()
            print(f"주사위를 굴려 나온 숫자 >> {dice_value}")
            
            if self.dice.check_value_is_one():
                print(f"주사위의 값이 1이 나와 상대방에게 턴을 넘깁니다. 누적 합: {self.computer.get_total_sum()}")
                self.computer.reset_sub_sum()
                return True
            else:
                self.computer.add_sub_sum(dice_value)
                print(f"Sub(Current) 누적 합 >> {self.computer.get_sub_sum()}")  
                if self.computer.add_and_check_sub_sum_and_total_sum_is_over_fifty():
                    self.computer.accumulate_sub_sum_to_total_sum()
                    print(f"총 누적 합이 50이상입니다.\n컴퓨터의 승리로 게임을 종료합니다! 총 누적 합 >> {self.computer.get_total_sum()}")
                    return False
        
            current_number_of_times += 1
            
        self.computer.accumulate_sub_sum_to_total_sum()
        print(f"컴퓨터의 턴이 종료되었습니다. 당신의 턴입니다. 총 누적 합 >> {self.computer.get_total_sum()}")
        return True
