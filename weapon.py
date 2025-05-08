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
SWORD_PARRIED = sound_folder / "parried.mp3"
REQUIEM_SOUNDS = [
    sound_folder / "requiem1.mp3",
    sound_folder / "requiem2.mp3",
    sound_folder / "requiem3.mp3"
]
LEAVE_SOUND = sound_folder / "leave.mp3"

PISTOL_FIRE = sound_folder / "pistolfire.mp3"
PISTOL_RELOAD = sound_folder / "pistol_reload.mp3"


RIFLE_FIRE = sound_folder / "riflefire.mp3"
RIFLE_RELOAD = sound_folder / "rifle_reload.mp3"

SNIPER_FIRE = sound_folder / "sniperfire.mp3"
SNIPER_RELOAD = sound_folder / "sniper_reload.mp3"

SHOTGUN_FIRE = sound_folder / "shotgunfire.mp3"
SHOTGUN_RELOAD = sound_folder / "shotgun_reload.mp3"
SHOTGUN_COCKING = sound_folder / "shotguncocking.mp3"


COUNTDOWN_ROCKETLAUNCHER = sound_folder / "siren_rocketlauncher.mp3"
EXPLOSION_ROCKET1 = sound_folder / "explosionrocket1.mp3"
EXPLOSION_ROCKET2 = sound_folder / "explosionrocket2.mp3"
NUCL_LAUNCH = sound_folder / "nuclrocketlauncher.mp3"
EXPL_LAUNCH = sound_folder / "explrocketlauncher.mp3"
ROCKET_RELOAD = sound_folder / "rocketlauncher_reload.mp3"

BOW_AIMING = sound_folder / "bow_aiming.mp3"
BOW_HIT = sound_folder / "bow_hit.mp3"
BOW_MISS = sound_folder / "bow_miss.mp3"

UNIVERSAL_MISS = sound_folder / "miss.mp3"
pygame.mixer.init()
pygame.mixer.set_num_channels(50)
def play_music():
    pygame.mixer.music.load(f"{sound_folder}\erlking_theme.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()

class Weapon(ABC):
    def __init__(self, name_weapon):
        self._name_weapon = name_weapon
    def sword_logic(self):
        pass
    def gun_logic(self):
        pass
    def bow_logic(self):
        pass
    def rocket_launcher_logic(self):
        pass

class Sword(Weapon):
    def __init__(self, name_weapon, material):
        super().__init__(name_weapon)
        self._material = material

    def sword_logic(self):
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
                            while pygame.mixer.get_busy():
                                time.sleep(1)
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
            while True:
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
                        s = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[0])
                        s.play()
                        temp_list.append(damage1)
                    else:
                        s = pygame.mixer.Sound(SWORD_PARRIED)
                        s.play()
                        print(f"You have been parried.")
                    time.sleep(1)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage."
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        
        elif self._material == "Wood":
            while True:
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
                        s = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[0])
                        s.play()
                        temp_list.append(damage1)
                    else:
                        s = pygame.mixer.Sound(SWORD_PARRIED)
                        s.play()
                        print(f"You have been parried.")
                    time.sleep(1)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage."
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        
        elif self._material == "Copper":
            while True:
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
                        s = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[0])
                        s.play()
                        temp_list.append(damage1)
                    else:
                        s = pygame.mixer.Sound(SWORD_PARRIED)
                        s.play()
                        print(f"You have been parried.")
                    time.sleep(1)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage."
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        
        elif self._material == "Silver":
            while True:
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
                        s = pygame.mixer.Sound(LIST_OF_SWORDSOUNDS[0])
                        s.play()
                        temp_list.append(damage1)
                    else:
                        s = pygame.mixer.Sound(SWORD_PARRIED)
                        s.play()
                        print(f"You have been parried.")
                    time.sleep(1)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have swung a total of {temp_slash} time(s). \nYou have inflicted a total of: {temp_total_damage} point of damage."
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0

                
    def run(self):
        self.sword_logic()
        
