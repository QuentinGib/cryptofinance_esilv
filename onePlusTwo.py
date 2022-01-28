# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:47:31 2021

@author: Quentin
"""
from random import randrange
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from tkinter import *

def oneTwo(alice_power):
    alice_blocks = []
    block_test = 0
    h_test = 0
    h = 0
    r1 = 0
    h1 = 0
    
    for i in range(100000):
        block = 0
        # Sur 3 blocks
        for j in range(3):
            rand = randrange(101)
            
            # Premier block trouvé par bob => On arrête
            if j == 0 and rand > alice_power:
                alice_blocks.append(0)
                h += 1
                h_test += 1
                break
            
            # Alice trouve un block, on avance d'un block
            if rand <= alice_power:
                block+=1
                block_test += 1
                
            # Au dernier block, si Alice a trouvé au moins 2 blocks
            # elle les ajoute à la blockchain officielle
            if block > 1 and j == 2:
                alice_blocks.append(block)
                h += block
            
            # Sinon si elle n'a trouvé qu'un bloc, elle ne gagne rien
            elif block == 1 and j == 2:
                alice_blocks.append(0)
                h += 2
            
            h_test += 1
        
        # if i == 1:
        #     r1 = alice_blocks[0]
        #     h1 = h
    
    r = sum(alice_blocks)
    # print("r = ", r)
    # print("h = ", h)
    
    result = r/h
    return result, (block_test/h_test)

def resultOnePlusTwo(fenetre, alicep):

    alice_power = int(alicep.get())

    result, classique = oneTwo(alice_power)

    label = Label(fenetre, text="Rentabilité 1+2 : "+str(result))
    label.grid(column=0, row=1)
    label2 = Label(fenetre, text="Rentabilité classique : "+str(classique))
    label2.grid(column=0, row=2)

    y = []
    c = []
    for i in range(50):
        result, classique = oneTwo(i)
        y.append(result)
        c.append(classique)
    

    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    
    plot1 = fig.add_subplot(111) 
  
    # plot1.title("Gain en fonction de la puissance de hashage")
    plot1.plot(y, label="Rentabilité 1+2", color="r")
    plot1.plot(c, label="Rentabilité classique", color="g")  
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = fenetre)   
    canvas.draw() 
  
    canvas.get_tk_widget().grid(column=0, columnspan=2, row=3)

# print("Rentabilité 1+2 : ", oneTwo(alice_power))
# print("Rentabilité classique : ", (block_test/h_test))

    