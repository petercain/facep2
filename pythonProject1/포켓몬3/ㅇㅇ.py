class Variable:
    S_pokemon = 0 #스타팅 포켓몬 선택


class PokeSt: #포켓몬 능력치
    def __init__(self,name, hp, mp, exp, skill_1,skill_2,skill_3):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.exp = exp
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
pokemons = [
    PokeSt("피카츄", 100, 100 , 0, 10, 20, 50),
    PokeSt("이브이", 100, 100 , 0, 10, 20, 50),
    PokeSt("김상희씨", 100, 100 , 0, 10, 20, 50),
    PokeSt("꼬부기", 100, 100 , 0, 10, 20, 50)
]

print(pokemons[Variable.S_pokemon].name)