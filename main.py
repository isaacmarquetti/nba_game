import random
from datetime import timedelta
from time import sleep

from classes import TeamWarriors, TeamCeltics, Game, Team

team_a = Team("Golden State Warriors", "GSW")
team_b = Team("Boston Celtics", "BOS")

team_a2 = TeamWarriors("Golden State Warriors")
team_b2 = TeamCeltics("Boston Celtics")

game = Game()
side = 0
quarter = 1

while quarter <= 5:
    if quarter == 1:
        game.screen_title()
        game.screen_options_1()
        game.screen_options_2_3()
    if quarter == 5:
        game.screen_title()
        print(f"|| FINAL DE PARTIDA || {team_a.team_abr:>5} {team_a.point_team()} x {team_b.point_team()} {team_b.team_abr}")
        print()
        game.screen_options_2_3()
    if 1 < quarter < 5:
        game.screen_title()
        print(f"|| FINAL DO {quarter-1}ºP || {team_a.team_abr:>5} {team_a.point_team()} x {team_b.point_team()} {team_b.team_abr}")
        print()
        print(f"[1] Próximo período ({quarter}ºP)")
        game.screen_options_2_3()
    opcao = input("Digite sua opção: ")
    if opcao == "1" and quarter != 5:
        print()
        print(f"{'#' * 19} {quarter}º PERIODO {'#' * 19}")
        time_delta = timedelta(minutes=12)
        while time_delta > timedelta(seconds=0):
            discount = random.randint(15, 22)
            print(f"{'+'}{'-' * 48}{'+'}")
            print(f"{'||':>6}{quarter:>4}P {game.clock(time_delta):^10}{'||'}", end=" ")
            print(f"{team_a.team_abr:>5} {team_a.point_team()} x {team_b.point_team()} {team_b.team_abr}")
            print(f"{'+'}{'-' * 48}{'+'}")
            time_delta -= timedelta(seconds=discount)
            sleep(2)
            if side == 0:
                team_a.ball()
                sleep(2)
                attempt = team_a2.points(random.randint(1, 10))
                if attempt == 0:
                    name_reb = team_b2.skill_rebound_player()
                    total_rebounds = team_b2.rebound_player(name_reb)
                    print(f"{name_reb} (TOTAL: {total_rebounds} reb)")
                    side = 1
                if attempt == 2:
                    name_pts = team_a2.skill_2pts_player()
                    while True:
                        name_ast = team_a2.skill_assists_player()
                        if name_pts != name_ast:
                            break
                    total_points = team_a2.point_player(name_pts, attempt)
                    total_assists = team_a2.assist_player(name_ast)
                    if name_ast == "":
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)")
                    else:
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)", end=" ")
                        print(f"Assist by {name_ast} (TOTAL: {total_assists} ast)")
                    team_a.point += 2
                    side = 1
                if attempt == 3:
                    name_pts = team_a2.skill_3pts_player()
                    while True:
                        name_ast = team_a2.skill_assists_player()
                        if name_pts != name_ast:
                            break
                    total_points = team_a2.point_player(name_pts, attempt)
                    total_assists = team_a2.assist_player(name_ast)
                    if name_ast == "":
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)")
                    else:
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)", end=" ")
                        print(f"Assist by {name_ast} (TOTAL: {total_assists} ast)")
                    team_a.point += 3
                    side = 1
            else:
                team_b.ball()
                sleep(2)
                attempt = team_b2.points(random.randint(1, 10))
                if attempt == 0:
                    name_reb = team_a2.skill_rebound_player()
                    total_rebounds = team_a2.rebound_player(name_reb)
                    print(f"{name_reb} (TOTAL: {total_rebounds} reb)")
                    side = 0
                if attempt == 2:
                    name_pts = team_b2.skill_2pts_player()
                    while True:
                        name_ast = team_b2.skill_assists_player()
                        if name_pts != name_ast:
                            break
                    total_points = team_b2.point_player(name_pts, attempt)
                    total_assists = team_b2.assist_player(name_ast)
                    if name_ast == "":
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)")
                    else:
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)", end=" ")
                        print(f"Assist by {name_ast} (TOTAL: {total_assists} ast)")
                    team_b.point += 2
                    side = 0
                if attempt == 3:
                    name_pts = team_b2.skill_3pts_player()
                    while True:
                        name_ast = team_b2.skill_assists_player()
                        if name_pts != name_ast:
                            break
                    total_points = team_b2.point_player(name_pts, attempt)
                    total_assists = team_b2.assist_player(name_ast)
                    if name_ast == "":
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)")
                    else:
                        print(f"{name_pts} {attempt}pts (TOTAL: {total_points} pts)", end=" ")
                        print(f"Assist by {name_ast} (TOTAL: {total_assists} ast)")
                    team_b.point += 3
                    side = 0
        quarter += 1
    if opcao == "2":
        print(f"{'+'}{'-' * 38}{'+'}")
        print(f"{'|'}{team_a.team:^38}{'|'}")
        print(f"{'+'}{'-' * 38}{'+'}")
        print(f"|{'PLAYERS':^20}{'|'}{'PTS':^5}{'|'}{'REB':^5}{'|'}{'AST':^5}{'|'}")
        print(f"|{team_a2.player_1[0][0]:^20}{'|'}{team_a2.player_1[1][0]:^5}{'|'}{team_a2.player_1[1][1]:^5}{'|'}{team_a2.player_1[1][2]:^5}{'|'}")
        print(f"|{team_a2.player_2[0][0]:^20}{'|'}{team_a2.player_2[1][0]:^5}{'|'}{team_a2.player_2[1][1]:^5}{'|'}{team_a2.player_2[1][2]:^5}{'|'}")
        print(f"|{team_a2.player_3[0][0]:^20}{'|'}{team_a2.player_3[1][0]:^5}{'|'}{team_a2.player_3[1][1]:^5}{'|'}{team_a2.player_3[1][2]:^5}{'|'}")
        print(f"|{team_a2.player_4[0][0]:^20}{'|'}{team_a2.player_4[1][0]:^5}{'|'}{team_a2.player_4[1][1]:^5}{'|'}{team_a2.player_4[1][2]:^5}{'|'}")
        print(f"|{team_a2.player_5[0][0]:^20}{'|'}{team_a2.player_5[1][0]:^5}{'|'}{team_a2.player_5[1][1]:^5}{'|'}{team_a2.player_5[1][2]:^5}{'|'}")
        print(f"{'+'}{'-' * 38}{'+'}")
        print(f"{'+'}{'-' * 38}{'+'}")
        print(f"{'|'}{team_b.team:^38}{'|'}")
        print(f"{'+'}{'-' * 38}{'+'}")
        print(f"|{'PLAYERS':^20}{'|'}{'PTS':^5}{'|'}{'REB':^5}{'|'}{'AST':^5}{'|'}")
        print(f"|{team_b2.player_1[0][0]:^20}{'|'}{team_b2.player_1[1][0]:^5}{'|'}{team_b2.player_1[1][1]:^5}{'|'}{team_b2.player_1[1][2]:^5}{'|'}")
        print(f"|{team_b2.player_2[0][0]:^20}{'|'}{team_b2.player_2[1][0]:^5}{'|'}{team_b2.player_2[1][1]:^5}{'|'}{team_b2.player_2[1][2]:^5}{'|'}")
        print(f"|{team_b2.player_3[0][0]:^20}{'|'}{team_b2.player_3[1][0]:^5}{'|'}{team_b2.player_3[1][1]:^5}{'|'}{team_b2.player_3[1][2]:^5}{'|'}")
        print(f"|{team_b2.player_4[0][0]:^20}{'|'}{team_b2.player_4[1][0]:^5}{'|'}{team_b2.player_4[1][1]:^5}{'|'}{team_b2.player_4[1][2]:^5}{'|'}")
        print(f"|{team_b2.player_5[0][0]:^20}{'|'}{team_b2.player_5[1][0]:^5}{'|'}{team_b2.player_5[1][1]:^5}{'|'}{team_b2.player_5[1][2]:^5}{'|'}")
        print(f"{'+'}{'-' * 38}{'+'}")
    if opcao == "3":
        break

