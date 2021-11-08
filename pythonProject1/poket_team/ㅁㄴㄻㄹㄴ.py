class PokeSt: #포켓몬 능력치
    def __init__(self, name, hp, n_hp, mp, n_mp, exp, n_exp, skill_1,skill_2,skill_3):
        self.name = name
        self.hp = hp
        self.n_hp = n_hp
        self.mp = mp
        self.n_mp = n_mp
        self.exp = exp
        self.n_exp = n_exp
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3

pokemons = [
    PokeSt("피카츄", 100, 100, 50, 50, 0, 100, 10, 20, 50),
    PokeSt("이브이", 90, 90, 100, 100, 0, 100, 10, 20, 50),
    PokeSt("김상희씨", 120, 120, 30, 30, 0, 100, 10, 20, 50),
    PokeSt("꼬부기", 130, 130, 80, 80, 0, 100, 10, 20, 50)
]

class EpokeSt: #적 포켓몬 능력치
    def __init__(self, name, hp, n_hp, skill_1,skill_2,skill_3):
        self.name = name
        self.hp = hp
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3

Epokemons = [
    EpokeSt("파이리", 80, 10, 20, 50),
    EpokeSt("따라큐", 120, 30, 50, 70)
]

print(pokemons[0].hp - Epokemons[0].skill_1)