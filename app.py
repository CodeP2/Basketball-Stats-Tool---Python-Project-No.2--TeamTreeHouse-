import constants
from copy import deepcopy
import sys

players_copy = deepcopy(constants.PLAYERS)
teams_copy = deepcopy(constants.TEAMS)


def clean_data():
    for player in players_copy:
        if player['experience'] == "YES":
            player['experience'] = True
        if player['experience'] == "NO":
            player['experience'] = False
        height = player['height'].split()
        player['height'] = int(height[0])
        guard = player['guardians'].split(' and ')
        player['guardians'] = (', '.join(guard))


def balance_teams():
    for index, exp in enumerate(players_copy):
        if exp['experience'] is True and index <= 6:
            Panthers.append(exp)
            Panthers_exp.append(exp)
    for index, inexp in enumerate(players_copy):
        if inexp['experience'] is False and 1 <= index <= 3:
            Panthers.append(inexp)
            Panthers_inexp.append(inexp)
    for index, exp in enumerate(players_copy):
        if exp['experience'] is True and 7 <= index <= 10:
            Bandits.append(exp)
            Bandits_exp.append(exp)
    for index, inexp in enumerate(players_copy):
        if inexp['experience'] is False and 5 <= index <= 11:
            Bandits.append(inexp)
            Bandits_inexp.append(inexp)
    for index, exp in enumerate(players_copy):
        if exp['experience'] is True and 12 <= index <= 16:
            Warriors.append(exp)
            Warriors_exp.append(exp)
    for index, inexp in enumerate(players_copy):
        if inexp['experience'] is False and 13 <= index <= 17:
            Warriors.append(inexp)
            Warriors_inexp.append(inexp)


if __name__ == "__main__":
    clean_data()
    while True:
        print('BASKETBALL TEAM STATS TOOL \n\n---- MENU----\n\n')
        print('Here are your choices:\nA)Display Team Stats\nB)Quit')
        choice = input("\n\nEnter an option:")
        if choice.lower() == "b":
            sys.exit(0)
        elif choice.lower() == "a":
            print('A)Panthers\nB)Bandits\nC)Warriors')
            teams = ['Panthers', 'Bandits', 'Warriors']
            Panthers = []
            Bandits = []
            Warriors = []
            Panthers_exp = []
            Panthers_inexp = []
            Bandits_exp = []
            Bandits_inexp = []
            Warriors_exp = []
            Warriors_inexp = []
            Panthers_name = []
            Bandits_name = []
            Warriors_name = []
            Panthers_guardians = []
            Bandits_guardians = []
            Warriors_guardians = []
            balance_teams()
            team_choice = input('\n\nEnter an option:')
            if team_choice.lower() == "a":
                print("Team: Panthers Stats\n--------------------")
                print(f'Total Players: {len(Panthers)}')
                print(f'Total experienced: {len(Panthers_exp)}')
                print(f'Total inexperienced: {len(Panthers_inexp)}')
                sums = 0
                Panthers_height = []
                for Pan_hei in Panthers:
                    sums += Pan_hei['height']
                    Panthers_height.append(sums)
                Pan_avg_hei = max(Panthers_height) / len(Panthers)
                print(f'Average height: {Pan_avg_hei}')
                for names in Panthers:
                    Panthers_name.append(names['name'])
                print('Players on Team:')
                print(', '.join(Panthers_name))
                for guardians in Panthers:
                    Panthers_guardians.append(guardians['guardians'])
                print('Guardians:')
                print(', '.join(Panthers_guardians))
            if team_choice.lower() == "b":
                print("Team: Bandits Stats\n--------------------")
                print(f'Total Players: {len(Bandits)}')
                print(f'Total experienced: {len(Bandits_exp)}')
                print(f'Total inexperienced: {len(Bandits_inexp)}')
                sums = 0
                Bandits_height = []
                for ban_hei in Bandits:
                    sums += ban_hei['height']
                    Bandits_height.append(sums)
                Ban_avg_hei = max(Bandits_height) / len(Bandits)
                print(f'Average height: {Ban_avg_hei}')
                for names in Bandits:
                    Bandits_name.append(names['name'])
                print('Players on Team:')
                print(', '.join(Bandits_name))
                for guardians in Bandits:
                    Bandits_guardians.append(guardians['guardians'])
                print('Guardians:')
                print(', '.join(Bandits_guardians))
            if team_choice.lower() == "c":
                print("Team: Warriors Stats\n--------------------")
                print(f'Total Players: {len(Warriors)}')
                print(f'Total experienced: {len(Warriors_exp)}')
                print(f'Total inexperienced: {len(Warriors_inexp)}')
                sums = 0
                Warriors_height = []
                for War_hei in Warriors:
                    sums += War_hei['height']
                    Warriors_height.append(sums)
                War_avg_hei = max(Warriors_height) / len(Warriors)
                print(f'Average height: {War_avg_hei}')
                for names in Warriors:
                    Warriors_name.append(names['name'])
                print('Players on Team:')
                print(', '.join(Warriors_name))
                for guardians in Warriors:
                    Warriors_guardians.append(guardians['guardians'])
                print('Guardians:')
                print(', '.join(Warriors_guardians))
            input("Press ENTER to continue...")
