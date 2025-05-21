from tkinter import *
window = Tk()

window.title("이미지 표시하기")
photo = PhotoImage(file="gif/dog.gif")
lable1 = Label(window, image=photo)
lable1.pack()
window,mainloop()