def divide(x,y):
    try:
        z= x/y
        if z< 0:
            raise ValueError("Sin numeros negativos")
    except (ZeroDivisionError):
        print("revisar funcion de dividir")
        v=1/"a"
    except ValueError as ve:
        print(ve)
    else:
        return z
    finally:
        print("excecuting finally clause")
    
         


resultado=divide(12,-1)
print(resultado) 
