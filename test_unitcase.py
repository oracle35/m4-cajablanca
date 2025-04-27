
import pytest
from main import validar_contrasena

def test_contrasena_valida():
    assert validar_contrasena("Password1!") == True

def test_contrasena_corta():
    assert validar_contrasena("P1!") == False

def test_contrasena_sin_mayuscula():
    assert validar_contrasena("password1!") == False

def test_contrasena_sin_numero():
    assert validar_contrasena("Password!") == False

def test_contrasena_sin_especial():
    assert validar_contrasena("Password1") == False

def test_contrasena_todo_faltante():
    assert validar_contrasena("pass") == False

def test_contrasena_con_caracteres_especiales_extra():
    assert validar_contrasena("P@ssw0rd!") == True  # Más de un especial

def test_contrasena_caracter_especial_al_inicio():
    assert validar_contrasena("!Password1") == True

def test_contrasena_caracter_especial_al_final():
    assert validar_contrasena("Password1!") == True

def test_contrasena_justo_8_caracteres():
    assert validar_contrasena("A1!bcdef") == True  # Exactamente 8 caracteres

def test_contrasena_muy_larga_valida():
    assert validar_contrasena("SuperSecurePassword123$") == True
