# import re
# date 읽기
def Poke_read():
    all = []
    with open('myPoke.csv', 'r', encoding='utf-8') as f:
        data = f.readlines()
        for v in data:
            v = v.strip().split(',')
            all.append(v)

    return all


def water():
    water_set = []
    for i in Poke_read():
        if '물' in i:
            water_set.append(i)

    return water_set


def fire():
    fire_set = []
    for i in Poke_read():
        if '불' in i:
            fire_set.append(i)

    return fire_set
