import tkinter as tk
from tkinter import ttk
from Action import Action
from State import State
from tkinter import messagebox

class CreateTape:
    
    def __init__(self, tm) -> None:
        self.tm = tm
        
        self.interface = tk.Tk()
        self.interface.geometry("450x200")
        self.interface.title("Crear cinta inicial")
        
        self.textTape = tk.Label(self.interface, text="Cinta de inicio", font=("Arial", 12))
        self.inputTape = tk.Entry(self.interface, width=50)
        
        self.textHead = tk.Label(self.interface, text="Posicion inicial de la cabeza", font=("Arial", 12))
        self.inputHead = tk.Entry(self.interface, width=50)
        
        self.button = tk.Button(self.interface, text="Aceptar")
        self.back = tk.Button(self.interface, text="Regresar")
        


    def runWindow(self):
        
        def backToMain():
            self.interface.destroy()
            
        def createTape():
            string = self.inputTape.get()
            tape = [int(c) for c in string if c in ['0', '1']]
            if len(tape) == 0 or int(self.inputHead.get()) not in range(0, len(tape)):
                messagebox.showerror("Error", "Ingrese datos validos")
                
            else:                            
                self.tm.tape = tape
                self.tm.headStart = int(self.inputHead.get())
                print(self.tm.tape)
                print(self.tm.headStart)
                self.interface.destroy()
 
        
        self.textTape.pack(pady=(10, 0))
        self.inputTape.pack(pady=(10, 15))
        self.textHead.pack(pady=(15, 10))
        self.inputHead.pack()
        self.back.place(x=110, y=160)
        self.button.place(x=280, y=160)
        
        self.button.config(command=createTape)
        self.back.config(command=backToMain)
        
        
        self.interface.mainloop()
    






