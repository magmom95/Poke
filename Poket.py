class PoketMon:

    def __init__(self, skill):
        self.skill = skill

    def attack(self):
        print(+self.skill + "을 수행합니다.")


class my(PoketMon):

    def __init__(self, type, skill):
        self.skill = skill
        self.type = type


class com(PoketMon):

    def __init__(self, type, skill):
        self.skill = skill
        self.type = type
