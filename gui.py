from tkinter import *    

   
def flat(array):
       res = "" 
       for item in array:
              res = res + item
       return res       


global input;
global sifre;

input = []
sifre = []
currentState = ["1"]

def handle_1():
       input.append("1")
       label.config(text=flat(input)) 
def handle_2():
       input.append("2")
       label.config(text=flat(input))
def handle_3():
       input.append("3")
       label.config(text=flat(input))
def handle_4():
       input.append("4")
       label.config(text=flat(input))
def handle_5():
       input.append("5")
       label.config(text=flat(input))
def handle_6():
       input.append("6")
       label.config(text=flat(input))
def handle_7():
       input.append("7")
       label.config(text=flat(input))
def handle_8():
       input.append("8")
       label.config(text=flat(input))  
def handle_9():
      input.append("9")
      label.config(text=flat(input))

def btn_sifreOlustur():
       def cb():
              resetErrorMsg()
              btn_sifreGir()
       if not flat(sifre) == "":
              errorMsg.config(text="ZATEN BİR ŞİFRENİZ MEVCUT!",bg="#EA2027")
              errorMsg.grid()
              errorMsg.after(2000,cb)
              return
       currentState.clear()
       currentState.append("1")
       label.config(text="Şifre oluşturun")

def btn_sifreGir():
       currentState.clear()
       currentState.append("0")
       input.clear()
       label.config(text="Şifre girin!")
       
def enter():
      if int(flat(currentState)) == 1:
        def cb():
              resetErrorMsg()
              btn_sifreGir()
      #  label.config(text="Şifre başarıyla oluşturuldu!")
        sifre.append(flat(input))
        input.clear()
        errorMsg.config(text="ŞİFRE BAŞARIYLA OLUŞTURULDU!",bg="#3ae374")  
        errorMsg.grid()
        label.after(2000,cb)
      elif int(flat(currentState)) == 0:
        def cb():
              resetErrorMsg()
              btn_sifreGir()
        if flat(input) == flat(sifre):
              errorMsg.config(text="ŞİFRE DOĞRU!",bg="#3ae374")
              errorMsg.grid()
              errorMsg.after(2000,cb)
        else:
              errorMsg.config(bg="#EA2027",text="ŞİFRE YANLIŞ!")
              errorMsg.grid()
              errorMsg.after(2000,cb)

def delete():
       def cb():
              resetErrorMsg()
              btn_sifreOlustur()
       if flat(sifre) == "":
              errorMsg.config(bg="#EA2027",text="SİLİNEBİLECEK MEVCUT BİR \nŞİFRENİZ BULUNMUYOR!")
              errorMsg.grid()
              errorMsg.after(2000,cb)
       else:
              sifre.clear()
              errorMsg.config(bg="#3ae374",text="ŞİFRENİZ BAŞARIYLA SİLİNDİ!")
              errorMsg.grid()
              errorMsg.after(2000,cb)

def resetErrorMsg():
       errorMsg.config(text="",bg="#EA2027")
       errorMsg.grid_remove()
root = Tk()
root.title("Deneme")
root.geometry("300x300")

root.config(bg="#5352ed")

errorMsg = Label(root,relief=FLAT,text="",bg="#EA2027",height=8,width=38)
errorMsg.grid(padx=850,pady=200)
errorMsg.grid_remove()


label = Label(root,bd=10,relief=GROOVE,width=60,text="Şifre Oluşturun")
label.place(height=100,width=300,x=500,y=20)

button = Button(root,relief=FLAT,bg="#ff7979",text="ENTER",width=40,activebackground="#ff7979",command=enter)
button.place(height=50,width=300,x=500,y=125)

reset = Button(root,relief=FLAT,text="Var olan şifreyi sil",bg="#EA2027",activebackground="#EA2027",command=delete)
reset.place(height=50,width=125,x=925,y=50)

sifre_olustur = Button(root,relief=FLAT,bg="#3ae374",text="ŞİFRE OLUŞTUR",activebackground="#3ae374",command=btn_sifreOlustur)
sifre_olustur.place(height=50,width=125,x=850,y=125)

sifre_gir = Button(root,relief=FLAT,bg="#3ae374",text="ŞİFRE GİR",activebackground="#3ae374",command=btn_sifreGir)
sifre_gir.place(height=50,width=125,x=997,y=125)

button_1 = Button(root,relief=FLAT,bg="white",text="1",command=handle_1)
button_1.place(height=50,width=80,x=500,y=200)

button_2 = Button(root,relief=FLAT,bg="white",text="2",command=handle_2)
button_2.place(height=50,width=80,x=610,y=200)

button_3 = Button(root,relief=FLAT,bg="white",text="3",command=handle_3)
button_3.place(height=50,width=80,x=720,y=200)

button_4 = Button(root,relief=FLAT,bg="white",text="4",command=handle_4)
button_4.place(height=50,width=80,x=500,y=275)

button_5 = Button(root,relief=FLAT,bg="white",text="5",command=handle_5)
button_5.place(height=50,width=80,x=610,y=275)

button_6 = Button(root,relief=FLAT,bg="white",text="6",command=handle_6)
button_6.place(height=50,width=80,x=720,y=275)

button_7 = Button(root,relief=FLAT,bg="white",text="7",command=handle_7)
button_7.place(height=50,width=80,x=500,y=350)

button_8 = Button(root,relief=FLAT,bg="white",text="8",command=handle_8)
button_8.place(height=50,width=80,x=610,y=350)

button_9 = Button(root,relief=FLAT,bg="white",text="9",command=handle_9)
button_9.place(height=50,width=80,x=720,y=350)


root.mainloop()
