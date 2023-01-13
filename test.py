from computer import ComputerAutoPlay
from user import UserPlay

if __name__ == "__main__":
    
    computer = ComputerAutoPlay()
    user = UserPlay()
    
    while True:
        if user.start_play():
           print('사용자의 paly 종료...\n\n\n')

        else:
            break


        if computer.start_auto_play():
            print("컴퓨터의 auto play 종료...\n\n\n")
        else:
            break