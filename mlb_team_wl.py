import pybaseball as pb
import pandas as pd

def display_team_game_logs(season, team):
    # Retrieve team game logs
    logs = pb.team_game_logs(season, team)

    # Display the game logs
    for index, row in logs.iterrows():
        game_date = row['Date']
        opponent = row['Opp']
        result = row['Rslt']
        print(f"Date: {game_date} | Opponent: {opponent} | Result: {result}")

    # Summary of win-loss counts
    win_count = logs[logs['Rslt'].str.contains('W')].shape[0]
    loss_count = logs[logs['Rslt'].str.contains('L')].shape[0]
    print(f"\nWin count: {win_count}")
    print(f"Loss count: {loss_count}")

# Prompt user to input the year and team abbreviation
year = input("Enter the year: ")
team = input("Enter the team abbreviation: ")

# Call the function to display the team game logs and win-loss counts
display_team_game_logs(int(year), team)
