# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:28:52 2021

@author: Quentin
"""
from tkinter import *
from functools import partial
from onePlusTwo import *
from selfishQ import *
from doubleSpending import *
from minageOptimal import *

fenetre = Tk()
fenetre.title("Cryptofinance")

menubar = Menu(fenetre)

labelfirst = Label(fenetre, text="Choisissez votre stratégie")
labelfirst.grid(column=0, row=0)

def onePlusTwo():
    fenetre = Tk()
    fenetre.title("1+2")
    
    label2 = Label(fenetre, text="Hashrate of the attacker (between 0 and 100) : ")
    label2.grid(column=0, row=0)
    text = StringVar(fenetre)
    alice_power = Entry(fenetre, textvariable=text)
    alice_power.grid(column=1, row=0)
    button = Button(fenetre, text='Try attack', 
                command=partial(resultOnePlusTwo, fenetre, text))
    button.grid(column=10, row=0)
    
    fenetre.mainloop()
    
def selfish():
    fenetre = Tk()
    fenetre.title("Selfish mining")
    
    label1 = Label(fenetre, text="alpha (between 0 and 1) : ")
    label1.grid(column=0, row=0)
    alpha = StringVar(fenetre)
    alpha_entry = Entry(fenetre, textvariable=alpha)
    alpha_entry.grid(column=1, row=0)
    
    label2 = Label(fenetre, text="gamma (between 0 and 1) : ")
    label2.grid(column=0, row=1)
    gamma = StringVar(fenetre)
    gamma_entry = Entry(fenetre, textvariable=gamma)
    gamma_entry.grid(column=1, row=1)
    
    label3 = Label(fenetre, text="Number of simulation run : ")
    label3.grid(column=0, row=2)
    N = StringVar(fenetre)
    N_entry = Entry(fenetre, textvariable=N)
    N_entry.grid(column=1, row=2)
    
    button = Button(fenetre, text='Try attack', 
                command=partial(resultSelfish, fenetre, alpha, gamma, N))
    button.grid(column=3, row=3)
    
def doubled():
    fenetre = Tk()
    fenetre.title("Double dépense")
    
    label1 = Label(fenetre, text="Number of confirmations : ")
    label1.grid(column=0, row=0)
    z = StringVar(fenetre)
    z_entry = Entry(fenetre, textvariable=z)
    z_entry.grid(column=1, row=0)
    
    label2 = Label(fenetre, text="Relative hashrate of the attacker : ")
    label2.grid(column=0, row=1)
    q = StringVar(fenetre)
    q_entry = Entry(fenetre, textvariable=q)
    q_entry.grid(column=1, row=1)
    
    label3 = Label(fenetre, text="Amount of the double spend : ")
    label3.grid(column=0, row=2)
    v = StringVar(fenetre)
    v_entry = Entry(fenetre, textvariable=v)
    v_entry.grid(column=1, row=2)
    
    label4 = Label(fenetre, text="Maximum delay authorized : ")
    label4.grid(column=0, row=3)
    A = StringVar(fenetre)
    A_entry = Entry(fenetre, textvariable=A)
    A_entry.grid(column=1, row=3)
    
    label5 = Label(fenetre, text="Number of cycles : ")
    label5.grid(column=0, row=4)
    n = StringVar(fenetre)
    n_entry = Entry(fenetre, textvariable=n)
    n_entry.grid(column=1, row=4)
    
    button = Button(fenetre, text='Simulate attack', 
                command=partial(resultDoubleSpending, fenetre, z, q, v, A, n))
    button.grid(column=3, row=5)
    
def opti():
    fenetre = Tk()
    fenetre.title("Minage optimal")
    
    label1 = Label(fenetre, text="Blocs secrets découverts : ")
    label1.grid(column=0, row=0)
    z = StringVar(fenetre)
    z_entry = Entry(fenetre, textvariable=z)
    z_entry.grid(column=1, row=0)
    
    label2 = Label(fenetre, text="Taille de la blockchain officielle : ")
    label2.grid(column=0, row=1)
    h = StringVar(fenetre)
    h_entry = Entry(fenetre, textvariable=h)
    h_entry.grid(column=1, row=1)
    
    label3 = Label(fenetre, text="Nombre de cycles : ")
    label3.grid(column=0, row=2)
    v = StringVar(fenetre)
    v_entry = Entry(fenetre, textvariable=v)
    v_entry.grid(column=1, row=2)
    
    label5 = Label(fenetre, text="Hashrate relatif de l'attaquant' : ")
    label5.grid(column=0, row=3)
    q = StringVar(fenetre)
    q_entry = Entry(fenetre, textvariable=q)
    q_entry.grid(column=1, row=3)
    
    label4 = Label(fenetre, text="c : ")
    label4.grid(column=0, row=4)
    A = StringVar(fenetre)
    A_entry = Entry(fenetre, textvariable=A)
    A_entry.grid(column=1, row=4)
    
    button = Button(fenetre, text='Simulate attack', 
                command=partial(resultOptimalMining, fenetre, z, h, v, q, A))
    button.grid(column=3, row=5)


menu = Menu(menubar, tearoff=0)
menu.add_command(label="1+2", command=onePlusTwo)
menu.add_command(label="Selfish mining", command=selfish)
menu.add_command(label="Double dépense", command=doubled)
menu.add_command(label="Minage optimal", command=opti)

fenetre.config(menu=menu)

fenetre.mainloop()

