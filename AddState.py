import tkinter as tk
from tkinter import ttk
from Action import Action
from State import State

class AddState:
    
    def __init__(self, tm) -> None:
        self.tm = tm
        self.optionAction = ["L", "R", "Fin"]
        self.optionValue = [0, 1, "Fin"]
        self.optionNewState = []
        for state in self.tm.states:
            self.optionNewState.append(state.name)
        
        
        self.interface = tk.Tk()
        self.inputName = tk.Entry(self.interface)
        self.inputValue0 = ttk.Combobox(self.interface, values=self.optionValue) 
        self.inputAction0 = ttk.Combobox(self.interface, values=self.optionAction)
        self.inputNewState0 = ttk.Combobox(self.interface, values=self.optionNewState)
        self.inputValue1 = ttk.Combobox(self.interface, values=self.optionValue)
        self.inputAction1 = ttk.Combobox(self.interface, values=self.optionAction)
        self.inputNewState1 = ttk.Combobox(self.interface, values=self.optionNewState)

    
    def runWindow(self):
        
        def showState(event):               
            stateName = self.inputName.get()                      
            if stateName != "" and stateName not in self.optionNewState:
                if len(self.optionNewState) != 0:
                    self.optionNewState.pop(len(self.optionNewState)-1)                
                self.optionNewState.append(stateName)
                self.inputNewState0["values"] = self.optionNewState
                self.inputNewState1["values"] = self.optionNewState 
                
        
        def showMainInterface():            
            if(
                self.inputValue0.get() == "Fin" or self.inputAction0.get() == "Fin" or self.inputNewState0.get() == "Fin"
            ):
                action0 = Action(
                    None,
                    None,
                    None
                )
                
                action1 = Action(
                    self.inputValue1.get(),
                    self.inputAction1.get(),
                    self.inputNewState1.get()
                )
                
                state = State(self.inputName.get(), action0, action1)            

                self.tm.states.append(state)
            elif(
                self.inputValue1.get() == "Fin" or self.inputAction1.get() == "Fin" or self.inputNewState1.get() == "Fin"
            ):
                action0 = Action(
                    int(self.inputValue0.get()),
                    self.inputAction0.get(),
                    self.inputNewState0.get()
                )
                
                action1 = Action(
                    None,
                    None,
                    None
                )
                
                state = State(self.inputName.get(), action0, action1)            

                self.tm.states.append(state)
            elif (
                self.inputValue0.get() == "" or self.inputAction0.get() == "" or self.inputNewState0.get() == "" or
                self.inputValue1.get() == "" or self.inputAction1.get() == "" or self.inputNewState1.get() == "" or
                self.inputName.get() == ""
            ):
                print("Ingrese todos los campos del formulario")
                
            else:                            
                action0 = Action(
                    self.inputValue0.get(),
                    self.inputAction0.get(),
                    self.inputNewState0.get()
                )
                
                action1 = Action(
                    self.inputValue1.get(),
                    self.inputAction1.get(),
                    self.inputNewState1.get()
                )
                
                if self.tm.getState(self.inputName.get()) == None:
                    state = State(self.inputName.get(), action0, action1)            

                    self.tm.states.append(state)
                else:
                    print("Estado ya existente")
            self.interface.destroy()

                
        self.interface.geometry("600x400")
        self.interface.title("Agregar Estado")

        for state in self.tm.states:
            self.optionNewState.append(state.name) 

        labelName = tk.Label(self.interface, text="Nombre del estado", font=("Arial", 12))
        labelName.place(x=230, y=20)        
        self.inputName.place(x=230, y=50, width=135)
        self.inputName.bind("<FocusIn>", showState)
        self.inputName.bind("<FocusOut>", showState)

        
        labelValue0 = tk.Label(self.interface, text="Valor a escribir cuando lee 0", font=("Arial", 8))
        labelValue0.place(x=30, y=120)        
        self.inputValue0.place(x=30, y=140, width=135)        
        
        labelAction0 = tk.Label(self.interface, text="A donde mover cuando lee 0", font=("Arial", 8))
        labelAction0.place(x=230, y=120)        
        self.inputAction0.place(x=230, y=140, width=135)
        
        labelNewState0 = tk.Label(self.interface, text="Cambiar estado cuando lee 0", font=("Arial", 8))
        labelNewState0.place(x=430, y=120)        
        self.inputNewState0.bind("<FocusIn>", showState)
        self.inputNewState0.place(x=430, y=140, width=135)
        
        labelValue1 = tk.Label(self.interface, text="Valor a escribir cuando lee 1", font=("Arial", 8))
        labelValue1.place(x=30, y=210)        
        self.inputValue1.place(x=30, y=230, width=135)
        
        labelAction1 = tk.Label(self.interface, text="A donde mover cuando lee 1", font=("Arial", 8))
        labelAction1.place(x=230, y=210)        
        self.inputAction1.place(x=230, y=230, width=135)
        
        labelNewState1 = tk.Label(self.interface, text="Cambiar estado cuando lee 1", font=("Arial", 8))
        labelNewState1.place(x=430, y=210) 
        self.inputNewState1.bind("<FocusIn>", showState)       
        self.inputNewState1.place(x=430, y=230, width=135)

        button = tk.Button(self.interface, text="Agregar Estado")
        button.place(x=250, y=300)
        button.config(command=showMainInterface)
        
        def backToMain():
            self.interface.destroy()
        
        
        back = tk.Button(self.interface, text="Regresar")
        back.place(x=30, y=350)
        back.config(command=backToMain)
        
        
        
        self.interface.mainloop()


    
    