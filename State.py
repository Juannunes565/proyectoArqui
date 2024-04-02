class State:
    
    """
    Constructor de la clase Estado
        -name: Es el nombre del estado, ejemplo: q0, q1... qN (str)
        -action0: Es la accion que se realizara cuando se lee en la cinta el valor "0" (Action)
        -action1: Es la accion que se realizara cuando se lee en la cinta el valor "1" (Action)
    
        Tanto action0 como action1 son Objetos "Action"
    """
    def __init__(self, name, action0, action1):       
        self.name = name         
        self.action0 = action0        
        self.action1 = action1        
                
        
    
            
        
    