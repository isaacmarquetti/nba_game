import random


class Team:
    point = 0

    def __init__(self, team, team_abr):
        self.team = team
        self.team_abr = team_abr

    def ball(self):
        modes = [f"Bola com o time dos {self.team}",
                 f"{self.team} no ataque",
                 f"Avança os {self.team}",
                 f"Quem ataca é o {self.team}",
                 f"Trabalha a bola no ataque os {self.team}"]
        print(random.choice(modes))

    def point_team(self):
        return self.point


class Game:
    @staticmethod
    def clock(delta):
        minutos, segundos = divmod(delta.total_seconds(), 60)
        return f'{minutos:02n}:{segundos:02n}'

    @staticmethod
    def screen_title():
        print()
        print(f"{'+'}{'-' * 48}{'+'}")
        print(f"{'|'}{'SIMULADOR DE JOGO DA NBA':^48}{'|'}")
        print(f"{'+'}{'-' * 48}{'+'}")
        print()

    @staticmethod
    def screen_options_1():
        print()
        print("[1] Começar Jogo")

    @staticmethod
    def screen_options_2_3():
        print("[2] Stats")
        print("[3] Sair")
        print()


class TeamWarriors:
    """
    [2pts, 3pts, Reb, Assist][Pts, Reb, Assist]
    """
    player_1 = ["Stephen Curry", 4, 5, 5, 6], [0, 0, 0]
    player_2 = ["Andrew Wiggins", 5, 2, 3, 2], [0, 0, 0]
    player_3 = ["Klay Thompson", 3, 4, 4, 3], [0, 0, 0]
    player_4 = ["Draymond Green", 2, 1, 7, 7], [0, 0, 0]
    player_5 = ["Kevon Looney", 2, 0, 5, 2], [0, 0, 0]

    def __init__(self, name_team):
        self.name_team = name_team

    def skill_2pts_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][1] + \
                 [self.player_2[0][0]] * self.player_2[0][1] + \
                 [self.player_3[0][0]] * self.player_3[0][1] + \
                 [self.player_4[0][0]] * self.player_4[0][1] + \
                 [self.player_5[0][0]] * self.player_5[0][1]
        return random.choice(player)

    def skill_3pts_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][2] + \
                 [self.player_2[0][0]] * self.player_2[0][2] + \
                 [self.player_3[0][0]] * self.player_3[0][2] + \
                 [self.player_4[0][0]] * self.player_4[0][2] + \
                 [self.player_5[0][0]] * self.player_5[0][2]

        return random.choice(player)

    def skill_rebound_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][3] + \
                 [self.player_2[0][0]] * self.player_2[0][3] + \
                 [self.player_3[0][0]] * self.player_3[0][3] + \
                 [self.player_4[0][0]] * self.player_4[0][3] + \
                 [self.player_5[0][0]] * self.player_5[0][3]
        return random.choice(player)

    def skill_assists_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][4] + \
                 [self.player_2[0][0]] * self.player_2[0][4] + \
                 [self.player_3[0][0]] * self.player_3[0][4] + \
                 [self.player_4[0][0]] * self.player_4[0][4] + \
                 [self.player_5[0][0]] * self.player_5[0][4] + \
                 [""] * 14
        return random.choice(player)

    def point_player(self, nome, pts):
        if nome == self.player_1[0][0]:
            self.player_1[1][0] += pts
            return self.player_1[1][0]
        if nome == self.player_2[0][0]:
            self.player_2[1][0] += pts
            return self.player_2[1][0]
        if nome == self.player_3[0][0]:
            self.player_3[1][0] += pts
            return self.player_3[1][0]
        if nome == self.player_4[0][0]:
            self.player_4[1][0] += pts
            return self.player_4[1][0]
        if nome == self.player_5[0][0]:
            self.player_5[1][0] += pts
            return self.player_5[1][0]

    def rebound_player(self, nome):
        if nome == self.player_1[0][0]:
            self.player_1[1][1] += 1
            return self.player_1[1][1]
        if nome == self.player_2[0][0]:
            self.player_2[1][1] += 1
            return self.player_2[1][1]
        if nome == self.player_3[0][0]:
            self.player_3[1][1] += 1
            return self.player_3[1][1]
        if nome == self.player_4[0][0]:
            self.player_4[1][1] += 1
            return self.player_4[1][1]
        if nome == self.player_5[0][0]:
            self.player_5[1][1] += 1
            return self.player_5[1][1]

    def assist_player(self, nome):
        if nome == self.player_1[0][0]:
            self.player_1[1][2] += 1
            return self.player_1[1][2]
        if nome == self.player_2[0][0]:
            self.player_2[1][2] += 1
            return self.player_2[1][2]
        if nome == self.player_3[0][0]:
            self.player_3[1][2] += 1
            return self.player_3[1][2]
        if nome == self.player_4[0][0]:
            self.player_4[1][2] += 1
            return self.player_4[1][2]
        if nome == self.player_5[0][0]:
            self.player_5[1][2] += 1
            return self.player_5[1][2]

    def points(self, n):
        if n <= 5:
            modes = ["Errou!",
                     "Nada feito! Bola com a defesa",
                     "Não converte a tentativa",
                     "Erra a tentativa"]
            print(random.choice(modes))
            return 0
        if 6 <= n <= 8:
            modes = [f"Ponto para o time {self.name_team}",
                     f"Converte o {self.name_team}",
                     f"Cesta para o {self.name_team}",
                     f"Anota uma cesta para o {self.name_team}",
                     f"Infiltra e converte para o {self.name_team}"]
            print(random.choice(modes))
            return 2
        if 9 <= n <= 10:
            modes = [f"Converte uma linda bola de 3 pontos o {self.name_team}",
                     f"De longe, cesta de 3 pontos para o {self.name_team}",
                     f"Cesta de 3 para o {self.name_team}",
                     f"Anota uma cesta, mais 3 pontos para o {self.name_team}"]
            print(random.choice(modes))
            return 3


