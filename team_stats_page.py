# %%
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import time

# %%
def team_scrape(url, dict_stats_by_team, dict_ranks_by_team, dict_coaches_by_team, dict_stats_by_team_in_games, year):
    get_scheme = 100000
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    top_info = soup.find('div', class_="teams")
    team = top_info.h1.find_all('span')[1]
    for p in top_info.find_all('p'):
        try:
            if 'coach' in p.a['href']:
                head_coach = p.a.text
                offensive_coord = head_coach
                defensive_coord = head_coach    
                off_scheme = 'Various'
                def_scheme = 'Various'            
                break
        except:
            if 'Coach:' in info.text:
                head_coach = info.text.split('\n')[1].strip('Coach:\n')
                offensive_coord = head_coach
                defensive_coord = head_coach
                off_scheme = 'Various'
                def_scheme = 'Various'
                break
            continue
    for i, info in enumerate(top_info.find_all('p')):
        try:
            if 'Offensive Coordinator' in info.strong.text:
                offensive_coord = info.text.split(': ')[1]
        except:
            continue         
        try:
            if 'Defensive Coordinator' in info.strong.text:
                defensive_coord = info.text.split(': ')[1]
        except:
            continue        
        if 'Offensive Scheme' in info.text:
            get_scheme = i
            off_scheme = info.text.split(': ')[1]
        if i == get_scheme + 1:
            def_scheme = info.text.split(': ')[1]
    team_stats = soup.find('div', class_="table_wrapper")
    table = team_stats.find('tbody').find_all('tr')
    for i, info in enumerate(table):
        if i == 0:
            # Team Stats
            t_stats = info.find_all('td', class_='right')
            #print(t_stats)
            points_forced = int(t_stats[0].text)
            yds_forced = int(t_stats[1].text)
            offensive_plays = int(t_stats[2].text)
            yds_per_play_forced = float(t_stats[3].text)
            tunovers_lost = int(t_stats[4].text)
            fumbles_lost = int(t_stats[5].text)
            first_downs_forced = int(t_stats[6].text)
            completions_forced = int(t_stats[7].text)
            pass_attempts_forced = int(t_stats[8].text)
            pass_yds_forced = int(t_stats[9].text)
            pass_td_forced = int(t_stats[10].text)
            interceptions_thrown = int(t_stats[11].text)
            yds_per_pass = float(t_stats[12].text)
            first_downs_forced_pass = int(t_stats[13].text)
            rush_attempts_forced = int(t_stats[14].text)
            rush_yds_forced = int(t_stats[15].text)
            rush_td_forced = int(t_stats[16].text)
            yds_per_run = float(t_stats[17].text)
            first_downs_forced_run = int(t_stats[18].text)
            penalties_against_team = int(t_stats[19].text)
            penalty_yds_against_team  = int(t_stats[20].text)
            penalty_firstdowns_against_team  = int(t_stats[21].text)
            total_drives_for_team  = int(t_stats[22].text)
            pct_scoring_drives_for_team  = float(t_stats[23].text)
            pct_turnover_drives_for_team  = float(t_stats[24].text)
            avg_starting_fld_pos = float(t_stats[25].text.strip('Own '))
            avg_drive_duration_for_team = t_stats[26].text
            avg_plays_per_drive_for_team  = float(t_stats[27].text)
            avg_yds_per_drive_for_team  = float(t_stats[28].text)
            avg_points_per_drive_for_team  = float(t_stats[29].text)
        elif i == 1:
            # Opponents' Stats/Team Defense Stats
            opp_stats = info.find_all('td', class_='right')
            #print(opp_stats)
            points_given = int(opp_stats[0].text)
            yds_given = int(opp_stats[1].text)
            defensive_plays = int(opp_stats[2].text)
            yds_per_play_given = float(opp_stats[3].text)
            tunovers_forced = int(opp_stats[4].text)
            fumbles_forced = int(opp_stats[5].text)
            first_downs_given = int(opp_stats[6].text)
            completions_given = int(opp_stats[7].text)
            pass_attempts_given = int(opp_stats[8].text)
            pass_yds_given = int(opp_stats[9].text)
            pass_td_given = int(opp_stats[10].text)
            interceptions_forced = int(opp_stats[11].text)
            yds_per_pass_given = float(opp_stats[12].text)
            first_downs_given_pass = int(opp_stats[13].text)
            rush_attempts_given = int(opp_stats[14].text)
            rush_yds_given = int(opp_stats[15].text)
            rush_td_given = int(opp_stats[16].text)
            yds_per_run_given = float(opp_stats[17].text)
            first_downs_given_run = int(opp_stats[18].text)
            penalties_against_opp = int(opp_stats[19].text)
            penalty_yds_against_opp  = int(opp_stats[20].text)
            penalty_firstdowns_against_opp  = int(opp_stats[21].text)
            total_drives_for_opp  = int(opp_stats[22].text)
            pct_scoring_drives_for_opp  = float(opp_stats[23].text)
            pct_turnover_drives_for_opp  = float(opp_stats[24].text)
            avg_starting_fld_pos_opp = float(opp_stats[25].text.strip('Own '))
            avg_drive_duration_for_opp = opp_stats[26].text
            avg_plays_per_drive_for_opp  = float(opp_stats[27].text)
            avg_yds_per_drive_for_opp = float(opp_stats[28].text)
            avg_points_per_drive_for_opp  = float(opp_stats[29].text)
        elif i == 2:
            # Offense Season Ranks
            t_ranks = info.find_all('td', class_='right')
            points_forced_rank = int(t_ranks[0].text)
            yds_forced_rank = int(t_ranks[1].text)
            tunovers_lost_rank = int(t_ranks[4].text)
            fumbles_lost_rank = int(t_ranks[5].text)
            first_downs_forced_rank = int(t_ranks[6].text)
            pass_attempts_forced_rank = int(t_ranks[8].text)
            pass_yds_forced_rank = int(t_ranks[9].text)
            pass_td_forced_rank = int(t_ranks[10].text)
            interceptions_thrown_rank = int(t_ranks[11].text)
            yds_per_pass_rank = int(t_ranks[12].text)
            rush_attempts_forced_rank = int(t_ranks[14].text)
            rush_yds_forced_rank = int(t_ranks[15].text)
            rush_td_forced_rank = int(t_ranks[16].text)
            yds_per_run_rank = int(t_ranks[17].text)
            pct_scoring_drives_for_team_rank  = int(t_ranks[23].text)
            pct_turnover_drives_for_team_rank  = int(t_ranks[24].text)
            avg_starting_fld_pos_rank = int(t_ranks[25].text)
            avg_drive_duration_for_team_rank = int(t_ranks[26].text)
            avg_plays_per_drive_for_team_rank  = int(t_ranks[27].text)
            avg_yds_per_drive_for_team_rank  = int(t_ranks[28].text)
            avg_points_per_drive_for_team_rank  = int(t_ranks[29].text)
        else:
            # Defense Season Ranks
            opp_ranks = info.find_all('td', class_='right')
            points_given_rank = int(opp_ranks[0].text)
            yds_given_rank = int(opp_ranks[1].text)
            tunovers_forced_rank = int(opp_ranks[4].text)
            fumbles_forced_rank = int(opp_ranks[5].text)
            first_downs_given_rank = int(opp_ranks[6].text)
            pass_attempts_given_rank = int(opp_ranks[8].text)
            pass_yds_given_rank = int(opp_ranks[9].text)
            pass_td_given_rank = int(opp_ranks[10].text)
            interceptions_forced_rank = int(opp_ranks[11].text)
            yds_per_pass_given_rank = int(opp_ranks[12].text)
            rush_attempts_given_rank = int(opp_ranks[14].text)
            rush_yds_given_rank = int(opp_ranks[15].text)
            rush_td_given_rank = int(opp_ranks[16].text)
            yds_per_run_given_rank = int(opp_ranks[17].text)
            pct_scoring_drives_for_opp_rank  = int(opp_ranks[23].text)
            pct_turnover_drives_for_opp_rank  = int(opp_ranks[24].text)
            avg_starting_fld_pos_opp_rank = int(opp_ranks[25].text)
            avg_drive_duration_for_opp_rank = int(opp_ranks[26].text)
            avg_plays_per_drive_for_opp_rank  = int(opp_ranks[27].text)
            avg_yds_per_drive_for_opp_rank  = int(opp_ranks[28].text)
            avg_points_per_drive_for_opp_rank  = int(opp_ranks[29].text)

    season_stats = soup.find('div', class_="table_wrapper", id='all_games')
    game_stats = season_stats.find('tbody').find_all('tr')
    for row in game_stats:
        if row.find_all('td')[0].text != '':   # Ignores playoffs and bye week blanks for game results
            info = row.find_all('td')
            week = row.th.text
            day_of_week = info[0].text
            date = info[1].text
            game_start = info[2].text
            game_outcome = info[4].text
            if info[5].text != '':
                overtime = info[5].text
            else:
                overtime = 'RG'
            record_after_game = info[6].text
            if info[7].text == '':
                team_playing_at = 'Home'
            elif info[7].text == 'N':
                team_playing_at = 'Neutral'
            else:
                team_playing_at = 'Away'
            game_opp = info[8].text
            points_scored = int(info[9].text)
            points_allowed = int(info[10].text)
            first_downs_forced = int(info[11].text)
            total_yds_forced = int(info[12].text)
            pass_yds_forced = int(info[13].text)
            rush_yds_forced = int(info[14].text)
            try:
                tunovers_lost = int(info[15].text)
            except:
                tunovers_lost = 0
            first_downs_given = int(info[16].text)
            total_yds_given = int(info[17].text)
            pass_yds_given = int(info[18].text)
            rush_yds_given = int(info[19].text)
            try:
                tunovers_forced = int(info[20].text)
            except:
                tunovers_forced = 0
            dict_stats_by_team_in_games[(team.text, week)] = {
                    'year': year,
                    'week': week,
                    'day_of_week': day_of_week,
                    'date': date,
                    'game_start_time': game_start,
                    'team_win_or_lose': game_outcome,
                    'overtime_game': overtime,
                    'record_after_game': record_after_game,
                    'team_playing_where': team_playing_at,
                    'game_opponent': game_opp,
                    'points_forced': points_scored,
                    'yds_forced': total_yds_forced,
                    'tunovers_lost': tunovers_lost,
                    'first_downs_forced': first_downs_forced,
                    'pass_yds_forced': pass_yds_forced,
                    'rush_yds_forced': rush_yds_forced,
                    'points_given': points_allowed,
                    'yds_given': total_yds_given,
                    'tunovers_forced': tunovers_forced,
                    'first_downs_given': first_downs_given,
                    'pass_yds_given': pass_yds_given,
                    'rush_yds_given': rush_yds_given
    }

    dict_stats_by_team[team.text] = {
            'points_forced': points_forced,
            'yds_forced': yds_forced,
            'offensive_plays': offensive_plays,
            'yds_per_play_forced': yds_per_play_forced,
            'tunovers_lost': tunovers_lost,
            'fumbles_lost': fumbles_lost,
            'first_downs_forced': first_downs_forced,
            'completions_forced': completions_forced,
            'pass_attempts_forced': pass_attempts_forced,
            'pass_yds_forced': pass_yds_forced,
            'pass_td_forced': pass_td_forced,
            'interceptions_thrown': interceptions_thrown,
            'yds_per_pass': yds_per_pass,
            'first_downs_forced_pass': first_downs_forced_pass,
            'rush_attempts_forced': rush_attempts_forced,
            'rush_yds_forced': rush_yds_forced,
            'rush_td_forced': rush_td_forced,
            'yds_per_run': yds_per_run,
            'first_downs_forced_run': first_downs_forced_run,
            'penalties_against_team': penalties_against_team,
            'penalty_yds_against_team': penalty_yds_against_team,
            'penalty_firstdowns_against_team': penalty_firstdowns_against_team,
            'total_drives_for_team': total_drives_for_team,
            'pct_scoring_drives_for_team': pct_scoring_drives_for_team,
            'pct_turnover_drives_for_team': pct_turnover_drives_for_team,
            'avg_starting_fld_pos': avg_starting_fld_pos,
            'avg_drive_duration_for_team': avg_drive_duration_for_team,
            'avg_plays_per_drive_for_team': avg_plays_per_drive_for_team,
            'avg_yds_per_drive_for_team': avg_yds_per_drive_for_team,
            'avg_points_per_drive_for_team': avg_points_per_drive_for_team,
            'points_given': points_given,
            'yds_given': yds_given,
            'defensive_plays': defensive_plays,
            'yds_per_play_given': yds_per_play_given,
            'tunovers_forced': tunovers_forced,
            'fumbles_forced': fumbles_forced,
            'first_downs_given': first_downs_given,
            'completions_given': completions_given,
            'pass_attempts_given': pass_attempts_given,
            'pass_yds_given': pass_yds_given,
            'pass_td_given': pass_td_given,
            'interceptions_forced': interceptions_forced,
            'yds_per_pass_given': yds_per_pass_given,
            'first_downs_given_pass': first_downs_given_pass,
            'rush_attempts_given': rush_attempts_given,
            'rush_yds_given': rush_yds_given,
            'rush_td_given': rush_td_given,
            'yds_per_run_given': yds_per_run_given,
            'first_downs_given_run': first_downs_given_run,
            'penalties_against_opp': penalties_against_opp,
            'penalty_yds_against_opp': penalty_yds_against_opp,
            'penalty_firstdowns_against_opp': penalty_firstdowns_against_opp,
            'total_drives_for_opp': total_drives_for_opp,
            'pct_scoring_drives_for_opp': pct_scoring_drives_for_opp,
            'pct_turnover_drives_for_opp': pct_turnover_drives_for_opp,
            'avg_starting_fld_pos_opp': avg_starting_fld_pos_opp,
            'avg_drive_duration_for_opp': avg_drive_duration_for_opp,
            'avg_plays_per_drive_for_opp': avg_plays_per_drive_for_opp,
            'avg_yds_per_drive_for_opp': avg_yds_per_drive_for_opp,
            'avg_points_per_drive_for_opp': avg_points_per_drive_for_opp
    }

    dict_ranks_by_team[team.text] = {
            'points_forced_rank': points_forced_rank,
            'yds_forced_rank': yds_forced_rank,
            'tunovers_lost_rank': tunovers_lost_rank,
            'fumbles_lost_rank': fumbles_lost_rank,
            'first_downs_forced_rank': first_downs_forced_rank,
            'pass_attempts_forced_rank': pass_attempts_forced_rank,
            'pass_yds_forced_rank': pass_yds_forced_rank,
            'pass_td_forced_rank': pass_td_forced_rank,
            'interceptions_thrown_rank': interceptions_thrown_rank,
            'yds_per_pass_rank': yds_per_pass_rank,
            'rush_attempts_forced_rank': rush_attempts_forced_rank,
            'rush_yds_forced_rank': rush_yds_forced_rank,
            'rush_td_forced_rank': rush_td_forced_rank,
            'yds_per_run_rank': yds_per_run_rank,
            'pct_scoring_drives_for_team_rank': pct_scoring_drives_for_team_rank,
            'pct_turnover_drives_for_team_rank': pct_turnover_drives_for_team_rank,
            'avg_starting_fld_pos_rank': avg_starting_fld_pos_rank,
            'avg_drive_duration_for_team_rank': avg_drive_duration_for_team_rank,
            'avg_plays_per_drive_for_team_rank': avg_plays_per_drive_for_team_rank,
            'avg_yds_per_drive_for_team_rank': avg_yds_per_drive_for_team_rank,
            'avg_points_per_drive_for_team_rank': avg_points_per_drive_for_team_rank,
            'points_given_rank': points_given_rank,
            'yds_given_rank': yds_given_rank,
            'tunovers_forced_rank': tunovers_forced_rank,
            'fumbles_forced_rank': fumbles_forced_rank,
            'first_downs_given_rank': first_downs_given_rank,
            'pass_attempts_given_rank': pass_attempts_given_rank,
            'pass_yds_given_rank': pass_yds_given_rank,
            'pass_td_given_rank': pass_td_given_rank,
            'interceptions_forced_rank': interceptions_forced_rank,
            'yds_per_pass_given_rank': yds_per_pass_given_rank,
            'rush_attempts_given_rank': rush_attempts_given_rank,
            'rush_yds_given_rank': rush_yds_given_rank,
            'rush_td_given_rank': rush_td_given_rank,
            'yds_per_run_given_rank': yds_per_run_given_rank,
            'pct_scoring_drives_for_opp_rank': pct_scoring_drives_for_opp_rank,
            'pct_turnover_drives_for_opp_rank': pct_turnover_drives_for_opp_rank,
            'avg_starting_fld_pos_opp_rank': avg_starting_fld_pos_opp_rank,
            'avg_drive_duration_for_opp_rank': avg_drive_duration_for_opp_rank,
            'avg_plays_per_drive_for_opp_rank': avg_plays_per_drive_for_opp_rank,
            'avg_yds_per_drive_for_opp_rank': avg_yds_per_drive_for_opp_rank,
            'avg_points_per_drive_for_opp_rank': avg_points_per_drive_for_opp_rank
    }
    
    dict_coaches_by_team[team.text] = {
            'head_coach': head_coach,
            'offensive_coord': offensive_coord,
            'defensive_coord': defensive_coord,
            'off_scheme': off_scheme,
            'def_scheme': def_scheme
    }
    
    wait_time = random.randint(2,11)
    print(f'Done extracting information for the {team.text}. Waiting for {wait_time} seconds before next request.')
    time.sleep(wait_time)
    return dict_stats_by_team, dict_ranks_by_team , dict_coaches_by_team, dict_stats_by_team_in_games