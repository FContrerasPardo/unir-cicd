import http.client
import json
import os
import unittest
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import pytest

# Base URL del servicio API para la calculadora, obtenida de las variables de entorno
BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # Tiempo de espera por defecto para las respuestas de la API, en segundos

@pytest.mark.api
class TestApi(unittest.TestCase):
    # Pruebas de éxito
    def setUp(self):
        # Asegurar que la URL base esté configurada antes de cada prueba
        self.assertIsNotNone(BASE_URL, "URL base no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL base parece inválida")

    def test_api_add(self):
        # Probar la función de suma de la API
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")

    # Prueba para la función de resta
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Prueba para la función de multiplicación
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Prueba para la función de división
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Prueba para la función de potencia
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Prueba para la función de raíz cuadrada
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    # Prueba para la función logarítmica
    def test_api_log(self):
        url = f"{BASE_URL}/calc/log/100/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)
    
    # Pruebas de error
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "La API no maneja la división por cero correctamente")

    def test_api_invalid_input(self):
        urls = [
            f"{BASE_URL}/calc/add/ten/2",
            f"{BASE_URL}/calc/divide/10/two"
        ]
        for url in urls:
            with self.assertRaises(HTTPError) as context:
                urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "La API no maneja entradas inválidas correctamente")

    # Prueba para la función de raíz cuadrada con número negativo
    def test_api_sqrt_negative_number(self):
        url = f"{BASE_URL}/calc/sqrt/-4"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "La API no maneja la raíz cuadrada de números negativos correctamente")

    # Prueba para la función logarítmica con base inválida
    def test_api_log_invalid_base(self):
        url = f"{BASE_URL}/calc/log/4/1"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, "La API no maneja la base logarítmica inválida correctamente")

if __name__ == "__main__":
    unittest.main()
