class PokeMon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def print_name(self):
        print(self.name)

    def attack1(self, oppo):
        print(f"{self.name}이{self.attack * 10}만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 10
        print("상대의 체력은 ", oppo.health, "가 되었습니다!")

    def attack2(self, oppo):
        print(f"{self.name}이{self.attack * 20}만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 20
        print("상대의 체력은 ", oppo.health, "가 되었습니다!")

    def attack3(self, oppo):
        print(f"{self.name}이{self.attack * 30}만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 30
        print("상대의 체력은 ", oppo.health, "가 되었습니다!")

    def attack4(self, oppo):
        print(f"{self.name}이{self.attack * 40}만큼 상대방을 공격했습니다!")
        oppo.health -= self.attack * 40
        isDead = oppo.ifDead()
        if not isDead:
            print("상대의 체력은 ", oppo.health, "가 되었습니다!")
            
    def ifDead(self):
        if 0 >= self.health:
            print(f"{self.name}이 끝났습니다.")
            image = Image.open(os.path.join('a.jpeg'))
            plt.imshow(image)
            plt.show()
            return True
        else:
            return False

test_water = water()
a = PokeMon(test_water[0][0], float(test_water[0][1]), float(test_water[0][2]))

test_fire = fire()
b = PokeMon(test_fire[0][0], float(test_fire[0][1]), float(test_fire[0][2]))

n = int(input("입력하세요 "))
a.attack1(b)
b.attack1(a)
a.attack2(b)
b.attack2(a)
a.attack3(b)
b.attack3(a)
a.attack4(b)
b.attack4(a)

