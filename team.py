import random
from superhero import Superhero
import requests

class Team():
    def __init__(self, team_number):
        self.team_number = team_number
        self.members = []
        self.deaths = []
        self.alignment = ''
        self.api_url = 'https://superheroapi.com/api/2183127771827858/'
        self.members_id = []

    def create_team(self, other_team):
        while True:
            if len(self.members) == 5:
                break
            else:
                id = random.randint(1, 732)
                if id not in self.members_id and id not in other_team.members_id:
                    self.members_id.append(id)
                    # get superhero data from API
                    url = self.api_url + str(id)
                    try:
                        response = requests.get(url, timeout=(0.3, 1.5))
                    except:
                        print('Error al conectar con la API, reintentando...')
                        self.members_id.remove(id)
                        continue
                    data = response.json()                    
                    # create superhero object
                    superhero = Superhero(self)
                    created = superhero.initiate_superhero(data)
                    if created:
                        self.members.append(superhero)
                        print(f'Superheroe creado para equipo {self.team_number}: ' + superhero.name)
                    else:
                        print('Error al crear superheroe, reintentando...')
                        self.members_id.remove(id)
                        continue

    def calculate_stats(self):
        self.define_alignment()
        for member in self.members:
            member.calculate_powerstats()

    def define_alignment(self):
        alignments = []
        for member in self.members:
            alignments.append(member.alignment)
        if alignments.count('good') > alignments.count('bad'):
            self.alignment = 'good'
        else:
            self.alignment = 'bad'

    def manage_turn(self, other_team):
        member = self.get_random_member()
        target = other_team.get_random_member()
        member.attack(target)
        print('\n')
        print(f'HP resultante {target.name}: {target.hp}')
        print('\n')
        input('Presione enter para continuar...')

    def verify_team(self):
        if len(self.members) == 0:
            return True
        else:
            return False

    def introduce_team(self):
        print(f'Equipo {self.team_number}, bando: {self.alignment}')
        for member in self.members:
            print(f'{member.name}:')
            print(f'\tBando: {member.alignment}')
            print(f'\tHP: {member.hp}')
            print(f'\tStamina actual: {member.actual_stamina}')
            print(f'\tCoeficiente de bando: {member.filiation_coefficient}')
        print('\n')
        input('Presione enter para continuar...')
        print('\n')

    def get_random_member(self):
        member = random.choice(self.members)
        if member in self.deaths:
            return self.get_random_member()
        else:
            return member

    def remove_hero(self, hero):
        self.members.remove(hero)
        self.deaths.append(hero)