class TeamCeltics:
    """
    [2pts, 3pts, Reb, Assist][Pts, Reb, Assist]
    """
    player_1 = ["Marcus Smart", 3, 2, 3, 6], [0, 0, 0]
    player_2 = ["Jaylen Brown", 6, 3, 5, 3], [0, 0, 0]
    player_3 = ["Jayson Tatum", 6, 3, 7, 4], [0, 0, 0]
    player_4 = ["Al Horford", 4, 1, 6, 3], [0, 0, 0]
    player_5 = ["Robert Williams", 4, 0, 6, 2], [0, 0, 0]

    def __init__(self, name_team):
        self.name_team = name_team

    def skill_2pts_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][1] + \
                 [self.player_2[0][0]] * self.player_2[0][1] + \
                 [self.player_3[0][0]] * self.player_3[0][1] + \
                 [self.player_4[0][0]] * self.player_4[0][1] + \
                 [self.player_5[0][0]] * self.player_5[0][1]
        return random.choice(player)

    def skill_3pts_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][2] + \
                 [self.player_2[0][0]] * self.player_2[0][2] + \
                 [self.player_3[0][0]] * self.player_3[0][2] + \
                 [self.player_4[0][0]] * self.player_4[0][2] + \
                 [self.player_5[0][0]] * self.player_5[0][2]

        return random.choice(player)

    def skill_rebound_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][3] + \
                 [self.player_2[0][0]] * self.player_2[0][3] + \
                 [self.player_3[0][0]] * self.player_3[0][3] + \
                 [self.player_4[0][0]] * self.player_4[0][3] + \
                 [self.player_5[0][0]] * self.player_5[0][3]
        return random.choice(player)

    def skill_assists_player(self):
        player = [self.player_1[0][0]] * self.player_1[0][4] + \
                 [self.player_2[0][0]] * self.player_2[0][4] + \
                 [self.player_3[0][0]] * self.player_3[0][4] + \
                 [self.player_4[0][0]] * self.player_4[0][4] + \
                 [self.player_5[0][0]] * self.player_5[0][4] + \
                 [""] * 14
        return random.choice(player)

    def point_player(self, nome, pts):
        if nome == self.player_1[0][0]:
            self.player_1[1][0] += pts
            return self.player_1[1][0]
        if nome == self.player_2[0][0]:
            self.player_2[1][0] += pts
            return self.player_2[1][0]
        if nome == self.player_3[0][0]:
            self.player_3[1][0] += pts
            return self.player_3[1][0]
        if nome == self.player_4[0][0]:
            self.player_4[1][0] += pts
            return self.player_4[1][0]
        if nome == self.player_5[0][0]:
            self.player_5[1][0] += pts
            return self.player_5[1][0]

    def rebound_player(self, nome):
        if nome == self.player_1[0][0]:
            self.player_1[1][1] += 1
            return self.player_1[1][1]
        if nome == self.player_2[0][0]:
            self.player_2[1][1] += 1
            return self.player_2[1][1]
        if nome == self.player_3[0][0]:
            self.player_3[1][1] += 1
            return self.player_3[1][1]
        if nome == self.player_4[0][0]:
            self.player_4[1][1] += 1
            return self.player_4[1][1]
        if nome == self.player_5[0][0]:
            self.player_5[1][1] += 1
            return self.player_5[1][1]

    def assist_player(self, nome):
        if nome == self.player_1[0][0]:
            self.player_1[1][2] += 1
            return self.player_1[1][2]
        if nome == self.player_2[0][0]:
            self.player_2[1][2] += 1
            return self.player_2[1][2]
        if nome == self.player_3[0][0]:
            self.player_3[1][2] += 1
            return self.player_3[1][2]
        if nome == self.player_4[0][0]:
            self.player_4[1][2] += 1
            return self.player_4[1][2]
        if nome == self.player_5[0][0]:
            self.player_5[1][2] += 1
            return self.player_5[1][2]

    def points(self, n):
        if n <= 5:
            modes = ["Errou!",
                     "Nada feito! Bola com a defesa",
                     "Não converte a tentativa",
                     "Erra a tentativa"]
            print(random.choice(modes))
            return 0
        if 6 <= n <= 8:
            modes = [f"Ponto para o time {self.name_team}",
                     f"Converte o {self.name_team}",
                     f"Cesta para o {self.name_team}",
                     f"Anota uma cesta para o {self.name_team}",
                     f"Infiltra e converte para o {self.name_team}"]
            print(random.choice(modes))
            return 2
        if 9 <= n <= 10:
            modes = [f"Converte uma linda bola de 3 pontos o {self.name_team}",
                     f"De longe, cesta de 3 pontos para o {self.name_team}",
                     f"Cesta de 3 para o {self.name_team}",
                     f"Anota uma cesta, mais 3 pontos para o {self.name_team}"]
            print(random.choice(modes))
            return 3