import pytest
from validator import Validator


@pytest.fixture
def vd():
    return Validator()

@pytest.mark.parametrize("valor, resultado", [
    ("11122233344", True),
    ("111.222.333-44", True),
    ("1112223334", False),
    ("111-222-333.4", False),
])
def test_validar_tamanho_cpf(vd, valor, resultado):
    assert vd.validar_cpf(valor) == resultado, "Tamanho de CPF invalido"

@pytest.mark.parametrize("valor, resultado", [
    ("11122233344", True),
    ("111.222.333-44", True),
    ("111.222.333", False),
    ("111-222-333.44", False),
])
def test_validar_formato_cpf(vd, valor, resultado):
    assert vd.validar_cpf(valor) == resultado, "Formato de CPF invalido"

@pytest.mark.parametrize("valor, resultado", [
    (11122233344, False),
    ("111.222.333-44", True),
    (111.222, False),
    ("11122233344", True),
])
def test_validar_entrada_cpf(vd, valor, resultado):
    assert vd.validar_cpf(valor) == resultado, "CPF nao esta no formato texto"

@pytest.mark.parametrize("valor, resultado", [
    ("11222333", True),
    ("1112223", False),
    ("11222-333", True),
    ("1112223334", False),
])
def test_validar_tamanho_cep(vd, valor, resultado):
    assert vd.validar_cep(valor) == resultado, "Tamanho de CEP invalido"

@pytest.mark.parametrize("valor, resultado", [
    ("00111-333", True),
    ("11122333", True),
    ("11122.333", False),
    ("11-222333", False),
])
def test_validar_formato_cep(vd, valor, resultado):
    assert vd.validar_cep(valor) == resultado, "Formato de CEP invalido"

@pytest.mark.parametrize("valor, resultado", [
    (11122233344, False),
    ("11222-333", True),
    (111.222, False),
    ("11122333", True),
])
def test_validar_entrada_cep(vd, valor, resultado):
    assert vd.validar_cep(valor) == resultado, "CEP nao esta no formato texto"

@pytest.mark.parametrize("valor, resultado", [
    ("11222333444455", True),
    ("11.222.333/4444-55", True),
    ("111222333444455", False),
    ("11.222.333/4444-555", False),
])
def test_validar_tamanho_cnpj(vd, valor, resultado):
    assert vd.validar_cnpj(valor) == resultado, "Tamanho de CNPJ invalido"

@pytest.mark.parametrize("valor, resultado", [
    ("11222333444455", True),
    ("11.222.333/4444.55", False),
    ("11-222-333.4444/55", False),
    ("11.222.333/4444-55", True),
])
def test_validar_formato_cnpj(vd, valor, resultado):
    assert vd.validar_cnpj(valor) == resultado, "Formato de CNPJ invalido"

@pytest.mark.parametrize("valor, resultado", [
    (11222333444455, False),
    ("11.222.333/4444-55", True),
    (111222333, False),
    ("11222333444455", True),
])
def test_validar_entrada_cnpj(vd, valor, resultado):
    assert vd.validar_cnpj(valor) == resultado, "CNPJ nao esta no formato texto"
