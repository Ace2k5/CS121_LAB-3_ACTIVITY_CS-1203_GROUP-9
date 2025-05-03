import random
from abc import ABC, abstractmethod
import time, sys
from pathlib import Path
import pygame
### ----------IMPORTANT FOR ERLKING GREATSWORD-------- ###
sound_folder = Path("CS121_LAB-3_ACTIVITY_CS-1203_GROUP-9/sounds")
AWAKENING = sound_folder / "Erlking's_AWAKENING.mp3"
LIST_OF_SOUNDS_ERLKING = [
    sound_folder / "battle1.mp3",
    sound_folder / "battle2.mp3",
    sound_folder / "battle3.mp3",
    sound_folder / "battle4.mp3",
    sound_folder / "battle5.mp3"
]
LIST_OF_SWORDSOUNDS = [
    sound_folder / "sound2.mp3"
]
REQUIEM_SOUNDS = [
    sound_folder / "requiem1.mp3",
    sound_folder / "requiem2.mp3",
    sound_folder / "requiem3.mp3"
]
LEAVE_SOUND = sound_folder / "leave.mp3"
pygame.mixer.init()
def play_music():
    pygame.mixer.music.load(f"{sound_folder}/erlking_theme.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()

class Weapon(ABC):
    def __init__(self, name_weapon):
        self._name_weapon = name_weapon
    def damage(self):
        pass
    def reload(self):
        pass

class Sword(Weapon):
    def __init__(self, name_weapon, material):
        super().__init__(name_weapon)
        self._material = material

    def damage(self):
        if self._material == "Erlking's Greatsword":
            play_music()
            entry = pygame.mixer.Sound(str(AWAKENING))
            entry.play()
            temp_text = "I have returned once again."
            temp_text2 = " To face Catherine..."
            temp_text3 = " and the accursed wretches of the manor."
            sound = pygame.mixer.Sound(str(AWAKENING))
            sound.play
            for letter in temp_text:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.9)
            for letter in temp_text2:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(0.8)
            for letter in temp_text3:
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(0.05)
            while pygame.mixer.get_busy():
                    time.sleep(1)
            while True:
                temp_text = "1. Beheading ⦿⦿ (WRATH)"
                temp_text2 = "2. Memorial Processing ⦿⦿⦿ (ENVY)"
                temp_text3 = "3. Requiem ⦿⦿ (GLOOM)"
                print()
                for letter in temp_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                time.sleep(0.5)
                for letter in temp_text2:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                time.sleep(0.5)
                for letter in temp_text3:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                time.sleep(0.5)
                temp_text = "Choose a skill(Input 4 to leave): "
                for letter in temp_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(0.05)
                temp_input = int(input(""))
                if temp_input == 1:
                    slash = 2
                    temp_list = []
                    temp_sum = 0
                    while slash > 0:
                        temp_text = "Beheading ⦿⦿ (WRATH)"
                        for letter in temp_text:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.05)
                        sound_select = random.randint(0, 4)
                        sound = pygame.mixer.Sound(LIST_OF_SOUNDS_ERLKING[sound_select])
                        sound.play()
                        time.sleep(0.5)
                        print()
                        sword_sound = 0
                        for i in range(2):
                            damage = random.randint(10, 50)
                            sound = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[sword_sound])
                            sound.play()
                            print(f"You have dealt: {damage} amount of damage.")
                            slash -= 1
                            temp_list.append(damage)
                            while pygame.mixer.get_busy():
                                time.sleep(0.01)
                        for i in range(len(temp_list)):
                            temp_sum += temp_list[i]
                        print(f"You have dealt: {temp_sum} amount of damage in two slashes.")
                        continue  
                elif temp_input == 2:
                    slash = 3
                    temp_list = []
                    temp_sum = 0
                    while slash > 0:
                        temp_text = "Memorial Processing ⦿⦿⦿ (ENVY)"
                        for letter in temp_text:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.05)
                        sound_select = random.randint(0, 4)
                        sound = pygame.mixer.Sound(LIST_OF_SOUNDS_ERLKING[sound_select])
                        sound.play()
                        time.sleep(0.5)
                        print()
                        sword_sound = 0
                        for i in range(3):
                            damage = random.randint(5, 35)
                            sound = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[sword_sound])
                            sound.play()
                            print(f"You have dealt: {damage} amount of damage.")
                            slash -= 1
                            temp_list.append(damage)
                            while pygame.mixer.get_busy():
                                time.sleep(0.01)
                        for i in range(len(temp_list)):
                            temp_sum += temp_list[i]
                        print(f"You have dealt: {temp_sum} amount of damage in three slashes.")
                        continue
                elif temp_input == 3:
                    slash = 2
                    temp_list = []
                    temp_sum = 0
                    while slash > 0:
                        temp_text = "REQUIEM ⦿⦿ (GLOOM)"
                        for letter in temp_text:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(0.05)
                        sound_select = random.randint(0, 4)
                        sound = pygame.mixer.Sound(LIST_OF_SOUNDS_ERLKING[sound_select])
                        sound.play()
                        time.sleep(0.5)
                        print()
                        damage = random.randint(50, 80)
                        sound = pygame.mixer.Sound(REQUIEM_SOUNDS[0])
                        sound.play()
                        print(f"You have dealt: {damage} amount of damage.")
                        slash = 1
                        temp_list.append(damage)
                        while pygame.mixer.get_busy():
                            time.sleep(0.01)
                        for i in range(3):
                            sound = pygame.mixer.Sound(REQUIEM_SOUNDS[1])
                            sound.play()
                            time.sleep(0.5)
                        while pygame.mixer.get_busy():
                            time.sleep(0.01)
                        sound = pygame.mixer.Sound(LIST_OF_SOUNDS_ERLKING[2])
                        sound.play()
                        damage = random.randint(100, 135)
                        print(f"You have dealt: {damage} amount of damage.")
                        temp_list.append(damage)
                        slash = 0
                        sound = pygame.mixer.Sound(REQUIEM_SOUNDS[2])
                        sound.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.01)
                    for i in range(len(temp_list)):
                        temp_sum += temp_list[i]
                    print(f"You have dealt a total of: {temp_sum} while doing 2 blunt attacks.")
                    continue
                elif temp_input == 4:
                    stop_music()
                    sound = pygame.mixer.Sound(LEAVE_SOUND)
                    sound.play()
                    text1 = "What a sorry mess this is..."
                    text2 = " no matter."
                    text3 = " I will return."
                    text4 = " I will return again and again until the day I crush Wuthering Heights between my teeth."
                    for letter in text1:
                        sys.stdout.write(letter)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.9)
                    for letter in text2:
                        sys.stdout.write(letter)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.9)
                    for letter in text3:
                        sys.stdout.write(letter)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(1.3)
                    for letter in text4:
                        sys.stdout.write(letter)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(0.9)
                    while pygame.mixer.get_busy():
                        time.sleep(0.01)
                    break      
        if self._material == "Iron":
            slash = random.randint(1,8)
            temp_slash = slash
            temp_list = []
            temp_total_damage = 0
            while slash > 0:
                slash -=1
                chance = 0.1
                chance_number = round(random.random(), 2)
                damage1 = random.randint(50, 100)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have been parried.")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage.")
        
        elif self._material == "Wood":
            slash = random.randint(1,4)
            temp_slash = slash
            temp_list = []
            temp_total_damage = 0
            while slash > 0:
                slash -=1
                chance = 0.3
                chance_number = round(random.random(), 2)
                damage1 = random.randint(10, 30)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have been parried.")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage.")
        
        elif self._material == "Copper":
            slash = random.randint(1,6)
            temp_slash = slash
            temp_list = []
            temp_total_damage = 0
            while slash > 0:
                slash -=1
                chance = 0.2
                chance_number = round(random.random(), 2)
                damage1 = random.randint(20, 50)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have been parried.")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage.")
        
        elif self._material == "Silver":
            slash = random.randint(1,7)
            temp_slash = slash
            temp_list = []
            temp_total_damage = 0
            while slash > 0:
                slash -=1
                chance = 0.15
                chance_number = round(random.random(), 2)
                damage1 = random.randint(40, 80)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have been parried.")
                time.sleep(1)
            for i in range(len(temp_list)):
                temp_total_damage += temp_list[i]
            return print(f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage.")
        
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
        if self._range == "Low":
            arrows = 12
            temp_list = []
            temp_total_damage = 0
            chance = 0.2
            while arrows > 0:
                arrows -=1
                chance_number = round(random.random(), 2)
                damage1 = random.randint(20, 60)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                print("putting another arrow...")
                time.sleep(1)
                print("Aiming...")
                time.sleep(1)
            else:
                print("No more arrows")
            for i in range(len(temp_list)): 
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        elif self._range == "Medium":
            arrows = 12
            temp_list = []
            temp_total_damage = 0
            chance = 0.2
            while arrows > 0:
                arrows -=1
                chance_number = round(random.random(), 2)
                damage1 = random.randint(60, 80)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                print("putting another arrow...")
                time.sleep(1)
                print("Aiming...")
                time.sleep(1)
            else:
                print("No more arrows")
            for i in range(len(temp_list)): 
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        elif self._range == "High":
            arrows = 12
            temp_list = []
            temp_total_damage = 0
            chance = 0.2
            while arrows > 0:
                arrows -=1
                chance_number = round(random.random(), 2)
                damage1 = random.randint(80, 100)
                if chance_number > chance:
                    print(f"You have inflicted: {damage1} points of damage.")
                    temp_list.append(damage1)
                else:
                    print(f"You have missed.")
                print("putting another arrow...")
                time.sleep(1)
                print("Aiming...")
                time.sleep(1)
            else:
                print("No more arrows")
            for i in range(len(temp_list)): 
                temp_total_damage += temp_list[i]
            return print(f"You have inflicted a total of: {temp_total_damage} point of damage.")
        else:
            print("Invalid range. Please choose between Low, Medium, or High.")
            return 0

class RocketLauncher(Weapon):
    def __init__(self, name_weapon, rocket_type):
        super().__init__(name_weapon)
        self._rocket_type = rocket_type
        self._rockets = 3

    def damage(self):
        total_damage = 0

        if self._rockets <= 0:
            print("No more rockets")
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
                print(f"BOOOOOM!!! You dealt {damage_value} explosive damage!!")
                total_damage += damage_value

            elif self._rocket_type == "Nuclear":
                chance = 0.3
                crit_chance = round(random.random(), 2)
                if crit_chance < chance:
                    damage_value = random.randint(1000, 3000)
                    print(f"CRITICAL HIT!! You dealt {damage_value} nuclear damage!!")
                    total_damage += damage_value
                else:
                    damage_value = random.randint(500, 700)
                    print(f"BOOOOOOOM!!! You dealt {damage_value} nuclear damage!!!")
                    total_damage += damage_value

            else:
                print("Unknown rocket type.")
                return 0

            time.sleep(3)

        print(f"You have inflicted a total of: {total_damage} point of damage")
        return total_damage

def random_weapon():
    x = random.randint(1, 4)
    print(f"You have rolled {x}.")

    if x == 1:
        print("You have been given a Sword!")
        option = ["NONE", "Iron", "Wood", "Copper", "Silver", "Erlking's Greatsword"]
        temp1 = str(input("Choose a name for the sword: "))
        if temp1 == "":
            print("Enter a valid name.")
            return
        print(f"You have a total of {len(option) - 1} of choices. Choose one:")
        for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
        temp2 = int(input("Choose between 1-5: "))
        sword_temp = Sword(temp1, option[temp2])
        return sword_temp
    
    elif x == 2:
        print("You have been given a Gun!")
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
        print("You have been given a Rocket Launcher!")
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
        return rocket_temp
    elif x == 4:
         option = ["NONE", "Low", "Medium", "High"]
         temp1 = str(input("Choose a name for the bow and arrow: "))
         if temp1 == "":
            print("Enter a valid name.")
            return
         print("Choose a bow's range:")
         for i in range(1, len(option)):
            print(f"{i} for {option[i]}")
         temp2 = int(input("Choose 1 to 3: "))
         bow_temp = Bow(temp1, option[temp2])
         return bow_temp
    

a = random_weapon()
a.damage()

#Changes ko (Basty) dito ay tinanggal ko muna ung mga miss chances na print, nilagyan ko na don sa sword class, naglagay den ako ng print("You have been given a Sword!") kada weapon. yon lungs
