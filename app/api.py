import http.client
from flask import Flask
from app import util
from app.calc import Calculator

# Creación de la instancia de la calculadora
CALCULATOR = Calculator()
# Creación de la aplicación Flask
api_application = Flask(__name__)
# Definición de los encabezados HTTP comunes
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    """
    Ruta raíz que devuelve un mensaje de bienvenida.
    """
    return "Hello from The Calculator!\n"


def process_operation(operation, op_1, op_2=None):
    """
    Función auxiliar para procesar operaciones de la calculadora.
    
    Parámetros:
    operation -- Función de operación de la calculadora a ejecutar.
    op_1 -- Primer operando como string.
    op_2 -- Segundo operando como string (opcional, dependiendo de la operación).
    
    Retorna:
    Una tupla de tres elementos: el resultado de la operación, el código HTTP y los encabezados.
    """
    try:
        # Conversión de los operandos a números
        num_1 = util.convert_to_number(op_1)
        num_2 = util.convert_to_number(op_2) if op_2 is not None else None

        # Ejecución de la operación
        result = operation(num_1, num_2) if num_2 is not None else operation(num_1)

        # Devolver el resultado con un código HTTP OK
        return ("{}".format(result), http.client.OK, HEADERS)
    except ZeroDivisionError:
        return "División por cero no es posible", http.client.BAD_REQUEST
    except (TypeError, ValueError) as e:
        # Devolver el mensaje de error con un código HTTP BAD_REQUEST
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    """
    Ruta para sumar dos números.
    """
    return process_operation(CALCULATOR.add, op_1, op_2)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    """
    Ruta para restar dos números.
    """
    return process_operation(CALCULATOR.substract, op_1, op_2)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    """
    Ruta para multiplicar dos números.
    """
    return process_operation(CALCULATOR.multiply, op_1, op_2)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    """
    Ruta para dividir un número por otro.
    """
    return process_operation(CALCULATOR.divide, op_1, op_2)


@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    """
    Ruta para elevar un número a la potencia de otro.
    """
    return process_operation(CALCULATOR.power, op_1, op_2)


@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    """
    Ruta para calcular la raíz cuadrada de un número.
    """
    return process_operation(CALCULATOR.sqrt, op_1)


@api_application.route("/calc/log/<op_1>/<base>", methods=["GET"])
def log(op_1, base):
    """
    Ruta para calcular el logaritmo de un número en una base dada.
    """
    return process_operation(CALCULATOR.log, op_1, base)


if __name__ == "__main__":
    # Ejecución de la aplicación Flask
    api_application.run(debug=True)
