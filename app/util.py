# Utils para la clase Calculator
from functools import wraps

class InvalidPermissionsError(Exception):
    """ Excepción para permisos no válidos """
    pass

def convert_to_number(operand):
    """
    Intenta convertir un operando a número (int o float).
    Lanza una excepción si la conversión no es posible.
    """
    try:
        return float(operand) if "." in operand else int(operand)
    except ValueError:
        raise TypeError("El operador no puede convertirse a número")

def validate_permissions(operation, user):
    """
    Simula la verificación de permisos de un usuario para una operación dada.
    """
    print(f"Verificando permisos de {user} para la operación {operation}")
    return user == "user1"

def validate_types(func):
    """
    Decorador que verifica si todos los argumentos son números.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Los parámetros deben ser números")
        return func(self, *args, **kwargs)
    return wrapper

def validate_user_permissions(func):
    """
    Decorador para verificar permisos de usuario en operaciones.
    """
    @wraps(func)
    def wrapper(self, x, y):
        if not validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissionsError('Usuario sin permisos')
        return func(self, x, y)
    return wrapper

def validate_non_negative(func):
    """
    Decorador que verifica si el primer argumento no es negativo.
    """
    @wraps(func)
    def wrapper(self, x, *args, **kwargs):
        if x < 0:
            raise ValueError("Números negativos no permitidos")
        return func(self, x, *args, **kwargs)
    return wrapper

def validate_log_arguments(func):
    """
    Decorador que verifica las condiciones específicas para la función log.
    """
    @wraps(func)
    def wrapper(self, x, base, *args, **kwargs):
        if x < 0:
            raise ValueError("Números negativos no permitidos")
        if base <= 0 or base == 1:
            raise ValueError("La base debe ser un número positivo mayor que 1")
        return func(self, x, base, *args, **kwargs)
    return wrapper