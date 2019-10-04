import random
import human

team1=['ninja','zombie','zombie','pirate','ninja','ninja','Rasengan']
team2=['pirate','ninja','pirate','zombie','pirate','pirate','Booty']
team3=['pirate','ninja','zombie','zombie','ninja','pirate','G16']


def match(t1,t2,point):
    dict = {
        'ninja':  t1 if (t2[point] == 'pirate') else t2,
        'pirate': t1 if (t2[point] == 'zombie') else t2,
        'zombie': t1 if (t2[point] == 'ninja') else t2 
    }
    return(dict[t1[point]])


matchup=[
    [team1,team2],
    [team1,team3],
    [team2,team3],
    [team1,team3],
    [team1,team2],
    [team2,team3]
    ]
winners=[]
dict = {
    'pirate': human.carl,
    'ninja': human.bob,
    'zombie': human.zb1
}
for i in range (6):
    winner = match (matchup[i][0],matchup[i][1],i)
    
    if winner == matchup[i][0]:
        loser = matchup[i][1]
    else:
        loser = matchup[i][0]
    print('team',winner[6],'wins when',winner[i],'beats',loser[i])
    dict[winner[i]].taunt(dict[loser[i]])


