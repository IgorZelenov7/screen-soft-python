from pyautogui import screenshot
from tkinter import *
from tkinter import messagebox
from datetime import datetime


def screen():
    # Генерация уникального имени файла с текущей датой и временем
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screen_{timestamp}.png'

    # Создание скриншота
    img = screenshot()
    img.save(filename)
    messagebox.showinfo('Ready', f'Screenshot saved as {filename}')


# Графический интерфейс
root = Tk()
root.title('Screen Soft')
root.geometry('300x700')
root.resizable(width=False, height=False)

# Кнопка для создания скриншота
btn = Button(root, text='Screen', font=('Ubuntu Regular 400', 15, 'bold'), command=screen)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()