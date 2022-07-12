import random

class Superhero():
    def __init__(self, team):
        self.name = ''
        self.alignment = ''

        self.intelligence = 0
        self.strength = 0
        self.speed = 0
        self.durability = 0
        self.power = 0
        self.combat = 0
        self.hp = 0

        self.actual_stamina = 0
        self.filiation_coefficient = 0
        self.team = team
        self.alive = True

    def initiate_superhero(self, data):
        self.name = data['name']
        self.intelligence = data['powerstats']['intelligence']
        self.strength = data['powerstats']['strength']
        self.speed = data['powerstats']['speed']
        self.durability = data['powerstats']['durability']
        self.power = data['powerstats']['power']
        self.combat = data['powerstats']['combat']
        self.actual_stamina = random.random() * 10
        self.alignment = data['biography']['alignment']
        return self.verify_powerstats()

    def verify_powerstats(self):
        if (self.intelligence != 'null' and self.strength != 'null' and self.speed != 'null' 
                and self.durability != 'null' and self.power != 'null' and self.combat != 'null'
                and self.alignment != 'null'):
            return True

    def calculate_powerstats(self):
        self.calculate_fb()
        self.intelligence = self.calculate_stat(self.intelligence)
        self.strength = self.calculate_stat(self.strength)
        self.speed = self.calculate_stat(self.speed)
        self.durability = self.calculate_stat(self.durability)
        self.power = self.calculate_stat(self.power)
        self.combat = self.calculate_stat(self.combat)
        self.calculate_hp()

    def calculate_stat(self, stat):
        stat = int(((2 * float(stat) + float(self.actual_stamina)) / 1.1) * float(self.filiation_coefficient))
        return stat

    def calculate_fb(self):
        if self.alignment == self.team.alignment:
            self.filiation_coefficient = (1 + random.random() * 9)
        else:
            self.filiation_coefficient = ((1 + random.random() * 9) ** -1)

    def calculate_hp(self):
        self.hp = int(((0.8 * self.strength + 0.7 * self.durability + self.power) / 2) * (1 + self.actual_stamina / 10) + 100)

    def attack(self, target):
        attack = random.randint(1, 3)
        if attack == 1:
            self.attack_mental(target)
        elif attack == 2:
            self.attack_strong(target)
        elif attack == 3:
            self.attack_speed(target)
        else:
            print('Error')

    def attack_mental(self, target):
        print(f'{self.name} ataca mentalmente a {target.name} (HP: {target.hp})')
        attack = round((self.intelligence * 0.7 + self.speed * 0.2 + self.combat * 0.1) * self.filiation_coefficient, 2)
        print(f'Puntos de ataque mental: {attack}')
        target.receive_damage(attack)

    def attack_strong(self, target):
        print(f'{self.name} ataca fuertemente a {target.name} (HP: {target.hp})')
        attack = round((self.strength * 0.6 + self.power * 0.2 + self.combat * 0.2) * self.filiation_coefficient, 2)
        print(f'Puntos de ataque fuerte: {attack}')
        target.receive_damage(attack)

    def attack_speed(self, target):
        print(f'{self.name} ataca a {target.name} (HP: {target.hp}) con velocidad')
        attack = round((self.speed * 0.55 + self.durability * 0.25 + self.strength * 0.2) * self.filiation_coefficient, 2)
        print(f'Puntos de ataque de velocidad: {attack}')
        target.receive_damage(attack)

    def receive_damage(self, attack_points):
        self.hp -= attack_points
        if self.hp <= 0:
            self.alive = False
            self.hp = 0
            print(f'{self.name} ha muerto')
            self.team.remove_hero(self)