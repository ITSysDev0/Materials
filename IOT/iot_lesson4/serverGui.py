import tkinter  
import socket   
from threading import Thread    
import RPi.GPIO as GPIO 

IP = '192.168.50.10'
PORT = 50000
BUFFER_SIZE = 1024

root=tkinter.Tk()
root.title("Server") 
root.geometry("270x75")

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

def statusBox(text,background):
    Status_Label = tkinter.Label(root,text=text,relief="sunken",font=('40'),width=22,heigh=2,bg=background)  #Display for Online Connection Status
    Status_Label.place(x=20,y=20)
    
    if Status_Label['text']=='Not Active':
        GPIO.output(27,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
    
#Button Function
def status_on():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
        s.bind((IP, PORT))  
        s.listen() 
        print("Server is on. Waiting for client response...") 

        while True:
            (connection,client) = s.accept()    
            try:
                print('LED ON', client)   
                receiveData = connection.recv(BUFFER_SIZE) 

                if(int(receiveData)==1):   
                    print("LED ON")    
                    GPIO.output(27,GPIO.HIGH)
                    GPIO.output(17,GPIO.LOW) 
                    statusBox("LED ON","limegreen")

                else:
                    print('LED OFF')
                    GPIO.output(27,GPIO.LOW)
                    GPIO.output(17,GPIO.HIGH)
                    statusBox("LED OFF","red")

            finally:
                    connection.close()

statusBox("Not Active","lightgrey")

t1=Thread(target=status_on) 
t1.start()

root.mainloop()
