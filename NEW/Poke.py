import os
import platform
import time
from PokeData import electronic, water, fire, rock
import matplotlib.pyplot as plt
from PIL import Image


def clear():
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


class PokeMon:
    def __init__(self, name, health, attack):

        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name+' ' + self.health+' ' + self.attack

    def attack1(self, oppo):
        print(f"당신의 {self.name} 포켓몬이 {self.attack * 10} 만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 10
        time.sleep(1)
        clear()
        isDead = oppo.ifDead()
        if not isDead:
            print("상대방 포켓몬의 체력은", oppo.health, "가 되었습니다!")
            time.sleep(1)
            clear()

    def attack2(self, oppo):
        print(f"당신의 {self.name} 포켓몬이 {self.attack * 20} 만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 20
        time.sleep(1)
        clear()
        isDead = oppo.ifDead()
        if not isDead:
            print("상대방 포켓몬의 체력은", oppo.health, "가 되었습니다!")
            time.sleep(1)
            clear()

    def attack3(self, oppo):
        print(f"당신의 {self.name} 포켓몬이 {self.attack * 30} 만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 30
        time.sleep(1)
        clear()
        isDead = oppo.ifDead()
        if not isDead:
            print("상대방 포켓몬의 체력은", oppo.health, "가 되었습니다!")
            time.sleep(1)
            clear()

    def attack4(self, oppo):
        print(f"당신의 {self.name} 포켓몬이 {self.attack * 40} 만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 40
        time.sleep(1)
        clear()
        isDead = oppo.ifDead()
        if not isDead:
            print("상대방 포켓몬의 체력은", oppo.health, "가 되었습니다!")
            time.sleep(1)
            clear()

    def ifDead(self):
        if 0 >= self.health:
            print(f"당신의 {self.name} 포켓몬 이 승리하였습니다.")
            return True
        else:
            return False


Water = water()
a = PokeMon(Water[0][0], float(Water[0][1]), float(Water[0][2]))

Fire = fire()
b = PokeMon(Fire[0][0], float(Fire[0][1]), float(Fire[0][2]))

Elect = electronic()
c = PokeMon(Elect[0][0], float(Elect[0][1]), float(Elect[0][2]))

Rock = rock()
d = PokeMon(Rock[0][0], float(Rock[0][1]), float(Rock[0][2]))

n = int(input("입력하세요 "))

if n == 1:
    a.attack1(b)
    a.attack2(b)
    a.attack3(b)
    a.attack4(b)

if n == 2:
    b.attack1(b)
    b.attack2(b)
    b.attack3(b)
    b.attack4(b)

if n == 3:
    c.attack1(b)
    c.attack2(b)
    c.attack3(b)
    c.attack4(b)

if n == 4:
    d.attack1(b)
    d.attack2(b)
    d.attack3(b)
    d.attack4(b)
