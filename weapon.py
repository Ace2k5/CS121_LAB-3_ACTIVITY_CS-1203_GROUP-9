import random
from abc import ABC, abstractmethod
import time
import keyboard

class Weapon(ABC):
    def __init__(self, name_weapon):
        self.__name_weapon = name_weapon
    def damage(self):
        pass
    def reload(self):
        pass

class Sword(Weapon):
    def __init__(self, name_weapon, material):
        super().__init__(name_weapon)
        self._material = material

    def damage(self):
        damage1 = random.randint(30, 70)
        return int(damage1)

class Gun(Weapon):
    def __init__(self, name_weapon, ammo_count):
        super().__init__(name_weapon)
        self.ammo_count = ammo_count
    def damage(self):
        self.damage = random.randint(100, 200)
        return int(self.damage)
    
class Bow(Weapon):
    def __init__(self, name_weapon, range):
        super().__init__(name_weapon)
        self._range = range
    
    def damage(self):
        self.damage = random.randint(70, 120)
        return self.damage

class RocketLauncher(Weapon):
    def __init__(self, name_weapon):
        super().__init__(name_weapon)

def random_weapon():
    x = 1
    print(f"You have rolled {x}")
    if x == 1:
        option = ["NONE", "Iron", "Wood", "Copper", "Silver"]
        temp_list = []
        temp1 = str(input("Choose a name for the sword: "))
        if temp1 == "":
            print("Enter a valid name.")
        print(f"You have a total of {len(option) - 1} of choices. Choose one:")
        for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
        temp2 = int(input("Choose between 1-4: "))
        sword_temp = Sword(temp1, option[temp2])
        return sword_temp
    if x == 2:
        gun_temp = Gun()
    



a = random_weapon()
print(a.damage())
