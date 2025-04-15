class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""

def ingrese_numero():
    entrada = input ("Ingrese un numero: ")
    try: 
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El numero debe ser positivo. \n")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un numero válido. \n")