import unittest
from unittest.mock import patch
import pytest
from app.calc import Calculator

def mocked_validation(*args, **kwargs):
    return True

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    # Configuración inicial para cada prueba
    def setUp(self):
        self.calc = Calculator()

    # Pruebas para la función add
    def test_add_method_returns_correct_result(self):
        # Testear sumas con diferentes tipos de entradas
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(2, self.calc.add(1, 1))
        self.assertEqual(10, self.calc.add(5, 5))


    # Pruebas para la función substract
    def test_substract_method_returns_correct_result(self):
        # Testear restas con diferentes tipos de entradas
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(6, self.calc.substract(4, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    # Pruebas para la función divide
    def test_divide_method_returns_correct_result(self):
        # Testear divisiones con diferentes tipos de entradas
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-1.5, self.calc.divide(-3, 2))
        self.assertEqual(-1.5, self.calc.divide(3, -2))
    # Pruebas para la función divide
    def test_divide_method_fails_with_division_by_zero(self):
        # Testear que divide maneja correctamente la división por cero
        self.assertRaises(ZeroDivisionError, self.calc.divide, 2, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, -2, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 0, 0)

    # Pruebas para manejar entradas no numéricas en add y divide
    def test_add_method_fails_with_nan_parameter(self):
        # Testear que add maneja correctamente entradas no numéricas
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        # Testear que divide maneja correctamente entradas no numéricas
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    # Pruebas para la función multiply con mock de validate_permissions
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        # Testear multiplicaciones con diferentes tipos de entradas
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    # Pruebas adicionales para nuevas funciones

    # Pruebas para la función power
    def test_power_method_returns_correct_result(self):
        # Testear potencias con diferentes tipos de entradas
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))

    def test_power_method_fails_with_nan_parameter(self):
        # Testear que power maneja correctamente entradas no numéricas
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")

    # Pruebas para la función sqrt
    def test_sqrt_method_returns_correct_result(self):
        # Testear raíz cuadrada con diferentes tipos de entradas
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(3, self.calc.sqrt(9))

    def test_sqrt_method_fails_with_negative_parameter(self):
        # Testear que sqrt maneja correctamente números negativos
        self.assertRaises(ValueError, self.calc.sqrt, -1)

    def test_sqrt_method_fails_with_nan_parameter(self):
        # Testear que sqrt maneja correctamente entradas no numéricas
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    # Pruebas para la función log
    def test_log_method_returns_correct_result(self):
        # Testear logaritmos con diferentes tipos de entradas
        self.assertAlmostEqual(2, self.calc.log(100, 10))
        self.assertAlmostEqual(1, self.calc.log(10, 10))

    def test_log_method_fails_with_invalid_parameters(self):
        # Testear que log maneja correctamente entradas inválidas
        self.assertRaises(ValueError, self.calc.log, -1, 10)
        self.assertRaises(ValueError, self.calc.log, 10, 0)
        self.assertRaises(ValueError, self.calc.log, 10, 1)

    def test_log_method_fails_with_nan_parameters(self):
        # Testear que log maneja correctamente entradas no numéricas
        self.assertRaises(TypeError, self.calc.log, "10", 10)
        self.assertRaises(TypeError, self.calc.log, 10, "10")

if __name__ == "__main__":
    unittest.main()