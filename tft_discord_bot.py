# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 23:16:08 2022

@author: Lance Tran
GOAL: Display tft rank for a given username
"""

from riotwatcher import TftWatcher
import pprint
import lightbulb

def get_API_key():
    k = open("riot_api_key.txt", "r")
    return k.read()

def get_discord_key():
    d = open("discord_key.txt", "r")
    return d.read()

def get_account_info(player):
    summId = player['id']
    tftDataList = tft_watcher.league.by_summoner(my_region, summId)
    tftAccountInfo = tftDataList[0]
    del tftAccountInfo['leagueId'], tftAccountInfo['queueType'], tftAccountInfo['summonerId'], tftAccountInfo['summonerName'], tftAccountInfo['veteran'], tftAccountInfo['inactive'], tftAccountInfo['freshBlood'], tftAccountInfo['hotStreak']
    
    return tftAccountInfo
    #print(tftAccountInfo['tier'], tftAccountInfo['rank'], tftAccountInfo['leaguePoints'], 'LP')
    #print(str(tftAccountInfo['wins']) + 'W', '-', str(tftAccountInfo['losses']) + 'L')

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
bot = lightbulb.BotApp(token = get_discord_key(), 
                       default_enabled_guilds=([insert discord server ID]))

my_region = 'na1'

@bot.command
@lightbulb.option('username', 'enter a username', type=str)
@lightbulb.command('search', 'Gets tft rank and match history')
@lightbulb.implements(lightbulb.SlashCommand)
async def tftInfo(context):
    player = tft_watcher.summoner.by_name(my_region, context.options.username)
    tftAccInfo = get_account_info(player)
    await context.respond(context.options.username + " is " + tftAccInfo['tier'] + " " + tftAccInfo['rank'] 
                          + " - " + str(tftAccInfo['leaguePoints']) + " " + 'LP\n' + 
                          str(tftAccInfo['wins']) + 'W - ' + str(tftAccInfo['losses']) + 'L')

bot.run()


