from tkinter import *
from tkinter import messagebox
## 함수 선언 부분 ##
def myFunc() :
    if chk.get() == 0 : # chk.get( ) 함수로 체크박스에 설정된 값을 가져온다.
        messagebox.showinfo("", "체크버튼이 OFF 입니다.")
    else :
        messagebox.showinfo("", "체크버튼이 ON 입니다.")

## 메인 코드 부분 ##
root = Tk()
root.geometry('300x100')
chk = IntVar() # 정수형 타입의 변수 생성
cb1 = Checkbutton(root, text = "클릭하세요", variable = chk, command = myFunc)
# 체크박스를 선택하면 chk에 1이 할당되고 함수를 호출하며, 해지하면 chk에 0이 할당되고 함수 호출
cb1.pack()
root.mainloop()