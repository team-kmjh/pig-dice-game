from computer import ComputerAutoPlay

if __name__ == "__main__":
    
    computer = ComputerAutoPlay()
    
    while True:
        
        if computer.start_auto_play():
            print("컴퓨터의 auto play 종료...")
        else:
            break