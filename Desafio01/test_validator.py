import pytest

from validator import Validator

@pytest.fixture
def vd():
    return Validator()

@pytest.mark.parametrize("valor", [
    "11122233344",
    "111.222.333-44",
    "1112223334",
    "111-222-333.4",
])
def test_validar_tamanho_cpf(vd, valor):
    assert vd.validar_cpf(valor), "Tamanho de CPF invalido"

@pytest.mark.parametrize("valor", [
    "11122233344",
    "111.222.333-44",
    "111.222.333",
    "111-222-333.44",
])
def test_validar_formato_cpf(vd, valor):
    assert vd.validar_cpf(valor), "Formato de CPF invalido"

@pytest.mark.parametrize("valor", [
    11122233344,
    "111.222.333-44",
    111.222,
    "11122233344",
])
def test_validar_entrada_cpf(vd, valor):
    assert vd.validar_cpf(valor), "CPF nao esta no formato texto"

@pytest.mark.parametrize("valor", [
    "11222333",
    "1112223",
    "11222-333",
    "1112223334",
])
def test_validar_tamanho_cep(vd, valor):
    assert vd.validar_cep(valor), "Tamanho de CEP invalido"

@pytest.mark.parametrize("valor", [
    "00111-333",
    "11122333",
    "11122.333",
    "11-222333",
])
def test_validar_formato_cep(vd, valor):
    assert vd.validar_cep(valor), "Formato de CEP invalido"

@pytest.mark.parametrize("valor", [
    11122233344,
    "11222-333",
    111.222,
    "11122333",
])
def test_validar_entrada_cep(vd, valor):
    assert vd.validar_cep(valor), "CepEP nao esta no formato texto"

@pytest.mark.parametrize("valor", [
    "11222333444455",
    "11.222.333/4444-55",
    "111222333444455",
    "11.222.333/4444-555",
])
def test_validar_tamanho_cnpj(vd, valor):
    assert vd.validar_cnpj(valor), "Tamanho de CNPJ invalido"

@pytest.mark.parametrize("valor", [
    "11222333444455",
    "11.222.333/4444.55",
    "11-222-333.4444/55",
    "11.222.333/4444-55",
])
def test_validar_formato_cnpj(vd, valor):
    assert vd.validar_cnpj(valor), "Formato de CNPJ invalido"

@pytest.mark.parametrize("valor", [
    11222333444455,
    "11.222.333/4444-55",
    111222333,
    "11222333444455",
])
def test_validar_entrada_cnpj(vd, valor):
    assert vd.validar_cnpj(valor), "CNPJ nao esta no formato texto"
