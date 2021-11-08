class PokeSt: #포켓몬 능력치
    def __init__(self, name, n_hp, hp, n_mp, mp, n_exp, exp, skill_1_name,skill_2_name,skill_3_name, skill_1,skill_2,skill_3):
        self.name = name #이름
        self.n_hp = n_hp #현재 체력
        self.hp = hp #최대 체력
        self.n_mp = n_mp #현재 마나
        self.mp = mp #최대 마나
        self.n_exp = n_exp #현재 경험치
        self.exp = exp #최대 경험치
        self.skill_1_name = skill_1_name #1스킬 이름
        self.skill_2_name = skill_2_name #2스킬 이름
        self.skill_3_name = skill_3_name #3스킬 이름
        self.skill_1 = skill_1 #1스킬 데미지
        self.skill_2 = skill_2 #2스킬 데미지
        self.skill_3 = skill_3 #3스킬 데미지

pokemons = [
    PokeSt("피카츄 Lv.1", 100, 100, 50, 50, 0, 100, "전광석화", "아이언테일", "백만볼트", 10, 20, 50)
]

pokemons[0].exp += 140

print(pokemons[0].exp)