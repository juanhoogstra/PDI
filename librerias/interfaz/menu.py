import tkinter as tk
from subprocess import getoutput
from configparser import ConfigParser
import os
import sys

configPar = ConfigParser()
path = os.path.dirname(os.path.abspath(sys.argv[0]))
configPath = os.path.join(path, "config.ini")
configPar.read(configPath)

class Menu(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.title("Comandos e información de la red")
        self.geometry("900x600")
        self.config(bg="#007F7F")

        entrada=tk.StringVar()

        self.lbl = tk.Label(self, text="Comandos e información de la red", bg="#007F7F", fg="white", font="Helvetica 16")
        self.lbl.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.08)

        self.lbl1 = tk.Label(self,  text="Dirección IPv4: ", bg="white", fg="#007F7F", font="Helvetica 12")
        self.lbl1.place(relx=0.05, rely=0.10, relwidth=0.44, relheight=0.08)

        self.lbl2 = tk.Label(self,  text="Mascara de subred: ", bg="white", fg="#007F7F", font="Helvetica 12")
        self.lbl2.place(relx=0.05, rely=0.20, relwidth=0.44, relheight=0.08)

        self.lbl3 = tk.Label(self,  text="Puerta de enlace predeterminada", bg="white", fg="#007F7F", font="Helvetica 12")
        self.lbl3.place(relx=0.51, rely=0.10, relwidth=0.44, relheight=0.08)

        self.lbl4 = tk.Label(self,  text="Servidores DNS:", bg="white", fg="#007F7F", font="Helvetica 12")
        self.lbl4.place(relx=0.51, rely=0.20, relwidth=0.44, relheight=0.08)

        self.lbx = tk.Listbox(self, bg="black", fg="white")
        self.lbx.place(relx=0.05, rely=0.3, relwidth=0.55, relheight=0.5)
        
        ipData = getoutput(['ipconfig', '/all'])
        
        info1 = ipData.splitlines()[17]
        self.lbl1.config(text=info1)
        
        info2 = ipData.splitlines()[21]
        self.lbl2.config(text=info2)
        
        info3 = ipData.splitlines()[18]
        self.lbl3.config(text=info3)
        
        info4 = ipData.splitlines()[25]
        self.lbl4.config(text=info4)

        for i in ipData.splitlines():
            self.lbx.insert(tk.END, i)

        self.btn1 = tk.Button(self, text=configPar.get("BTN1", "label"), bg="black", fg="white", command=lambda:self.entrada1(entrada))
        self.btn1.place(relx=0.65, rely=0.3, relwidth=0.3, relheight=0.08)
        
        self.btn2 = tk.Button(self, text=configPar.get("BTN2", "label"), bg="black", fg="white", command=lambda:self.entrada2(entrada))
        self.btn2.place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.08)

        self.btn3 = tk.Button(self, text=configPar.get("BTN3", "label"), bg="black", fg="white", command=lambda:self.entrada3(entrada))
        self.btn3.place(relx=0.65, rely=0.5, relwidth=0.3, relheight=0.08)

        self.btn4 = tk.Button(self, text=configPar.get("BTN4", "label"), bg="black", fg="white", command=lambda:self.entrada4(entrada))
        self.btn4.place(relx=0.65, rely=0.6, relwidth=0.3, relheight=0.08)
        
        self.btn5 = tk.Button(self, text="Limpiar consola", bg="#007F9F", fg="white", command=lambda:self.limpiar())
        self.btn5.place(relx=0.65, rely=0.7, relwidth=0.3, relheight=0.08)

        self.txt = tk.Entry(self, textvariable=entrada, font="Helvetica 16", bg="white", fg="black")
        self.txt.place(relx=0.05, rely=0.87, relwidth=0.55, relheight=0.08)

        self.btnEnter = tk.Button(self, text="Enter", bg="#00AF7F", fg="white", font=18, command=lambda:self.enter(entrada))
        self.btnEnter.place(relx=0.65, rely=0.87, relwidth=0.3, relheight=0.08)

    def entrada1(self, entrada):
        newData = getoutput(configPar.get("BTN1", "command"))
        self.insertar(entrada, newData)
    
    def entrada2(self, entrada):
        newData = getoutput(configPar.get("BTN2", "command"))
        self.insertar(entrada, newData)
    
    def entrada3(self, entrada):
        newData = getoutput(configPar.get("BTN3", "command"))
        self.insertar(entrada, newData)
    
    def entrada4(self, entrada):
        newData = getoutput(configPar.get("BTN4", "command"))
        self.insertar(entrada, newData)

    def enter(self, entrada): 
        newData = getoutput(entrada.get().split(" "))
        self.insertar(entrada, newData)

    def limpiar(self):
        self.lbx.delete(1, tk.END)

    def insertar(self, entrada, newData):
        self.lbx.insert(tk.END, "------------------------------------------------------------\n")
        for i in newData.splitlines():
            self.lbx.insert(tk.END, i)
        entrada.set('')

    def render(self):
        self.mainloop()

# /*
# IPv4Address
# MAscara de subred
# Puerta de enlace predeterminada
# Servidores DNS

# ipconfig /flushdns
# */