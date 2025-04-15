class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    
    

def ingrese_numero():
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)  
        if numero < 0:
            raise NumeroDebeSerPositivo("La entrada debe ser un numero positivo")  
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido") 