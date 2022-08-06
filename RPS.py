from tkinter import Tk,Button,Label,PhotoImage,Menu,messagebox
from random import choice
from PIL import ImageTk,Image

def menu():
    menu = Menu()
    file = Menu(menu)
    menu.add_cascade(label="Theme", menu = file)
    file.add_command(label="light",compound="left",command=lambda:theme(0))
    file.add_command(label="dark",compound="left",command=lambda:theme(1))
    file.add_command(label="Exit",command=lambda:theme("exit"))
    root.config(menu=menu)
def theme(t):
    if t==0:
        root.config(bg=white)
        label1.config(bg=white)
        label.config(bg=white,fg=black)
        draw.config(bg=white,fg=black)
        loss.config(bg=white,fg=black)
        win.config(bg=white,fg=black)
    elif t==1:
        root.config(bg=black)
        label1.config(bg=black)        
        label.config(bg=black,fg=white)
        draw.config(bg=black,fg=white)
        loss.config(bg=black,fg=white)
        win.config(bg=black,fg=white)
    elif t=="exit":
        a = str(messagebox.askyesno(title="Exit", message="Do you want to exit ?"))
        if a=="True":
            root.destroy()
def counter(n):
    global won,lost,drawed
    if n=="draw":
        drawed = drawed + 1
        draw.config(text=f"Draw = {drawed}",font=("style",20))
    elif n=="win":
        won = won + 1
        win.config(text=f"Won = {won}")
    elif n=="loss":
        lost = lost + 1
        loss.config(text=f"Lost = {lost}")
def pressed(num):
    com_choice = choice(["rock", "paper", "scissor"])
    label.config(text= f"computer choose: {com_choice}",font=("style",20))
    if num == "rock" and com_choice == "rock":
        label1.config(text="Game Draw",fg="red",font=("style",20))
        counter("draw")
    elif num == "paper" and com_choice == "paper":
        label1.config(text="Game Draw",fg="red",font=("style",20))
        counter("draw")
    elif num == "scissor" and com_choice == "scissor":
        label1.config(text="Game Draw",fg="red",font=("style",20))
        counter("draw")
    elif num == "rock" and com_choice =="paper":
        label1.config(text= "Computer won the game...",fg="blue",font=("style",20))
        counter("loss")
    elif num == "rock" and com_choice =="scissor":
        label1.config(text= "You won the game...",fg="green",font=("style",20))
        counter("win")
    elif num == "paper" and com_choice =="rock":
        label1.config(text= "You won the game...",fg="green",font=("style",20))
        counter("win")
    elif num == "paper" and com_choice =="scissor":
        label1.config(text= "Computer won the game...",fg="blue",font=("style",20))
        counter("loss")
    elif num == "scissor" and com_choice =="rock":
        label1.config(text= "Computer won the game...",fg="blue",font=("style",20))
        counter("loss")
    elif num == "scissor" and com_choice =="paper":
        label1.config(text= "You won the game...",fg="green",font=("style",20))
        counter("win")
    else:
        label1.config(text= "Wrong choice",fg="red",font=("style",20))

if __name__ == "__main__":
    black = "black"
    white = "white"

    global won,lost,drawed
    won = 0
    lost = 0
    drawed = 0

    root = Tk()
    root.title("Rock Paper Scissor")
    root.geometry("390x330")
    root.config(bg=black)
    menu()

    scissor_raw = Image.open("scissor.jpg").resize((100,100),Image.ANTIALIAS)
    scissor_img = ImageTk.PhotoImage(scissor_raw)
    paper_raw = Image.open("paper.jpg").resize((100,100),Image.ANTIALIAS)
    paper_img = ImageTk.PhotoImage(paper_raw)
    stone_raw = Image.open("rock.jpg").resize((100,100),Image.ANTIALIAS)
    stone_img = ImageTk.PhotoImage(stone_raw)

    label = Label(root,text=' ',height=2,bg="black",fg="white")
    label.grid(row=0,column=0,columnspan=3)

    button1 = Button(root,text='',width=100,height=100,image=stone_img, command=lambda:pressed("rock"))
    button1.grid(row=1, column=0,padx=2)

    button2 = Button(root,text='',width=100,height=100,image=paper_img, command=lambda:pressed("paper"))
    button2.grid(row=1 , column=1,padx=2)

    button3 = Button(root,text='',width=100,height=100,image=scissor_img, command=lambda:pressed("scissor"))
    button3.grid(row=1 , column=2,padx=2)

    label1 = Label(root,text=' ',height=3,bg="black")
    label1.grid(row=2,column=0,columnspan=3)

    win = Label(root, text=f" Won = {won}",font=("style",20),bg="black",fg="white")
    win.grid(row=3,column=0,padx=2)

    loss = Label(root, text=f"Lost = {lost}",font=("style",20),bg="black",fg="white")
    loss.grid(row=3,column=1,padx=2)

    draw = Label(root, text=f"Draw = {drawed}",font=("style",20),bg="black",fg="white")
    draw.grid(row=3,column=2,padx=2)

    root.mainloop()