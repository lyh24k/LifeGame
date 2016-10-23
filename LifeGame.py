import Tkinter
import random
import time
import os
from Tkinter import *

class GameMap(object):
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        Map=[([0]*cols) for i in range(rows)]
        self.Map=Map
        pass
    def reset(self,life_ratio):
        while life_ratio>0:
            i=random.randint(0,self.rows-1)
            j=random.randint(0,self.cols-1)
            if self.Map[i][j]==0:
                self.Map[i][j]=1
                life_ratio-=1
        pass
    def get_neighbor_count(self,row,col):
        count=0
        r=row-1
        while r<=row+1:
            c=col-1
            while c<=col+1:
                if r<0 or c<0 or r>self.rows-1 or c>self.cols-1:
                    c+=1
                    continue
                if self.Map[r][c]==1:
                    count+=1
                c+=1
                #pass
            r+=1
            #pass
        if self.Map[row][col]==1:
            count-=1
        return count
        pass
    def Change(self):
        r=0
        Newmap=self.Map
        while r<self.rows:
            c=0
            while c<self.cols:
                count=self.get_neighbor_count(r,c)
                if count>=4 or count<=1:
                    Newmap[r][c]=0
                elif count==3:
                    Newmap[r][c]=1
                c+=1
                #pass
            r+=1
            #pass
        return Newmap
        pass
    pass

gameCore=GameMap(10,15)
gameCore.reset(30)

mainWindow=Tk()
mainWindow.title("Click To Continue")

i=0;
j=0;

def flash(event):
	cells=[([0]*15)for i in range(10)]
	for i in range(10):
	    for j in range(15):
		    if gameCore.Map[i][j]==1:
			    cells[i][j]=Label(mainWindow,width=5,height=2,bg="black")		    
		    else:
			    cells[i][j]=Label(mainWindow,width=5,height=2,bg="white")
		    cells[i][j].grid(row=i,column=j)
	gameCore.Change()
	
	del cells
	pass

mainWindow.bind("<Button-1>",flash)

mainWindow.mainloop()

