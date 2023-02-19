from tkinter import *
from PIL import ImageTk
login = Tk()
login.title('GAME')
login.geometry("600x300")
login.configure(bg = 'Skyblue')
login.resizable(False,False)

bg = ImageTk.PhotoImage(file = 'speaker.png')
bg_image = Label(login,image = bg).place(x=0,y=0,relwidth=1,relheight=1)

username = Label(login,text = "NAME : " ,font = ("arial ", 30 ,"bold")).place(x = 10,y=10)
entry_value = StringVar()
entry_value.set("")
entry = Entry(login,textvar=entry_value,bg="lightblue",font=("arial",30,'bold'))
entry.place(relx=0.3,rely=0.06,relheight=0.12,relwidth=0.6)

def enter():
    print(entry_value.get())
    entry_value.set("")
    login.destroy()

button = Button(login,text = "SUBMIT" , bg = "skyblue" ,font = ("arial",20,'bold'),command = enter).place(x=270,y=125)

login.mainloop()