class Gun(Weapon):
    def __init__(self, name_weapon, type_gun):
        super().__init__(name_weapon)
        self._type_gun = type_gun
    def gun_logic(self):
        if self._type_gun == "Pistol":
            while True:
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
                        s = pygame.mixer.Sound(PISTOL_FIRE)
                        s.play()                        
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                        s = pygame.mixer.Sound(UNIVERSAL_MISS)
                        s.play()
                    time.sleep(0.5)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(PISTOL_RELOAD)
                        s.play()
                        time.sleep(2)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0

        elif self._type_gun == "Rifle":
            while True:
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
                        s = pygame.mixer.Sound(RIFLE_FIRE)
                        s.play()
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                        s = pygame.mixer.Sound(UNIVERSAL_MISS)
                        s.play()
                    time.sleep(0.1)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(RIFLE_RELOAD)
                        s.play()
                        time.sleep(3.5)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        time.sleep(3)
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        

        elif self._type_gun == "Sniper":
            while True:
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
                        s = pygame.mixer.Sound(SNIPER_FIRE)
                        s.play()
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                    time.sleep(2)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(SNIPER_RELOAD)
                        s.play()
                        time.sleep(3.5)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        

        elif self._type_gun == "Shotgun":
            while True:
                ammo = 8
                temp_list = []
                temp_total_damage = 0
                chance = 0.45
                while ammo > 0:
                    ammo -= 1
                    s = pygame.mixer.Sound(SHOTGUN_FIRE)
                    s.play()
                    for i in range(9):
                        chance_number = round(random.random(), 2)
                        damage1 = random.randint(50, 100)
                        if chance_number > chance:
                            print(f"You have inflicted: {damage1} points of damage.")
                            temp_list.append(damage1)
                        else:
                            print("You have missed.")
                    time.sleep(0.2)
                    print("Stabilizing...")
                    s = pygame.mixer.Sound(SHOTGUN_COCKING)
                    s.play()
                    time.sleep(1)

                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)

                temp_inp = str(input("Attack one more? (Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(SHOTGUN_RELOAD)
                        s.play()
                        time.sleep(4.5)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
    def run(self):
        self.gun_logic()
    
class Bow(Weapon):
    def __init__(self, name_weapon, range):
        super().__init__(name_weapon)
        self._range = range
    
    def bow_logic(self):
        if self._range == "Low":
            print("The enemy is in close range.")
            time.sleep(1.5)
            while True:
                arrows = 12
                temp_list = []
                temp_total_damage = 0
                chance = 0.2
                print("putting an arrow...")
                time.sleep(1)
                while arrows > 0:
                    arrows -=1
                    chance_number = round(random.random(), 2)
                    damage1 = random.randint(20, 60)
                    print("Aiming...")
                    s = pygame.mixer.Sound(BOW_AIMING)
                    s.play()
                    while pygame.mixer.get_busy():
                        time.sleep(0.1)
                    if chance_number > chance:
                        print(f"You have inflicted: {damage1} points of damage.")
                        s = pygame.mixer.Sound(BOW_HIT)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                        time.sleep(0.5)
                        s = pygame.mixer.Sound(BOW_MISS)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                    if arrows > 0:
                        print("putting another arrow...")
                        time.sleep(1)
                else:
                    print("No more arrows")
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Getting more arrows...")
                        time.sleep(1)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
        
        elif self._range == "Medium":
            print("The enemy holds steady at mid range. Keep Alert!")
            time.sleep(1.5)
            while True:
                arrows = 12
                temp_list = []
                temp_total_damage = 0
                chance = 0.2
                print("putting an arrow...")
                time.sleep(1)
                while arrows > 0:
                    arrows -=1
                    chance_number = round(random.random(), 2)
                    damage1 = random.randint(60, 80)
                    print("Aiming...")
                    s = pygame.mixer.Sound(BOW_AIMING)
                    s.play()
                    while pygame.mixer.get_busy():
                        time.sleep(0.1)
                    if chance_number > chance:
                        print(f"You have inflicted: {damage1} points of damage.")
                        s = pygame.mixer.Sound(BOW_HIT)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                        s = pygame.mixer.Sound(BOW_MISS)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                    if arrows > 0:
                        print("putting another arrow...")
                        time.sleep(1)
                else:
                    print("No more arrows")
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Getting more arrows...")
                        time.sleep(1)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0

        elif self._range == "High":
            print("The enemy is keeping their distance afar.")
            time.sleep(1.5)
            while True:
                arrows = 12
                temp_list = []
                temp_total_damage = 0
                chance = 0.2
                print("putting an arrow...")
                time.sleep(1)
                while arrows > 0:
                    arrows -=1
                    chance_number = round(random.random(), 2)
                    damage1 = random.randint(80, 100)
                    print("Aiming...")
                    s = pygame.mixer.Sound(BOW_AIMING)
                    s.play()
                    while pygame.mixer.get_busy():
                        time.sleep(0.1)
                    if chance_number > chance:
                        print(f"You have inflicted: {damage1} points of damage.")
                        s = pygame.mixer.Sound(BOW_HIT)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                        temp_list.append(damage1)
                    else:
                        print(f"You have missed.")
                        s = pygame.mixer.Sound(BOW_MISS)
                        s.play()
                        while pygame.mixer.get_busy():
                            time.sleep(0.1)
                    if arrows > 0:
                        print("putting another arrow...")
                        time.sleep(1)
                else:
                    print("No more arrows")
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Getting more arrows...")
                        time.sleep(1)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
    def run(self):
        self.bow_logic()


class RocketLauncher(Weapon):
    def __init__(self, name_weapon, rocket_type):
        super().__init__(name_weapon)
        self._rocket_type = rocket_type

    def rocket_launcher_logic(self):
        if self._rocket_type == "Explosive":
            while True:
                ammo = 3
                temp_list = []
                temp_total_damage = 0
                while ammo > 0:
                    ammo -= 1
                    chance = 0.1
                    chance_number = round(random.random(), 2)
                    damage1 = random.randint(400, 700)
                    damage2 = random.randint(100, 200)
                    if chance_number > chance:
                        print("INCOMING!!!")
                        s = pygame.mixer.Sound(EXPL_LAUNCH)
                        s.play()
                        time.sleep(1.5)
                        print(f"BOOOOOM!!! You dealt {damage1} explosive damage!!")
                        s = pygame.mixer.Sound(EXPLOSION_ROCKET1)
                        s.play()
                        temp_list.append(damage1)
                    else:
                        print(f"You missed your target! But still dealt {damage2} explosive damage!!")
                        temp_list.append(damage2)
                    time.sleep(2)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                    end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                    sys.stdout.write(letter)
                    sys.stdout.flush()
                    time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(ROCKET_RELOAD)
                        s.play()
                        time.sleep(6)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
                    
        elif self._rocket_type == "Nuclear":
            while True:
                ammo = 3
                temp_list = []
                temp_total_damage = 0

                print("⚠ WARNING ⚠ WARNING ⚠ WARNING ⚠")
                s = pygame.mixer.Sound(COUNTDOWN_ROCKETLAUNCHER)
                s.play()
                print(f"Firing {ammo} rockets")
                s = pygame.mixer.Sound(NUCL_LAUNCH)
                s.play()
                time.sleep(5.5)

                while ammo > 0:
                    ammo -= 1
                    crit_chance = round(random.random(), 2)

                    if crit_chance < 0.3:
                        damage1 = random.randint(1000, 3000)
                        print(f"CRITICAL HIT!! You dealt {damage1} nuclear damage!!")
                        s = pygame.mixer.Sound(EXPLOSION_ROCKET2)
                        s.play()
                        temp_list.append(damage1)
                    else:
                        damage1 = random.randint(500, 800)
                        print(f"BOOOOOOOM!!! You dealt {damage1} nuclear damage!!!")
                        s = pygame.mixer.Sound(EXPLOSION_ROCKET2)
                        s.play()
                    time.sleep(4)
                for i in range(len(temp_list)):
                    temp_total_damage += temp_list[i]
                end_text = f"You have inflicted a total of: {temp_total_damage} points of damage.\n"
                for letter in end_text:
                        sys.stdout.write(letter)
                        sys.stdout.flush()
                        time.sleep(0.05)
                temp_inp = str(input("Attack one more?(Y/N): ")).strip().upper()
                while True:
                    if temp_inp == "Y":
                        print("Reloading...")
                        s = pygame.mixer.Sound(ROCKET_RELOAD)
                        s.play()
                        time.sleep(6)
                        break
                    elif temp_inp == "N":
                        print("Exiting...")
                        return 0
                    else:
                        print("Invalid option.")
                        return 0
    def run(self):
        self.rocket_launcher_logic()

def random_weapon():
    x = 3
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
         print("You have been given a Bow and Arrows!")
         option = ["NONE", "Low", "Medium", "High"]
         temp_range = ["Low", "Medium", "High"]
         temp1 = str(input("Choose a name for the bow and arrow: "))
         if temp1 == "":
            print("Enter a valid name.")
            return
         temp2 = random.choice(temp_range)
         bow_temp = Bow(temp1, temp2)
         return bow_temp
    

a = random_weapon()
a.run()
