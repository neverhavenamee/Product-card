from tkinter import *
from googletrans import Translator
from PIL import Image, ImageTk
import os
root = Tk()
def setupwindow():
    root.geometry("400x600")
    root.title('Google Translate')
    #icon
    path_directory = os.path.dirname(__file__)#lấy đường dẫn của file hiện tại(file đang code)
    root.iconbitmap(os.path.join(path_directory, 'logo.ico'))
    #giới hạn thu phóng cửa sổ
    root.minsize(400, 600)
    #background
    path_directory = os.path.dirname(__file__)#lấy đường dẫn của file hiện tại(file đang code)
    load = Image.open(os.path.join(path_directory, 'galaxy.png'))
    img = ImageTk.PhotoImage(load)
    panel = Label(root, image = img)
    panel.image = img
    panel.place(x=0,y=0)

    #cố định kích thước cửa sổ
    root.resizable(False, False)
setupwindow()
label = Label(root, text='GOOGLE TRANSLATE', bg = '#001733',fg='grey', bd=0)
label.config(font=("Transformers Movie", 30))
label.pack(pady=10)
box=Text(root, width=28, height=8, font=("ROBOTO", 16), bg='#DDDDDD')
box.pack(pady=20)
box1=Text(root, width=28, height=8, font=("ROBOTO", 16), bg='#DDDDDD')
box1.pack(pady=50)
button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)
def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t=Translator()
    a=t.translate(INPUT, src="vi",dest="en")
    b=a.text
    box1.insert(END,b)
clear_button=Button(button_frame, text='Clear text', font=('Arial', 10, 'bold'), bg='black', fg='white', command=clear)
clear_button.place(x=50,y=310)
trans_button=Button(button_frame, text='Translate', font=('Arial', 10, 'bold'), bg='black', fg='white', command=translate)
trans_button.place(x=270,y=310)
root.mainloop()