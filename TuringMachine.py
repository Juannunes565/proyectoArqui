import time
from tkinter import messagebox


class TuringMachine: 
    #Constantes
    RIGHT = "R"
    LEFT = "L"
    
    """
    Constructor de la clase Maquina de Turing
        -numOfElements: representa la cantidad de elementos que poseera la cinta, este valor puede ser
        una lista o un entero (list, int)
        ejemplo para lista: [0, 0, 0, 1, 1, 0, 1, 0]
        ejemplo para entero: 4 (Esto da como resultado una lista con 4 ceros: [0, 0, 0, 0])
        -headPosition: representa en donde va a empezar la cabeza (int, default=0)
        
    """
    def __init__(self, numOfelements, headStart=0) -> None:
        
        #Si numOfElements es una lista
        if isinstance(numOfelements, list):
            self.tape = numOfelements
        
        #Si numOfElements es un entero crea una lista con ceros
        elif isinstance(numOfelements, int):            
            self.tape = [0] * numOfelements
            
        self.headStart = headStart
        self.states = []
    
    
    #Metodo para mover a la izquierda       
    def toLeft(self):
        self.headStart -= 1
        if self.headStart <= -1:
            self.tape = ([0]*2) + self.tape
        
    #Metodo para mover a la derecha
    def toRight(self):
        self.headStart += 1
        if self.headStart >= len(self.tape):
            self.tape = self.tape + ([0]*2)
        
    #Metodo para mover el puntero dado un valor    
    def move(self, value):
        if value == self.LEFT:
            self.toLeft()
        
        elif value == self.RIGHT:
            self.toRight()
    
    
    #Metodo para leer en la cinta   
    def read(self):        
        return self.tape[self.headStart]

    #Metodo para escribir en la cinta, solo se puede escribir 0 o 1
    def write(self, value): 
        
        if value is not None:                   
            if(int(value)in [0, 1]):
                self.tape[self.headStart] = int(value)
    
    #Metodo para obtener un estado dado su nombre
    def getState(self, stateName):
        for state in self.states:
            if state.name == stateName:
                return state
        return None
    
    #Metodo para cambiar entre estados
    def transition(self, state):        
        value = self.read()
                           
        if value == 0:
            if isinstance(state, str):
                action = self.getState(state).action0
            else:                
                action = state.action0                
        
        elif value == 1:
            if isinstance(state, str):
                action = self.getState(state).action1
            else:                
                action = state.action1
            
        self.write(action.value)
        self.move(action.action)
        
        return self.getState(action.newState)

    
    #Metodo para hacer funcionar la maquina de estado
    def runMachine(self, initialState):
        
        state = self.transition(initialState)  
        start_time = time.time()          
        while state != None:            
            state = self.transition(state)
            if time.time() - start_time > 3: 
                messagebox.showerror("Bucle infinito", "Se ha detectado un bucle infinito")
                break               
        
        
            
        
    
    
