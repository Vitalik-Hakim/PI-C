from tkinter import *
from tkinter import ttk
import sys
import requests
import sys
from pi import *
import os
import pyttsx3


root = Tk()
root.geometry('1080x400')
#root.resizable(0,0)
root.config(bg = 'black')
root.title("πPI-C GAME")
username1 = StringVar()
username2 = StringVar()

def print_user1():
    print(username1.get())
    get_ready2['state'] = DISABLED

    
def print_user2():
    print(username2.get())
    get_ready1['state'] = DISABLED



###R######## short squeeze for Spich :) #########
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
######## short squeeze #########ecord######
    

Label(root, text = "πPI-C", font = "courier 30 bold", bg='black',fg="lime").pack()
Label(root,text ="@Vitalik-Hakim", font = 'arial 3 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Label(root,text ="TYPE PI HERE", font = 'courier 13 bold', bg='#1B1212',fg="lime").place(x=200,y=60)
Input_text = Text(root,font = 'courier 11 bold', height = 11, padx=5, pady=5, width = 50 ,bg='black',fg="lime",insertbackground="lime")
Input_text.place(x=30,y = 100)
entry_user1 =ttk.Entry(root, textvariable = username1, justify = CENTER,
                                     font = ('courier', 15, 'bold')).place(x=29,y=350)
Label(root,text ="TYPE PI HERE", font = 'courier 13 bold',bg='#1B1212',fg="lime").place(x=780,y=60)
Output_text = Text(root,font = 'courier 11 bold', height = 11, padx=5, pady=5, width = 50 ,bg='black',fg="lime",insertbackground="lime")
Output_text.place(x = 600 , y = 100)
entry_user2 =ttk.Entry(root, textvariable = username2, justify = CENTER,
                                     font = ('courier', 15, 'bold')).place(x=600,y=350)

get_ready2 = Button(root, text = 'Ready',font = 'arial 12 bold',pady = 2,command = print_user1  , bg = 'lime', activebackground = 'sky blue', relief="flat", cursor="hand2")
get_ready2.place(x = 305, y= 350 )
get_ready1 = Button(root, text = 'Ready',font = 'arial 12 bold',pady = 2,command =print_user2, bg = 'lime', activebackground = 'sky blue', relief="flat", cursor="hand2")
get_ready1.place(x = 870, y= 350 )






def PIDAY():
    get_ready2['state'] = DISABLED
    get_ready1['state'] = DISABLED
    user1 = username1.get()
    user2 = username2.get()


    alice = Input_text.get(1.0, END+"-1c") #Player one
    bob = Output_text.get(1.0, END+"-1c") #Player two




    #alice = input("{} Say the pi you know: ".format(user1))
    #bob = input("{} Say the pi you know: ".format(user2))

    alist = list(alice)
    blist = list(bob)

    lenA  = len(alist)
    lenB  = len(blist)


    #Verify order or pi numbers
    correct1 = True
    correct2 = True
    #Alice verify
    for pis in range(lenA):
        if pi_100[0:lenA] == alice:
            pass
            correct1 = True
        else:
            print("{} is incorrect! \n".format(user1))
            SpeakText("{} is incorrect! \n".format(user1))
            correct1 = False
            break

    #Bob verify
    for pis in range(lenB):
        if pi_100[0:lenB] == bob:
            correct2 = True
            pass
        else:
            print("{} is incorrect! \n".format(user2))
            SpeakText("{} is incorrect! \n".format(user2))
            correct2 = False
            break


    if correct1 == False and correct2 == False:
        SpeakText("You both suck! nyeh")
        print("You both suck! nyeh")
        os.popen('PI-Cg.py')
        sys.exit()
    elif correct1 == True and correct2 == False:
        Winner = "{} is the winner!".format(user1)
        SpeakText(Winner)
        print(Winner)
        os.popen('PI-Cg.py')
        sys.exit()
    elif correct2 == True and correct1 == False:
        Winner = "{} is the winner!".format(user2)
        print(Winner)
        SpeakText(Winner)
        os.popen('PI-Cg.py')
        sys.exit()
    else:
        pass



    #If they cross this line then its time for lenEval

    if len(alice) > len(bob):
        Winner = "{} is the winner!".format(user1)
        SpeakText(Winner)
        print(Winner)
    elif len(bob) > len(alice):
        Winner = "{} is the winner!".format(user2)
        SpeakText(Winner)
        print(Winner)
    else:
        print("Its a tie between {} and {}".format(user1,user2))
        SpeakText("Its a tie between {} and {}".format(user1,user2))
    Output_text.delete(1.0, END)
    Output_text.insert(END, Winner)


start_btn = Button(root, text = 'Stop',font = 'arial 12 bold',pady = 5,padx=31,command = "PIDAY" , bg = 'red', activebackground = 'sky blue', relief="flat", cursor="hand2")
start_btn.place(x = 490, y= 180 )
stop_btn = Button(root, text = 'Start',font = 'arial 12 bold',pady = 5,padx=31,command = PIDAY , bg = 'royal blue1', activebackground = 'sky blue', relief="flat", cursor="hand2")
stop_btn.place(x = 490, y= 130 )
about_btn = Button(root, text = 'About',font = 'arial 12 bold',pady = 5,padx=26,command = "PIDAY" , bg = 'purple', activebackground = 'sky blue', relief="flat", cursor="hand2")
about_btn.place(x = 490, y= 250 )
root.mainloop()
