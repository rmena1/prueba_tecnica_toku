from team import Team

class Combat():
    def __init__(self):
        self.team1 = ''
        self.team2 = ''
        self.current_turn = 'Equipo 1'

    def create_team(self):
        print('\n')
        self.team1 = Team(1)
        self.team2 = Team(2)
        self.team1.create_team(self.team2)
        print('\n')
        self.team2.create_team(self.team1)
        print('\n')
        print('Equipos creados correctamente\n')

    def manage_turns(self):
        while True:
            print('Turno de ' + self.current_turn + '\n')
            if self.current_turn == 'Equipo 1':
                self.team1.manage_turn(self.team2)
                self.current_turn = 'Equipo 2'
            else:
                self.team2.manage_turn(self.team1)
                self.current_turn = 'Equipo 1'
            print('\n')
            if self.team1.verify_team():
                print('Pelea terminada \n')
                print('Equipo 1 ha perdido\n')
                input('Presione enter para continuar...')
                print('\n')
                print('Equipo 2 ha ganado!!!\n')
                self.print_survivors()
                break
            elif self.team2.verify_team():
                print('Pelea terminada \n')
                print('Equipo 2 ha perdido\n')
                input('Presione enter para continuar...')
                print('\n')
                print('Equipo 1 ha ganado!!!\n')
                self.print_survivors()
                break

    def print_survivors(self):
        for team in [self.team1, self.team2]:
            for member in team.members:
                if member.hp > 0:
                    print(f'{member.name} ha sobrevivido!')

    def start_fight(self):
        print('Creando equipos, superheroes y calculando stats...')
        self.create_team()
        self.team1.calculate_stats()
        self.team2.calculate_stats()
        print('Stats calculados correctamente \n')
        input('Presione enter para continuar...')
        print('\n')
        self.team1.introduce_team()
        self.team2.introduce_team()
        print('Comenzando pelea...')
        print('\n')
        self.manage_turns()
        