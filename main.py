from pyautogui import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Screen Soft')
root.geometry('300x70')
root.resizable(width=False, height=False)


btn = Button(root, text='Screen', font=('Comic Sans MS', 15, 'bold'))
btn.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()