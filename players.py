import csv
import sys

class Player(object):
  def __init__(self, id, position, first_name, last_name, fppg, played, salary, game, team, opponent, injury_indicator, injury_details):
    self.id = id
    self.position = position
    self.first_name = first_name
    self.last_name = last_name
    self.fppg = fppg
    self.played = played
    self.salary = salary
    self.game = game
    self.team = team
    self.opponent = opponent
    self.injury_indicator = injury_indicator
    self.injury_details = injury_details
    self.value = float(self.fppg) / float(self.salary)
    
  def __lt__(self, other):
    return self.value < other.value

  def __repr__(self):
    return ", ".join([self.first_name, self.last_name, self.position, str(self.value)])

class Team(object):
  def __init__(self):
    self.players = []
  def add_player(self, p):
    self.players.append(p)
  def 
    
f = open('players.csv', 'r')
reader = csv.reader(f)
next(reader, None)
players = []
for row in reader:
  print row, len(row)
  players.append(Player(*row[:12]))
f.close()

print sorted(players, reverse=True)
