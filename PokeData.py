from Poke import PokeMon
# import re


class Data:
    def Poke_read():
        all = []
        with open('myPoke.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

            for v in data:
                v = v.split(',')
                all.append(PokeMon(v[0], v[1], v[2]))

        return all
