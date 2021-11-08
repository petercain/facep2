class poketmon: #포켓몬 능력치
    def __init__(self, name,hp, mp, exp):
        self.name = name #이름
        self.hp = hp #최대 체력
        self.mp = mp #최대 마나
        self.exp = exp #최대 경험치
        self.skills = {} #포켓몬의 속성으로 묶어둘러고

class skills:
    def __init__(self, damage, ump):
        self.damage = damage
        self.ump = ump

pika = poketmon("피카츄", 100, 100, 0)

kkobook = poketmon("꼬북이", 110, 90, 0)

pika.skills = {"몸통박치기":skills(10,0), "백만볼트":skills(20,10)}

kkobook.skills = {"몸통박치기":skills(10,0), "물대포":skills(30,15)}

print(pika.name, pika.skills["백만볼트"].damage, pika.skills["백만볼트"].ump)
print(kkobook.name, kkobook.skills["물대포"].damage, kkobook.skills["물대포"].ump)