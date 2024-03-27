import tkinter  
import socket  

IP = '192.168.50.10'   
PORT = 50000
BUFFER_SIZE = 1024

root=tkinter.Tk()
root.title("Client")
root.geometry("300x90") 

def socketSign(sign):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((IP, PORT))
    signal = sign
    s.send(signal.encode())
    return sign
    
def on_stat():

    sg = socketSign('1')
    
    if sg=='1':
        offBtn.configure(text='OFF',bg = 'lightgrey')
        onBtn.configure(text='ON',bg = 'limegreen')
    else:
        onBtn.configure(text='OFF',bg = 'lightgrey')

def off_stat():
    
    sg = socketSign('0')
    
    if sg=='0':
        offBtn.configure(text='OFF',bg = 'red')
        onBtn.configure(text='ON',bg = 'lightgrey')
    else:
        offBtn.configure(text='OFF',bg = 'lightgrey')

#ON Button
onBtn = tkinter.Button(root,text='ON',font=('30'),width=10,heigh=2,bg='lightgrey',command = on_stat)  
onBtn.place(x=20,y=20) 
offBtn = tkinter.Button(root,text='OFF',font=('30'),width=10,heigh=2,bg='lightgrey',command = off_stat) 
offBtn.place(x=150,y=20) 

root.mainloop()
