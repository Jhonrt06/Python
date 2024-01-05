class Laptop:
    """
    Clase empleada para trabajar con laptops
    """
    # Metodo cosntructor
    
    def __init__(self,marca,procesador, memoria=32,ssd=True):
        
        self.marca= marca
        self.procesador=procesador
        self.memoria= memoria
        self.has_ssd=ssd 
        
        
        
    
    
def main():
    labtob1=Laptop('Dell','Core i7 9600',16, True) #Cree un objeto nuevo    
    
    print(labtob1.marca)
    

if __name__=='__main__':
    main()
    
    