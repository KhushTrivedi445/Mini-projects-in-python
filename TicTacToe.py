from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("tic tac toe")
root.geometry("340x365")
root.resizable(0,0)

clicked=True
count=0
#reset function

#disable all buttons
def Disable_buttons():
        bt1.config(state=DISABLED)
        bt2.config(state=DISABLED)
        bt3.config(state=DISABLED)
        bt4.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt6.config(state=DISABLED)
        bt7.config(state=DISABLED)
        bt8.config(state=DISABLED)
        bt9.config(state=DISABLED)
#Checking if we found winner or not
def getWinner():
        global winner
        winner=False
        if (bt1["text"]=="X" and bt2["text"]=="X" and bt3["text"]=="X" ):
                bt1.config(bg="Pink")
                bt2.config(bg="Pink")
                bt3.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()
        elif (bt4["text"]=="X" and bt5["text"]=="X" and bt6["text"]=="X" ):
                bt4.config(bg="Pink")
                bt5.config(bg="Pink")
                bt6.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt7["text"]=="X" and bt8["text"]=="X" and bt9["text"]=="X" ):
                bt7.config(bg="Pink")
                bt8.config(bg="Pink")
                bt9.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt1["text"]=="X" and bt4["text"]=="X" and bt7["text"]=="X" ):
                bt1.config(bg="Pink")
                bt4.config(bg="Pink")
                bt7.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt2["text"]=="X" and bt5["text"]=="X" and bt8["text"]=="X" ):
                bt2.config(bg="Pink")
                bt5.config(bg="Pink")
                bt8.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt3["text"]=="X" and bt9["text"]=="X" and bt6["text"]=="X" ):
                bt3.config(bg="Pink")
                bt9.config(bg="Pink")
                bt6.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt3["text"]=="X" and bt5["text"]=="X" and bt7["text"]=="X" ):
                bt3.config(bg="Pink")
                bt5.config(bg="Pink")
                bt7.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt1["text"]=="X" and bt5["text"]=="X" and bt9["text"]=="X" ):
                bt1.config(bg="Pink")
                bt5.config(bg="Pink")
                bt9.config(bg="Pink")
                winner=True
                messagebox.showinfo("winner", "yayy X you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt1["text"] == "O" and bt2["text"] == "O" and bt3["text"] == "O"):
                bt1.config(bg="Pink")
                bt2.config(bg="Pink")
                bt3.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt4["text"] == "O" and bt5["text"] == "O" and bt6["text"] == "O"):
                bt4.config(bg="Pink")
                bt5.config(bg="Pink")
                bt6.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt7["text"] == "O" and bt8["text"] == "O" and bt9["text"] == "O"):
                bt7.config(bg="Pink")
                bt8.config(bg="Pink")
                bt9.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt1["text"] == "O" and bt4["text"] == "O" and bt7["text"] == "O"):
                bt1.config(bg="Pink")
                bt4.config(bg="Pink")
                bt7.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt2["text"] == "O" and bt5["text"] == "O" and bt8["text"] == "O"):
                bt2.config(bg="Pink")
                bt5.config(bg="Pink")
                bt8.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt3["text"] == "O" and bt9["text"] == "O" and bt6["text"] == "O"):
                bt3.config(bg="Pink")
                bt9.config(bg="Pink")
                bt6.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt3["text"] == "O" and bt5["text"] == "O" and bt7["text"] == "O"):
                bt3.config(bg="Pink")
                bt5.config(bg="Pink")
                bt7.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (bt1["text"] == "O" and bt5["text"] == "O" and bt9["text"] == "O"):
                bt1.config(bg="Pink")
                bt5.config(bg="Pink")
                bt9.config(bg="Pink")
                winner = True
                messagebox.showinfo("winner", "yayy O you Won the match🥳🤩!!!!!")
                Disable_buttons()

        elif (winner != True and count == 9):
                messagebox.showinfo("draw", "hey its a draw")
                Disable_buttons()


#code for X and O
def get_digit(b):
        global clicked,count
        if (b["text"]==" " and clicked==True):
                b["text"]="X"
                clicked=False
                count+=1
                getWinner()

        elif (b["text"]==" " and clicked==False):
                b["text"]="O"
                clicked=True
                count+=1
                getWinner()
        else:
                messagebox.showerror("Tic tac toe","Hey you have selected the wrong box\n Please try again")


def ResetGame():
        global bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9
        global clicked,count
        clicked=True
        count=0

        bt1=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt1))
        bt1.grid(row=0,column=0)

        bt2=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt2))
        bt2.grid(row=0,column=1)

        bt3=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt3))
        bt3.grid(row=0,column=2)

        bt4=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt4))
        bt4.grid(row=1,column=0)

        bt5=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt5))
        bt5.grid(row=1,column=1)

        bt6=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt6))
        bt6.grid(row=1,column=2)

        bt7=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt7))
        bt7.grid(row=2,column=0)

        bt8=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt8))
        bt8.grid(row=2,column=1)

        bt9=Button(root,text=" ",font=("Verdana",20),bg="white",fg="black",height=3,width=6,command=lambda : get_digit(bt9))
        bt9.grid(row=2,column=2)

#create menu
myMenu=Menu(root)
root.config(menu=myMenu)

#Create options menu
options=Menu(myMenu,tearoff=False)
myMenu.add_cascade(label="Options",menu=options)
options.add_command(label="Reset Game",command=lambda :ResetGame())

ResetGame()
root.mainloop()