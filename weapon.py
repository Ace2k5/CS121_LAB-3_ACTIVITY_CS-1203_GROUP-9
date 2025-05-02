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
    def __init__(self, name_weapon, type_gun):
        super().__init__(name_weapon)
        self._type_gun = type_gun
    def damage(self):
        if self._type_gun == "Pistol":
            ammo = 12
            temp_list = []
            temp_total_damage = 0
            while ammo > 0:
                ammo -=1
                chance = 0.1
                chance_number = round(random.random(), 2)
                print(chance_number)
                damage1 = random.randint(50, 100)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        

        elif self._type_gun == "Rifle":
            ammo = 30
            temp_list = []
            temp_total_damage = 0
            while ammo > 0:
                ammo -=1
                chance = 0.2
                chance_number = round(random.random(), 2)
                print(chance_number)
                damage1 = random.randint(50, 100)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                time.sleep(0.2)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        

        elif self._type_gun == "Sniper":
            ammo = 5
            temp_list = []
            temp_total_damage = 0
            while ammo > 0:
                ammo -=1
                chance = 0.01
                chance_number = round(random.random(), 2)
                print(chance_number)
                damage1 = random.randint(100, 5000)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                time.sleep(2)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        

        elif self._type_gun == "Shotgun":
            ammo = 9
            temp_list = []
            temp_total_damage = 0
            chance = 0.45
            while ammo > 0:
                ammo -=1
                for i in range(9):
                    chance_number = round(random.random(), 2)
                    print(chance_number)
                    damage1 = random.randint(50, 100)
                    if chance_number > chance:
                        print(f"You have inflicted: {damage1} points of damage.")
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                print("Stabilizing...")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
    
class Bow(Weapon):
    def __init__(self, name_weapon, range):
        super().__init__(name_weapon)
        self._range = range
    
    def damage(self):
        damage1 = random.randint(70, 120)
        return damage1

class RocketLauncher(Weapon):
    def __init__(self, name_weapon, rocket_type):
        super().__init__(name_weapon)
        self._rocket_type = rocket_type
        self._rockets = 3

    def damage(self):
        total_damage = 0

        if self._rockets <= 0:
            print("No mor rockets")
            return 0

        print(f"Firing 3 {self._rocket_type} rockets...")

        for _ in range(3):
            if self._rockets <= 0:
                print("Out of rockets!")
                break

            self._rockets -= 1
            print(f"Firing {self._rocket_type} rocket...")

            time.sleep(1.5)
            
            if self._rocket_type == "Explosive":
                damage_value = random.randint(400, 700)
                print(f"BOOOOOM!!! You dealt {damage_value} explosive damage")
                total_damage += damage_value

            elif self._rocket_type == "Nuclear":
                chance = 0.3
                crit_chance = round(random.random(), 2)
                if crit_chance < chance:
                    damage_value = random.randint(1000, 3000)
                    print(f"DAAAAAAAAAMN CRITICAL HIT!! You dealt {damage_value} nuclear damage!!")
                    total_damage += damage_value
                else:
                    damage_value = random.randint(300, 500)
                    print(f"You dealt {damage_value} nuclear damage!!!")
                    total_damage += damage_value

            else:
                print("Unknown rocket type.")
                return 0
            
            time.sleep(3)

        print(f"You have inflicted a total of: {total_damage} point of damage")
        return total_damage

def random_weapon():
    x = 2
    print(f"You have rolled {x}")

    if x == 1:
        option = ["NONE", "Iron", "Wood", "Copper", "Silver"]
        temp1 = str(input("Choose a name for the sword: "))
        if temp1 == "":
            print("Enter a valid name.")
            return
        print(f"You have a total of {len(option) - 1} of choices. Choose one:")
        for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
        temp2 = int(input("Choose between 1-4: "))
        sword_temp = Sword(temp1, option[temp2])
        return sword_temp
    
    elif x == 2:
        option = ["NONE", "Pistol", "Rifle", "Sniper", "Shotgun"]
        temp1 = str(input("Choose a name for the gun: "))
        if temp1 == "":
            print("Enter a valid name.")
            return
        print(f"You have a total of {len(option) - 1} of choices. Choose one:")
        for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
        temp2 = int(input("Choose between 1-4: "))
        gun_temp = Gun(temp1, option[temp2])
        return gun_temp

    elif x == 3:
        option = ["NONE", "Explosive", "Nuclear"]
        temp1 = str(input("Choose a name for the rocket launcher: "))
        if temp1 == "":
            print("Enter a valid name.")
            return
        print("Choose a rocket type:")
        for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
        temp2 = int(input("Choose 1 or 2: "))
        rocket_temp = RocketLauncher(temp1, option[temp2])
        rocket_temp.status()
        return rocket_temp
    



a = random_weapon()
a.damage()
