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
    self.salary = float(salary)
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
  
  def name(self):
    return self.first_name + " " + self.last_name

f = open('players.csv', 'r')
reader = csv.reader(f)
next(reader, None)
players = []
for row in reader:
  players.append(Player(*row[:12]))
f.close()

players = sorted(players, reverse=True)

salary_cap = 60000

qb  = [x for x in players if x.position == 'QB']
rb  = [x for x in players if x.position == 'RB']
wr  = [x for x in players if x.position == 'WR']
te  = [x for x in players if x.position == 'TE']
k   = [x for x in players if x.position ==  'K']
d   = [x for x in players if x.position ==  'D']

roster = qb[:1], rb[:2], wr[:3], te[:1], k[:1], d[:1]

roster = [item for sublist in roster for item in sublist]
cs = 0

for p in roster:
  cs += p.salary

if cs < salary_cap:
  print "Found Team"
  for p in roster:
    print p.position, p.name(), p.salary
  print "Total Salary:", cs
