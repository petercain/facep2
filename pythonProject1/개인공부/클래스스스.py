# class Example:
#     def __init__(self, name, age):
#         self.name = name + "님"
#         self.age = age + 5
#
#         print("self123.name의 값 : {}\n그냥 name의 값 : {}\n".format(self.name, name))
#         print("self123.age.의 값 : {}\n그냥 age의 값 : {}".format(self.age, age))
#
# a = Example("chris", 20)



class Example2:
    def self_method(self, param1):
        print("parameter1 : {}".format(param1))

    def non_self_method(param2):
        print("parameter2 : {}".format(param2))

try:
    Example2().self_method(1000)
    Example2().non_self_method(1000)
except:
    pass

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성 되었습니다.".format(self.name))
        print("체력{}, 공격력 {}".format(self.hp, self.damage))

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 데미지 : {}".format(wraith1.name, wraith1.damage))
try:
    if wraith1.clocking == True:
        print("{}는 현재 클로킹 상태입니다.".format(wraith1.name))
except:
    pass

wraith2 = Unit("망령", 85, 10)
wraith2.clocking = True
try:
    if wraith2.clocking == True:
        print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))
except:
    pass