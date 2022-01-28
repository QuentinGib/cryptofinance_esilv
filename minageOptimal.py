# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:02:36 2021

@author: Quentin
"""
# import random
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from tkinter import *

"""
a : nb de blocs secrets découverts
h : taille de la blockchain off
n : nombre maximal de blocs découverts
q : relative hashrate of the attacker
"""
def optimalMining(a, h, n, q, c) :
    
    if n == 0:
        if a > h:
            return 	a - (a-h)*c
        else:
            return 0
    
    if a > h+1 :
        return max(h+1-c+optimalMining(a - h - 1, 0, n, q, c),
                   q * optimalMining(a+1, h, n-1, q, c) + (1-q) * (optimalMining(a, h+1, n-1, q, c)-c))
    if a == h + 1:
        return max(h+1-c,
                   q * optimalMining(a+1, h, n-1, q, c) + (1-q) * (optimalMining(a, h+1, n-1, q, c)-c))
    if a <= h:
        return max(0, 
                   q * optimalMining(a+1, h, n-1, q, c) + (1-q) * (optimalMining(a, h+1, n-1, q, c)-c))

a = 0
h = 0
n = 3
q = 0.43
c = q

def resultOptimalMining(fenetre, a, h, n, q, c):

    a = float(a.get()) 
    h = float(h.get())
    n = float(n.get())
    q = float(q.get())
    c = float(c.get())

    result = optimalMining(a, h, n, q, c)
    label = Label(fenetre, text="Simulated probability : "+str(result))
    label.grid(column=0, row=6)

    y = []
    for i in range(50):
        y.append(optimalMining(a, h, n, i/100, i/100))
    

    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    
    plot1 = fig.add_subplot(111) 
  
    
    plot1.plot(y)  
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = fenetre)   
    canvas.draw() 
  
    canvas.get_tk_widget().grid(column=0, columnspan=2, row=7)
    
    # toolbar = NavigationToolbar2Tk(canvas, 
    #                                fenetre) 
    # toolbar.update() 
    
    # canvas.get_tk_widget().grid(column=0, row=7) 

