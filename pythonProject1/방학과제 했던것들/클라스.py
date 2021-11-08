class EpokeSt: #적 포켓몬 능력치
    def __init__(self, name, n_hp, hp, skill_1_name,skill_2_name,skill_3_name, skill_1,skill_2,skill_3):
        self.name = name
        self.n_hp = n_hp
        self.hp = hp
        self.skill_1_name = skill_1_name
        self.skill_2_name = skill_2_name
        self.skill_3_name = skill_3_name
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3

#a = randint(10,20), 공격력 랜덤넣기

Epokemons = [
    EpokeSt("따라큐", 50, 50, "야습", "섀도크루", "치근거리기", 30, 50, 70),
    EpokeSt("파이리", 40, 40, "할퀴기", "화염방사", "지구던지기", 10, 20, 50)

]



x = Epokemons[0].name

print(x)