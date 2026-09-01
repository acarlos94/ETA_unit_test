import pytest
from ..app.validator import Validator


@pytest.fixture
def vd():
    return Validator()

def test_check_cpf_texto(vd):
    with pytest.raises(TypeError):
        vd.validar_cpf(123456)

@pytest.mark.parametrize("valor", [
    "11122233344",
    "111.222.333-44"
])
def test_check_cpf_valido(vd, valor):
    assert vd.validar_cpf(valor), "cpf invalido"

@pytest.mark.parametrize("valor", [
    "1112223334",
    "111.222.333-444",
    "111-222-333.44",
])
def test_check_cpf_invalido(vd, valor):
    assert vd.validar_cpf("") == False, "CPF invalido foi autorizado"

def test_check_cep_texto(vd):
    with pytest.raises(TypeError):
        vd.validar_cep(123456)

@pytest.mark.parametrize("valor", [
    "11222333",
    "11222-333"
])
def test_check_cep_valido(vd, valor):
    assert vd.validar_cep(valor), "CEP invalido"

@pytest.mark.parametrize("valor", [
    "112223334",
    "11222-3",
    "11222.333",
])
def test_check_cep_invalido(vd, valor):
    assert vd.validar_cep("") == False, "CEP invalido foi autorizado"

def test_check_cnpj_texto(vd):
    with pytest.raises(TypeError):
        vd.validar_cnpj(123456)

@pytest.mark.parametrize("valor", [
    "11222333444455",
    "11.222.333/4444-55"
])
def test_check_cnpj_valido(vd, valor):
    assert vd.validar_cnpj(valor), "CNPJ invalido"

@pytest.mark.parametrize("valor", [
    "112223334444555",
    "11.222.333/444-55",
    "11-222-333/4444.55"
])
def test_check_cnpj_invalido(vd, valor):
    assert vd.validar_cnpj("") == False, "CNPJ invalido foi autorizado"
