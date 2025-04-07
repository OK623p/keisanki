from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def answer(sisoku):
    input_line = entry.get()
    siki = input_line.split(" ")
    if len(siki) != 2:
        messagebox.showinfo("すみません","まだそこまでの技術がありません")
        return
    x = int(siki[0])
    y = int(siki[1])
    ans = 0
    if sisoku == "+":
        ans = x + y
    elif sisoku == "-":
        ans = x - y
    elif sisoku == "*":
        ans = x * y
    elif sisoku == "/":
        if y == 0 :
            messagebox.showinfo("エラー","ゼロ除算エラー")
            return
        else:
            ans = x / y
        if x % y == 0:
            ans = int(ans)
    messagebox.showinfo("解","答えは"+str(ans)+"です")

root = Tk()
root.geometry("300x125")
root.title("簡易計算機")


label = ttk.Label(
    root,
    text = "半角区切りでX□Yみたいな二個の計算だけです。",
    padding = (5,20),
    
)
entry = ttk.Entry(root,justify="center")
"""消すのめんどいからなしで
entry.insert(END,"X Y")"""
plus_button = ttk.Button(root,text = "+",width = 5,command =lambda: answer("+"))
minus_button = ttk.Button(root,text = "-",width = 5,command =lambda: answer("-"))
multiple_button = ttk.Button(root,text = "×",width = 5,command =lambda: answer("*"))
divide_button = ttk.Button(root,text = "÷",width = 5,command =lambda: answer("/"))

#レイアウト
label.place(x = 30, y = 0)
entry.place(x = 85, y = 50)
plus_button.place(x = 50, y= 75)
minus_button.place(x = 100, y= 75)
multiple_button.place(x = 150, y= 75)
divide_button.place(x = 200, y= 75)
#ウィンドウ表示
root.mainloop()