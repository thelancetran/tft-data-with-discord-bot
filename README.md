# tft-rank-discord-bot
Simple discord bot that returns a rank and other data based on a given username input.

My second project where I tried to work with APIs, notably from Riot Games and Discord. 
Tft_match_history takes a summoner name and returns their TFT (solo) tier, rank, league points (lp), and win-loss ratio. Additionally, returns the match data of the player's most recent tft game. Only the Riot Games API is used here. 
Tft_discord_bot similarly does the same, except it does not return the match data; however, it does incorporate the discord API.


Uses Riot Games developer API to access data from Teamfight Tactics. 
Used Spyder IDE within Anaconda python distribution to code. 
RiotWatcher (Riot Games API wrapper) used for accessibility. (https://riot-watcher.readthedocs.io/en/latest/) 
Hikari (Discord API wrapper) used for accessibility. (https://github.com/hikari-py/hikari) 
