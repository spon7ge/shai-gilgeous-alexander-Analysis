#libaries Ill be using for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import seaborn as sns
#NBA_API
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo, shotchartdetail, teamgamelog, boxscoreadvancedv2, leaguedashplayerstats, leaguedashteamstats
from nba_api.stats.static import *

#Basketball Reference API
from basketball_reference_web_scraper import client

from matplotlib.patches import Circle, Rectangle, Arc

#Basic stats
def calculate_per_game_totals(totals):
    per_game_stats = {
        'PPG': (totals['PTS'].values[0] / totals['GP'].values[0]).round(2),
        'RPG': (totals['REB'].values[0] / totals['GP'].values[0]).round(2),
        'APG': (totals['AST'].values[0] / totals['GP'].values[0]).round(2),
        'SPG': (totals['STL'].values[0] / totals['GP'].values[0]).round(2),
        'BPG': (totals['BLK'].values[0] / totals['GP'].values[0]).round(2),
        'MPG': (totals['MIN'].values[0] / totals['GP'].values[0]).round(2),
        'FT%': totals['FT_PCT'].values[0],
        'FG%': totals['FG_PCT'].values[0],
        '3FG%': totals['FG3_PCT'].values[0],
        'GP': totals['GP'].values[0]
    }
    return per_game_stats

#player career stats
def get_players_stats(player_id, season):
    data = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    season_stats = data.loc[data['SEASON_ID'] == season]
    per_game_totals = calculate_per_game_totals(season_stats)
    return per_game_totals
# get_players_stats(player_id=1628983, season='2019-20')

#Adv stats
def get_adv_br_metrics(data):
    per_game_adv_stats = {
        'player_efficiency_rating': data['player_efficiency_rating'].values[0],
        'true_shooting_percentage': data['true_shooting_percentage'].values[0],
        'win_shares': data['win_shares'].values[0],
        'offensive_box_plus_minus': data['offensive_box_plus_minus'].values[0],
        'defensive_box_plus_minus': data['defensive_box_plus_minus'].values[0],
        'box_plus_minus': data['box_plus_minus'].values[0],
    }
    return per_game_adv_stats

def get_adv_nba_metrics(data):
    data = {
        'EFG_PCT': data['EFG_PCT'].values[0],
        'TS_PCT': data['TS_PCT'].values[0],
        'OFF_RATING': data['OFF_RATING'].values[0],
        'DEF_RATING': data['DEF_RATING'].values[0],
        'NET_RATING': data['NET_RATING'].values[0],
        'USG_PCT': data['USG_PCT'].values[0],
        'PIE': data['PIE'].values[0],
        'EFG_PCT_RANK': data['EFG_PCT_RANK'].values[0],
        'USG_PCT_RANK': data['USG_PCT_RANK'].values[0],
        'TS_PCT_RANK': data['TS_PCT_RANK'].values[0],
        'PIE_RANK': data['PIE_RANK'].values[0],        
    }
    return data

#combined the adv metrics into one 
def combine_adv_stats(data1, data2):
    combined_data = data1.copy()  # Start with the first dictionary's data
    for key, value in data2.items():
        if key in combined_data:
            # If the key exists in both dictionaries, decide how to handle it
            # Here, we'll just take the average of the values as an example
            combined_data[key] = (combined_data[key] + value) / 2
        else:
            combined_data[key] = value  # Add new key-value pairs from data2
    
    return combined_data

#insert end year for basketball reference api ex. 2018-19 use 2019
def basketball_reference_adv_data(year):
    df = pd.DataFrame(client.players_advanced_season_totals(season_end_year=year))
    adv_df = df.loc[df['name'] == 'Shai Gilgeous-Alexander'].copy()
    adv_df = get_adv_br_metrics(adv_df)
    return adv_df

#insert player id and year ex. player_id=1628983,year='2018-19'
def nba_api_adv_data(year,player_id):
    advanced_df = leaguedashplayerstats.LeagueDashPlayerStats(
    season=year,
    per_mode_detailed='PerGame',
    measure_type_detailed_defense='Advanced'
    ).get_data_frames()[0]
    advanced_df = advanced_df[advanced_df['PLAYER_ID'] == player_id]
    data = get_adv_nba_metrics(advanced_df)
    return data

def league_BR_stats(year):
    df = pd.DataFrame(client.players_advanced_season_totals(season_end_year=year))
    array = ['player_efficiency_rating','true_shooting_percentage','win_shares','offensive_box_plus_minus','defensive_box_plus_minus','box_plus_minus']
    print(f"The Leagues Advance Metrics Averages\n")
    for i in array:
        print(f"{i}: {df[i].mean().round(2)}")

def get_BR_avgs(data):
    array = ['player_efficiency_rating','true_shooting_percentage','win_shares','offensive_box_plus_minus','defensive_box_plus_minus','box_plus_minus']
    print(f"Shai Gilgeous-Alexander Averages\n")
    for i in array:
        print(f"{i}: {data[i]}")

def get_shot_chart(player_id,year):
    data = shotchartdetail.ShotChartDetail(
    team_id=0, 
    player_id=player_id,
    season_type_all_star='Regular Season',
    season_nullable=year,
    context_measure_simple="FGA"
    ).get_data_frames()[0]
    return data

#function that draws the basketball court
def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax