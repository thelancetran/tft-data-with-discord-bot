# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 23:16:08 2022

@author: Lance Tran
GOAL: Display tft rank for given username
"""

from riotwatcher import TftWatcher
import pprint

def get_API_key():
    k = open("riot_api_key.txt", "r")
    return k.read()

def get_account_info(player):
    summId = player['id']
    tftDataList = tft_watcher.league.by_summoner(my_region, summId)
    tftAccountInfo = tftDataList[0]
    
    print(tftAccountInfo['tier'], tftAccountInfo['rank'], tftAccountInfo['leaguePoints'], 'LP')
    print(str(tftAccountInfo['wins']) + 'W', '-', str(tftAccountInfo['losses']) + 'L')

def get_tft_match_history(player):
    puuid = player['puuid']
    matchIDs = tft_watcher.match.by_puuid(my_region, puuid, 1)

    for x in range(len(matchIDs)):
        tftMatchData = tft_watcher.match.by_id(my_region, matchIDs[x])
        matchInfo = tftMatchData['info']
        matchPlayerList = matchInfo['participants']
        for x in range(len(matchPlayerList)):
            playerMatchData = matchPlayerList[x]
            checkPlayer = playerMatchData['puuid']
            if checkPlayer == puuid:
                del playerMatchData['companion'], playerMatchData['puuid'], playerMatchData['time_eliminated']
                pprint.pprint(playerMatchData)
            
    
#%% Main
tft_watcher = TftWatcher(get_API_key())

my_region = 'na1'

user = input("Enter Summoner Name:")
player = tft_watcher.summoner.by_name(my_region, user)
#player is dict containing id, accountId, puuid, name, profileIconId, revisionDate, and summonerLevel

get_account_info(player)
get_tft_match_history(player)


