class Action:
    
    """
    Constructor de la clase Accion
        -value: Representa el valor que se va a escribir sobre la cinta (str)
        -action: Representa la accion que se realizara (mover a izquierda o mover a derecha) (str)
        -newState: Representa el nuevo estado al que se cambiara despues de realizar la accion (str)
    """
    def __init__(self, value, action, newState) -> None:
        self.value = value
        self.action = action
        self.newState = newState
        
    