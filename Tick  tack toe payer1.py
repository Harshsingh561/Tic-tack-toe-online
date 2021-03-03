from tkinter import *
from threading import *
from tkinter import messagebox
import socket
s = socket.socket()
host = input('Enter the name of the server to connect: ')
s.connect((host, 9999))
print("Connected")
class tic_tac_toe:
    def __init__(self):
        self.b1=False
        self.b2=False
        self.b3=False
        self.b4=False
        self.b5=False
        self.b6=False
        self.b7=False
        self.b8=False
        self.b9=False
        self.p1=False
        self.p2=False
        self.p3=False
        self.p4=False
        self.p5=False
        self.p6=False
        self.p7=False
        self.p8=False
        self.p9=False
        self.wi = False
        self.cur_msg = None
        self.exit=False
    def recv(self):
        while self.cur_msg!='Winner':
            msg = s.recv(1024).decode()
            self.cur_msg=msg
            if self.cur_msg=='btn1':
                    btn1.config(text='X')
                    btn1.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn2':
                    btn2.config(text='X')
                    btn2.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn3':
                    btn3.config(text='X')
                    btn3.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn4':
                    btn4.config(text='X')
                    btn4.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn5':
                    btn5.config(text='X')
                    btn5.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn6':
                    btn6.config(text='X')
                    btn6.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn7':
                btn7.config(text='X')
                btn7.config(state='disable')
                btnp1.config(state='normal')
                btnp2.config(state='disable')
            elif self.cur_msg=='btn8':
                    btn8.config(text='X')
                    btn8.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='btn9':
                    btn9.config(text='X')
                    btn9.config(state='disable')
                    btnp1.config(state='normal')
                    btnp2.config(state='disable')
            elif self.cur_msg=='Reset':
                self.cur_msg=None
                self.resty()
            if self.exit:
                break
        else:
            pass
    def text(self):
        btn1.config(text='O')
        self.b1 = True
        btn1.config(state='disable')
        s.send('btn1'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text2(self):
        btn2.config(text='O')
        self.b2 = True
        btn2.config(state='disable')
        s.send('btn2'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text3(self):
        btn3.config(text='O')
        self.b3=True

        btn3.config(state='disable')
        s.send('btn3'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text4(self):
        btn4.config(text='O')
        self.b4=True

        btn4.config(state='disable')
        s.send('btn4'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text5(self):
        btn5.config(text='O')
        self.b5=True

        btn5.config(state='disable')
        s.send('btn5'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text6(self):
        btn6.config(text='O')
        self.b6 = True

        btn6.config(state='disable')
        s.send('btn6'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text7(self):
        btn7.config(text='O')
        self.b7 = True

        btn7.config(state='disable')
        s.send('btn7'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text8(self):
        btn8.config(text='O')
        self.b8 = True

        btn8.config(state='disable')
        s.send('btn8'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def text9(self):
        btn9.config(text='O')
        self.b9 = True
        btn9.config(state='disable')
        s.send('btn9'.encode())
        btnp2.config(state='normal')
        btnp1.config(state='disable')
    def winner(self):
        lst=[btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
        if btn1['text']==btn2['text']==btn3['text']=='X':
            btn1.config(bg='#F88379')
            btn2.config(bg='#F88379')
            btn3.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn1['text']==btn4['text']==btn7['text']=='X':
            btn1.config(bg='#F88379')
            btn4.config(bg='#F88379')
            btn7.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn7['text']==btn8['text']==btn9['text']=='X':
            btn7.config(bg='#F88379')
            btn8.config(bg='#F88379')
            btn9.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn3['text']==btn6['text']==btn9['text']=='X':
            btn3.config(bg='#F88379')
            btn6.config(bg='#F88379')
            btn9.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn4['text']==btn5['text']==btn6['text']=='X':
            btn4.config(bg='#F88379')
            btn5.config(bg='#F88379')
            btn6.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn2['text']==btn5['text']==btn8['text']=='X':
            btn2.config(bg='#F88379')
            btn5.config(bg='#F88379')
            btn8.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            s.send('Winner'.encode())
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn1['text']==btn5['text']==btn9['text']=='X':
            btn1.config(bg='#F88379')
            btn5.config(bg='#F88379')
            btn9.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            self.wi = True
            s.send('Winner'.encode())
            for i in lst:
                i.config(state='disable')
            return None
        elif btn3['text']==btn5['text']==btn7['text']=='X':
            btn5.config(bg='#F88379')
            btn7.config(bg='#F88379')
            btn3.config(bg='#F88379')
            messagebox.showinfo(title='Winner', message='Player1 Won')
            self.wi=True
            s.send('Winner'.encode())
            for i in lst:
                i.config(state='disable')
            return None
        # Computer
        elif btn1['text']==btn2['text']==btn3['text']=='O':
            btn1.config(bg='#FAA0A0')
            btn2.config(bg='#FAA0A0')
            btn3.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn1['text']==btn4['text']==btn7['text']=='O':
            btn1.config(bg='#FAA0A0')
            btn4.config(bg='#FAA0A0')
            btn7.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn7['text']==btn8['text']==btn9['text']=='O':
            btn7.config(bg='#FAA0A0')
            btn8.config(bg='#FAA0A0')
            btn9.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn3['text']==btn6['text']==btn9['text']=='O':
            btn3.config(bg='#FAA0A0')
            btn6.config(bg='#FAA0A0')
            btn9.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn4['text']==btn5['text']==btn6['text']=='O':
            btn4.config(bg='#FAA0A0')
            btn5.config(bg='#FAA0A0')
            btn6.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn2['text']==btn5['text']==btn8['text']=='O':
            btn2.config(bg='#FAA0A0')
            btn8.config(bg='#FAA0A0')
            btn5.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn1['text']==btn5['text']==btn9['text']=='O':
            btn1.config(bg='#FAA0A0')
            btn5.config(bg='#FAA0A0')
            btn9.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi = True
            for i in lst:
                i.config(state='disable')
            return None
        elif btn3['text']==btn5['text']==btn7['text']=='O':
            btn7.config(bg='#FAA0A0')
            btn3.config(bg='#FAA0A0')
            btn5.config(bg='#FAA0A0')
            s.send('Winner'.encode())
            messagebox.showinfo(title='Winner', message='You Won')
            self.wi=True
            for i in lst:
                i.config(state='disable')
            return None
        btn1.after(1, self.winner)
    def resety(self):
        s.send('Reset'.encode())
        self.b1 = False
        self.b2 = False
        self.b3 = False
        self.b4 = False
        self.b5 = False
        self.b6 = False
        self.b7 = False
        self.b8 = False
        self.b9 = False
        self.p1 = False
        self.p2 = False
        self.p3 = False
        self.p4 = False
        self.p5 = False
        self.p6 = False
        self.p7 = False
        self.p8 = False
        self.p9 = False
        self.wi = False
        self.cur_msg = None
        lst= [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
        for i in lst:
            i.config(bg='tomato')
            i.config(state='normal')
            i.config(text='')
        btnp2.config(state='disable')
        btnp1.config(state='normal')
    def resty(self):
        self.b1 = False
        self.b2 = False
        self.b3 = False
        self.b4 = False
        self.b5 = False
        self.b6 = False
        self.b7 = False
        self.b8 = False
        self.b9 = False
        self.p1 = False
        self.p2 = False
        self.p3 = False
        self.p4 = False
        self.p5 = False
        self.p6 = False
        self.p7 = False
        self.p8 = False
        self.p9 = False
        self.wi = False
        self.cur_msg = None
        lst = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
        for i in lst:
            i.config(bg='tomato')
            i.config(state='normal')
            i.config(text='')
        btnp2.config(state='disable')
        btnp1.config(state='normal')
root = Tk()
root.geometry('610x400')
root.resizable(False, False)
root.attributes('-transparentcolor', root.cget('bg'))
root.title('Tick Tack Toe')
cl = tic_tac_toe()
btn1 = Button(height=8,width=24, command=cl.text, bg='tomato')
btn2 = Button(height=8,width=24, command=cl.text2, bg='tomato')
btn3 = Button(height=8,width=24, command=cl.text3, bg='tomato')
btn4 = Button(height=8,width=24, command=cl.text4, bg='tomato')
btn5 = Button(height=8,width=24, command=cl.text5, bg='tomato')
btn6 = Button(height=8,width=24, command=cl.text6, bg='tomato')
btn7 = Button(height=8,width=24, command=cl.text7, bg='tomato')
btn8 = Button(height=8,width=24, command=cl.text8, bg='tomato')
btn9 = Button(height=8,width=24, command=cl.text9, bg='tomato')
btnp1 = Button(text='Your go: O', bg='blue')
btnp2 = Button(text='Player2: X', state='disable', bg='blue')
reset = Button(text='Reset', bg='blue', command=cl.resety, width=8, height=3)
reset.place(x=540, y=60)
btnp1.place(y=0, x=540)
btnp2.place(y=30, x=540)
btn1.place(x=0, y=0)
btn2.place(x=180, y=0)
btn3.place(x=360, y=0)
btn4.place(x=0, y=135)
btn5.place(x=180, y=135)
btn6.place(x=360, y=135)
btn7.place(x=0, y=270)
btn8.place(x=180, y=270)
btn9.place(x=360, y=270)
thr = Thread(target=cl.winner)
thr.start()
thr2 = Thread(target=cl.recv)
thr2.start()
root.mainloop()
cl.exit=True
