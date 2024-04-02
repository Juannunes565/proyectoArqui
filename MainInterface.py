import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from AddState import AddState
from TuringMachine import TuringMachine
from State import State
from Action import Action
from CreateTape import CreateTape

class MainInterface:
    
    def __init__(self, tape=None, headStart=None, tm=None) -> None:
        
        if tm is None:            
            if isinstance(tape, int):
                self.tm = TuringMachine([0]*tape, headStart)
            else:
                self.tm = TuringMachine(tape, headStart)
                
        else:
            self.tm = tm
        
        
    def runWindow(self):        
        interface = tk.Tk()
        interface.geometry("600x400")
        interface.title("Maquina de turing")

        label = tk.Label(interface, text="Cinta Inicial", font=("Arial", 12))
        label.pack(pady=(10,10))

        startTape = tk.Text(interface, height=1)
        startTape.pack()
        startTape.tag_config("color", foreground="red")        
        startTape.insert(tk.END, self.tm.tape[0:self.tm.headStart])
        startTape.insert(tk.END, " ")
        startTape.insert(tk.END, self.tm.tape[self.tm.headStart], "color")
        startTape.insert(tk.END, " ")
        startTape.insert(tk.END, self.tm.tape[self.tm.headStart+1:])
        startTape.config(state="disabled")
        
        def toCreateTape():
            interface.destroy()
            createTape = CreateTape(self.tm)
            createTape.runWindow()
            
            main = MainInterface(tm=createTape.tm)
            main.runWindow()
        
        setTape = tk.Button(interface, text="Crear cinta inicial")
        setTape.place(x=150, y=80)
        setTape.config(command=toCreateTape)

        button = tk.Button(interface, text="Agregar Estado")
        button.place(x=343, y=80)
        

        pi = tk.Label(interface, text="Estado de inicio ", font=("Arial", 12))
        pi.pack(pady=(60,10)) 

        
        statesNames = []
        for state in self.tm.states:
            statesNames.append(state.name)
        
        states = ttk.Combobox(interface, values=statesNames)
        states.pack(pady=(0,20))

        start = tk.Button(interface, text="Mostrar resultado")
        start.pack()
        
        result = tk.Label(interface, text="Cinta resultado", font=("Arial", 12))
        result.pack(pady=(40,20))
        
        finalTape = tk.Text(interface, height=1)
        finalTape.pack()
        finalTape.config(state="disabled")

        def showAddState():
            
            interface.destroy()
            addState = AddState(self.tm)
            addState.runWindow()
                        
            main = MainInterface(tm=addState.tm)
            main.runWindow()     
        
        def showFinalTape():
            if states.get() == "":
                messagebox.showerror("Error", "No se puede iniciar sin al menos un estado")                
            else:
                try:                                                    
                    self.tm.runMachine(states.get()) 
                    finalTape.config(state="normal")
                    finalTape.tag_config("color", foreground="red")        
                    finalTape.insert(tk.END, self.tm.tape[0:self.tm.headStart])
                    finalTape.insert(tk.END, " ")
                    finalTape.insert(tk.END, self.tm.tape[self.tm.headStart], "color")
                    finalTape.insert(tk.END, " ")
                    finalTape.insert(tk.END, self.tm.tape[self.tm.headStart+1:])   
                    finalTape.config(state="disabled")                 
                except:
                    messagebox.showerror("Error", "Error en la ejecucion de la maquina de estado")
                     

        button.config(command=showAddState)
        start.config(command=showFinalTape)
        


        

        interface.mainloop()


main = MainInterface([0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], headStart=2)
main.runWindow()