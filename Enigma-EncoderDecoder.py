##importing mmodules

from tkinter import *
import base64

#initialize window
tkinit = Tk()
tkinit.geometry('600x400')
tkinit.resizable(0,0)

#title of the window
tkinit.title("Enigma by Akshat Pareek")



#label

Label(tkinit, text ='Enigma', font = 'Times 20').pack()
Label(tkinit, text ='Made with ❤️by Akshat Pareek', font = 'Times 15 bold italic').pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    tkinit.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Message
Label(tkinit, font= 'arial 12 bold', text='Message:').place(x= 60,y=60)
Entry(tkinit, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(tkinit, font = 'arial 12 bold', text ='Key: ').place(x=60, y = 90)
Entry(tkinit, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(tkinit, font = 'arial 12 bold', text ='Mode(\'e\'-encode, \'d\'-decode): ').place(x=60, y = 120)
Entry(tkinit, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)



#result
Entry(tkinit, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

######result button
Button(tkinit, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 155)


#reset button
Button(tkinit, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 250)

#exit button
Button(tkinit, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=250, y = 250)
tkinit.mainloop()
