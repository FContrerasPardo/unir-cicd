import math
from app.util import validate_types, validate_user_permissions, validate_non_negative,validate_log_arguments

class Calculator:
    """
    Una clase que representa una calculadora simple.

    Métodos:
    add(x, y) -- Suma dos números.
    substract(x, y) -- Resta dos números.
    multiply(x, y) -- Multiplica dos números, con verificación de permisos.
    divide(x, y) -- Divide dos números, con manejo de división por cero.
    power(x, y) -- Eleva un número a la potencia de otro.
    sqrt(x) -- Calcula la raíz cuadrada de un número.
    log(x, base) -- Calcula el logaritmo de un número en una base dada.
    """

    @validate_types
    def add(self, x, y):
        """
        Suma dos números.

        Parámetros:
        x -- Primer número (int o float)
        y -- Segundo número (int o float)

        Retorna:
        La suma de x y y (int o float)
        """
        return x + y
    
    @validate_types
    def substract(self, x, y):
        """
        Resta el segundo número del primero.

        Parámetros:
        x -- Primer número (int o float)
        y -- Segundo número (int o float)

        Retorna:
        La resta de x y y (int o float)
        """
        return x - y

    @validate_types
    @validate_user_permissions
    def multiply(self, x, y):
        """
        Multiplica dos números. Requiere verificación de permisos del usuario.

        Parámetros:
        x -- Primer número (int o float)
        y -- Segundo número (int o float)

        Retorna:
        El producto de x y y (int o float)

        Excepciones:
        InvalidPermissionsError -- Si el usuario no tiene permisos
        """
        return x * y

    @validate_types
    def divide(self, x, y):
        """
        Divide el primer número por el segundo. Maneja división por cero.

        Parámetros:
        x -- Numerador (int o float)
        y -- Denominador (int o float)

        Retorna:
        El cociente de x y y (int o float)

        Excepciones:
        ZeroDivisionError -- Si y es 0
        """
        if y == 0:
            raise ZeroDivisionError("División por cero no es posible")
        return x / y

    @validate_types
    def power(self, x, y):
        """
        Eleva un número a la potencia de otro.

        Parámetros:
        x -- Base (int o float)
        y -- Exponente (int o float)

        Retorna:
        x elevado a la potencia de y (int o float)
        """
        return math.pow(x, y)
        
    @validate_types
    @validate_non_negative
    def sqrt(self, x):
        """
        Calcula la raíz cuadrada de un número. 

        Parámetros:
        x -- Número (int o float)

        Retorna:
        La raíz cuadrada de x (float)
        """
        return math.sqrt(x)
        
    @validate_types
    @validate_log_arguments
    def log(self, x, base):
        """
        Calcula el logaritmo de un número en una base dada.

        Parámetros:
        x -- Número (int o float)
        base -- Base del logaritmo (int o float)

        Retorna:
        El logaritmo de x en la base especificada (float)
        """
        return math.log(x, base)

# Código para probar la clase si se ejecuta directamente este archivo
if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(2, 2)
    print(f"Resultado: {result}")
