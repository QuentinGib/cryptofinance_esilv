# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:06:01 2021

@author: Quentin
"""
import random
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from tkinter import *

#alpha: selfish miners mining power (percentage),
#N: number of simulations run
def simulate(alpha,N):
  
    # Start state 
    state=0
    # the length of the blockchain
    ChainLength=0
    # the revenue of the selfish mining pool
    SelfishRevenue=0
    # the length of hidden blocks
    HiddenBlocks=0

    #A round begin when the state=0
    for i in range(N):
        r=random.random()
        if state==0:
            #The selfish pool has 0 hidden block.
            if r<=alpha:
                #The selfish pool mines a block.
                #They don't publish it. 
                # ChainLength no change
                HiddenBlocks=1
                state=1
            else:
                #The honest miners found a block.
                #The round is finished : the honest miners found 1 block
                # and the selfish miners found 0 block.
                ChainLength+=1
                state=0

        elif state==1:
            #The selfish pool has 1 hidden block.
            if r<=alpha:
                #The selfish miners found a new block, they have two.
                # ChainLength no change
                HiddenBlocks=2
                state=2
            else:
                ChainLength+=1
                # Lead was 1, others find a block.
                HiddenBlocks=0
                #If the pool has a private branch of length 1 and the others mine one block, the pool publishes its branch, which results in two public branches of length 1
                state=-1

        elif state==-1:
            #The honest miners found a block.
            #So the selfish miners publish their hidden block.
            #The blockchain is forked with one block in each fork.
            if r<=alpha:
                #the selfish miners found a block in their fork.
                #The round is finished : Selfish miners won 2 blocks and the honest miners 0.
                SelfishRevenue+=2
                ChainLength+=1
                # HiddenBlocks no change
                state=0
            # elif r<=alpha+(1-alpha)*gamma:
            #     SelfishRevenue+=1
            #     ChainLength+=1
            #     # HiddenBlocks no change
            #     state=0
            else:
                # SelfishRevenue no change, Others obtain a revenue of two
                ChainLength+=1
                # HiddenBlocks no change
                state=0

        elif state==2:
            #The selfish pool has 2 hidden block.
            if r<=alpha:
                # ChainLength no change
                HiddenBlocks+=1
                state+=1
            else:
                #The honest miners found a block.
                ChainLength+= 2
                SelfishRevenue+=2  # (g) Lead was 2, others find a block.
                HiddenBlocks=0  #If the others mine a block when the lead is two, the pool publishes its private branch, and the system drops to a lead of 0.
                state=0

        elif state>2:
            if r<=alpha:
                #The selfish miners found a new block
                # ChainLength no change
                HiddenBlocks+=1
                state+=1
            else:
                #The honest miners found a block
                ChainLength+=1
                SelfishRevenue+=1  # Lead was more than 2, others win.
                HiddenBlocks-=1
                state-=1

    #print("state,ChainLength,SelfishRevenue,HiddenBlocks:",state,ChainLength,SelfishRevenue,HiddenBlocks)
    result = float(SelfishRevenue)/ChainLength
    return result

def resultSelfish(fenetre,alpha,N):

    alpha = float(alpha.get())
    N = int(N.get())

    result = simulate(alpha, N)
    label = Label(fenetre, text="Theoretical probability :"+str((alpha*(1-alpha)**2*(4*alpha)-alpha**3)/(1-alpha*(1+(2-alpha)*alpha))))
    label.grid(column=0, row=3)
    label = Label(fenetre, text="Simulated probability : "+str(result))
    label.grid(column=0, row=4)

    y = []
    c = []
    for i in range(50):
        a = i/100
        y.append(simulate(a, N))
        c.append(a)
    

    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    
    plot1 = fig.add_subplot(111) 
  
    
    plot1.plot(y, color="r")
    plot1.plot(c, color="g")  
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = fenetre)   
    canvas.draw() 
  
    canvas.get_tk_widget().grid(column=0, columnspan=2, row=5)

alpha=0.33
Nsimu=10**6

# print("Theoretical probability :",(alpha*(1-alpha)**2*(4*alpha+gamma*(1-2*alpha))-alpha**3)/(1-alpha*(1+(2-alpha)*alpha)))
# print("Simulated probability :",Simulate(alpha,gamma,Nsimu))