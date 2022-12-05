##############
# basic python
##############

##########################
# how to read this chapter
##########################
1 + 1

##########
# comments
##########

# print the result of 1 + 1
print(1 + 1)

###########
# variables
###########

goals_scored = 2

goals_scored
3*goals_scored

goals_scored = goals_scored + 1
goals_scored

####################
# types of variables
####################

keeper_saves = 12  # int
ball_speed_kmh = 96.5  # float

starting_fwd = 'Lionel Messie'
description = "It's a goal"

type(starting_fwd)

type(keeper_saves)

player_description = f'{description} by {starting_fwd}!'
player_description

# string methods
'gooaaaaal'.upper()

'Christiano Ronaldo, Man U'.replace('Man U', 'Real Madrid')

####################################
# How to figure things out in Python
####################################
'lionel messie'.capitalize()

'  lionel messie'
'lionel messie'

'  lionel messie'.lstrip()

#######
# bools
#######
team1_goals = 2
team2_goals = 1

# and these are all bools:
team1_won = team1_goals > team2_goals
team2_won = team1_goals < team2_goals
teams_tied = team1_goals == team2_goals
teams_did_not_tie = team1_goals != team2_goals

type(team1_won)
teams_did_not_tie

# error because test for equality is ==, not =
# teams_tied = (team1_goals = team2_goals)  # commented out since it throws an error

shootout = (team1_goals > 3) and (team2_goals > 3)
at_least_one_good_team = (team1_goals > 3) or (team2_goals > 3)
you_guys_are_bad = not ((team1_goals > 1) or (team2_goals > 1))
meh = not (shootout or at_least_one_good_team or you_guys_are_bad)

###############
# if statements
###############
if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

message
