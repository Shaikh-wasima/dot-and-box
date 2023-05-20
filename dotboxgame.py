

from tkinter import Tk
from tkinter import StringVar 
from tkinter import Frame 
from tkinter import Canvas 
from tkinter import Label 
from tkinter import N
from tkinter import HORIZONTAL f
rom tkinter import VERTICAL 
from tkinter import font


TOL = 8
CELLSIZE = 40
OFFSET = 10	#size between each dots 
CIRCLERAD = 5 #radius of dots 
DOTOFFSET = OFFSET + CIRCLERAD 
GAME_H = 400
GAME_W = 400


class Player(object):

def    init (self, name, color="orange"): 
self.score = 0
self.str = StringVar() 
self.name = name 
self.color = color

def update(self):	#constructor for updating score of players self.str.set(self.name + ": %d" % self.score)
class MyFrame(Frame):

def     init (self, master): 
Frame. init (self, master)
self.canvas = Canvas(self, height = GAME_H, width = GAME_W) 
self.canvas.bind("<Button-1>", 
lambda e:self.click(e)) 
self.canvas.grid(row=0,column=0)

self.dots = [[self.canvas.create_oval(CELLSIZE*i+OFFSET, \
CELLSIZE*j+OFFSET, \ CELLSIZE*i+OFFSET+2*CIRCLERAD, \ CELLSIZE*j+OFFSET+2*CIRCLERAD, \
fill="") \for j in range(10)] for i in range(10)] 
self.lines = []

self.infoframe = Frame(self)
self.players = [Player("Player1","green"), Player("Player2","blue")] 
self.infoframe.players = [Label(self.infoframe, textvariable = i.str) 
for i in self.players] 
for i in self.infoframe.players:
i.grid()

self.turn = self.players[0] 
self.update_players()
self.infoframe.grid(row = 0, column = 1, sticky = N) 
self.grid()
def update_players(self): 
for i in self.players:
i.update()

def click(self, event):	#for clicking event on dots x,y = event.x, event.y
orient = self.isclose(x,y)

if orient:
if self.line_exists(x,y, orient): 
return
l = self.create_line(x,y, orient) 
score = self.new_box_made(l) 
if score:
self.turn.score += score 
self.turn.update() 
self.check_game_over()
else:
index = self.players.index(self.turn) 
self.turn = self.players[1-index]
self.lines.append(l)

def create_line(self, x, y, orient):	# for creating lines
startx = CELLSIZE * ((x-OFFSET)//CELLSIZE) + DOTOFFSET
starty = CELLSIZE * ((y-OFFSET)//CELLSIZE) + DOTOFFSET 
tmpx = (x-OFFSET)//CELLSIZE
tmpy = (y-OFFSET)//CELLSIZE

if orient == HORIZONTAL: 
endx = startx + CELLSIZE 
endy = starty
else:
endx = startx
endy = starty + CELLSIZE
#print "line drawn: %d,%d to %d,%d" % (startx,starty,endx,endy) return self.canvas.create_line(startx,starty,endx,endy)


def new_box_made(self, line): 
score = 0
x0,y0,x1,y1 = self.canvas.coords(line) 
if x0 == x1: # vertical line
midx = x0
midy = (y0+y1)/2
pre = (x0 - CELLSIZE/2, midy) 
post = (x0 + CELLSIZE/2, midy)
elif y0 == y1: # horizontal line 
midx = (x0 + x1)/2
midy = y0
pre = (midx, y0 - CELLSIZE/2) 
post = (midx, y0 + CELLSIZE/2)

if len(self.find_lines(pre)) == 3: # not 4, because newly created line is self.fill_in(pre)	# is not returned (?!)
score += 1
if len(self.find_lines(post)) == 3: 
self.fill_in(post)
score += 1 
return score

def find_lines(self, coords): 
x, y = coords
if x < 0 or x > GAME_W: 
return []
if y < 0 or y > GAME_W: 
return []
#print "Cell center: %d,%d" % (x,y)
lines = [x for x in self.canvas.find_enclosed(x-CELLSIZE,\
y-CELLSIZE,\ x+CELLSIZE,\ y+CELLSIZE)\
if x in self.lines] #print lines
return lines

def fill_in(self, coords): x,y = coords
self.canvas.create_text(x,y,text=self.turn.name, fill=self.turn.color)

def isclose(self, x, y): x -= OFFSET
 
 
 def isclose(self, x, y): 
 x -= OFFSET
 
 y -= OFFSET
dx = x - (x//CELLSIZE)*CELLSIZE d
y = y - (y//CELLSIZE)*CELLSIZE

if abs(dx) < TOL:
if abs(dy) < TOL:
return None # mouse in corner of box; ignore 
else:
return VERTICAL 
elif abs(dy) < TOL:
return HORIZONTAL 
else:
return None

def line_exists(self, x,y, orient): #if trying to draw on created lines then id_ = self.canvas.find_closest(x,y,halo=TOL)[0]
if id_ in self.lines: 
return True
else:
return False

def check_game_over(self):	#for result(winner ,loser) total = sum([x.score for x in self.players])
if total == 81:	#if all dots are done
if self.players[0].score>self.players[1].score: 
self.canvas.create_text(GAME_W/2, GAME_H/2,\
text="Player 1 Win", font="arial", \ fill="black")
elif self.players[0].score<self.players[1].score: 
self.canvas.create_text(GAME_W/2, GAME_H/2, \
text="Player 2 Win", font="arial", \ fill="black")
else:
self.canvas.create_text(GAME_W/2, GAME_H/2, \ text="game over", font="arial", \ fill="black")

mainw = Tk()
mainw.f = MyFrame(mainw) 
mainw.mainloop()

