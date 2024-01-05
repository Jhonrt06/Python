from math import pi
class Cilindro:
    
    #Constructor
    
    def __init__(self,radio,altura,color='blue'):
        self.radio=radio
        self.altura=altura
        self.color=color
        
    # metodo de instancia    
    def perimetro(self):
        return 2*self.radio + self.altura 
    
    def area_base(self):
        return pi*self.radio**2
    def volumen(self):
        return pi*self.radio**2 * self.altura
    
    def __str__(self):
        return(f'Radio:{self.radio}\nAltura: {self.altura}\nColor: {self.color}')
    
    #metodo estatico
    
    @staticmethod #decorador
    def are_equal_height(cilindro1,cilindro2):
        if cilindro1.altura==cilindro2.altura:
            return True
        else:
            return False
    
    @classmethod #decorador
    def tank_cilindrico(cls):
        radio=3
        altura=5
        return cls(radio,altura)

        
        
    

if __name__=="__main__":
    
    cil1=Cilindro(2,4,'azul')
    cil2=Cilindro(3,5,'verde')
    tanque=Cilindro.tank_cilindrico()
  
    print(f' Son los cilindros iguales? = {Cilindro.are_equal_height(cil1,cil2)}')
    
    
    print(f'El perimetro del cilindro es {cil1.perimetro()}')

    print(f'El area del cilindro es {cil1.area_base()}')
    print(f'El volumen del cilindro es {cil1.volumen()}')
    print(f'Mi tanque generico es: \n{tanque}')

    
      
