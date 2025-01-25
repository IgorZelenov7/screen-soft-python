from pyautogui import screenshot
from tkinter import *
from tkinter import messagebox


def screen():
    img = screenshot() # Создаем скриншот
    img.save(r'screen.png')  # Сохраняем скриншот
    messagebox.showinfo('Alert', 'Screen Ready')  # Показываем сообщение


# Графический интерфейс
root = Tk()
root.title('Screen Soft')
root.geometry('300x70')
root.resizable(width=False, height=False)

# Кнопка для создания скриншота
btn = Button(root, text='Screen', font=('Comic Sans MS', 15, 'bold'), command=screen)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()