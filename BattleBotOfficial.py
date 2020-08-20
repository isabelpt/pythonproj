import random
class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2

    def battle(self):
        while self.bbot1.is_alive() and self.bbot2.is_alive():
            # begin this round
            if self.bbot1.speed <= self.bbot2.speed:
                self.bbot1.action(self.bbot2)
                self.bbot2.action(self.bbot1)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round\n")
            else:
                self.bbot2.action(self.bbot1)
                self.bbot1.action(self.bbot2)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round\n")
        if self.bbot1.is_alive():
            print(self.bbot1.name + " is the winner.")
        else:
            print(self.bbot2.name + " is the winner.")


class BattleBot1:
        def __init__(self, name, color):
            self.name = name
            self.health = 100.0
            self.color = color
            self.armor = 10.0
            self.damage = 10.0
            self.speed = 10.0

        def attack(self, opponent):
            damage_dealt = self.damage - (self.damage * (opponent.armor / 100))
            opponent.take_damage(damage_dealt)

        def take_damage(self, damage_dealt):
            if self.dodge():
                print(self.name + " has dodged the attack.")
                self.health -= 0
                self.armor -= 0
            else:
                self.health -= damage_dealt
                self.armor -= 1

        def defend(self):
            self.armor += 2
            self.damage -= 1
            self.speed -= 1

        def build_attack(self):
            self.damage += 2
            self.speed -= 1
            self.armor -= 1

        def is_alive(self):
            if self.health <= 0:
                return False
            else:
                return True

        def get_stats(self):
            print(self.color + " " + self.name)
            print("Health: " + str(self.health))
            print("Damage: " + str(self.damage))
            print("Armor: " + str(self.armor))
            print("Speed: " + str(self.speed))

        def action(self, opponent):
            chance = random.randint(1, 100)
            if chance <= 20:
                self.attack(opponent)
            elif chance <= 40:
                self.defend()
         #   elif chance <= 50:
             #   self.heavy_attack(opponent)
            elif chance <= 60:
                self.build_attack()
            elif chance <= 65:
                self.full_heal()
            else:
                print(self.name + " glitched out.")

        def dodge(self):
            if self.speed > 10:
                chance_dodge = random.randint(1, 3)
                if chance_dodge == 1 or 2:
                    return True
                else:
                    return False
            elif self.speed <= 10:
                chance_dodge = random.randint(1, 2)
                if chance_dodge == 1:
                    return True
                else:
                    return False

        def full_heal(self):
            self.health = 100
            self.damage -= 1

        def heavy_attack(self, opponent, damage_dealt):
            damage_dealt *= 2
            opponent.take_damage(damage_dealt)
            self.health -= 5


class BattleBot2:
        def __init__(self, name, color):
            self.name = name
            self.color = color
            self.health = 100.0
            self.armor = 10.0
            self.damage = 10.0
            self.speed = 10.0

        def attack(self, opponent):
            # 10.0 - (10.0 * .1)
            damage_dealt = self.damage - (self.damage * (opponent.armor / 100))
            opponent.take_damage(damage_dealt)
            if self.dodge():
                self.health -= 0.0
                self.armor -= 0.0
            else:
                self.health -= damage_dealt
                self.armor -= 1.0
            if self.cant_die():
                self.health += 1000.0
            else:
                self.health += 0.0

        def take_damage(self, damage_dealt):
            if self.dodge():
                print(self.name + " has dodged the attack.")
                self.health -= 0
                self.armor -= 0
            else:
                self.health -= damage_dealt
                self.armor -= 1

        def defend(self):
            self.armor += 2.0
            self.damage -= 1.0
            self.speed -= 1.0

        def build_attack(self):
            self.damage += 2.0
            self.speed -= 1.0
            self.armor -= 1.0

        def is_alive(self):
            if self.health <= 0:
                return False
            else:
                return True

        def dodge(self):
            chance_dodge = random.randint(1, 2)
            if chance_dodge == 1:
                return True
            else:
                return False

        def opponent_kill(self, opponent):
            opponent.health = 0

        def cant_die(self):
            probability = random.randint(1, 9)
            if probability == 1:
                return True
            else:
                return False

        def get_stats(self):
            print(self.color + " " + self.name)
            print("Health: " + str(self.health))
            print("Damage: " + str(self.damage))
            print("Armor: " + str(self.armor))
            print("Speed: " + str(self.speed))

        def action(self, opponent):
            likelihood = random.randint(1, 100)
            if likelihood <= 20:
                self.attack(opponent)
            elif likelihood <= 40:
                self.defend()
            elif likelihood <= 60:
                self.build_attack()
            elif likelihood <= 70:
                self.opponent_kill(opponent)
            else:
                print(self.name + " glitched out.")


Bot1 = BattleBot1("Shaun", "Blue")
Bot2 = BattleBot2("Izzy", "Purple")
Arena = Arena(Bot1, Bot2)
Arena.battle()