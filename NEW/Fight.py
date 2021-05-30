import time
import os
import platform
# import matplotlib.pyplot as plt
# from PIL import Image


def clear():
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear()

print("포켓몬 세계에 오신것을 환영합니다.")
time.sleep(1)
clear()
while True:

    print("상대방이 포켓몬을 꺼냈습니다.")
    time.sleep(1)
    clear()
    print("당신은 무엇을 할껀가요?(번호를 입력해주세요)")
    print("1. 물기, 2.울기 3.불기 4.웃기")
    n = int(input(""))
    time.sleep(0.5)
    clear()
    print("상대방의 체력이 10 달았습니다.")
    time.sleep(1)
    clear()
    print("상대방의 공격으로 인하여 당신의 체력이 20 달았습니다.")
    time.sleep(1)
    clear()
    print("당신의 포켓몬의 현재 체력은 80입니다.")
    print("당신은 무엇을 할껀가요?(번호를 입력해주세요)")
    print("1. 물기, 2.울기 3.불기 4.웃기")
    n = int(input(""))
    print("당신이 승리 하였습니다.")
    # print("당신의 포켓몬이 쓰러졌습니다. 눈앞이 깜깜해졌습니다.")
    time.sleep(1)
    clear()
    end = int(input("끝내고 싶으면 1을 입력해주세요 "))
    clear()
    if end == 1:
        break


def main():

    # while receive_input():
    #     pass


if __name__ == "__main__":
    main()
