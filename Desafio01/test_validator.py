import pytest

from validator import Validator

@pytest.fixture
def vd():
    return Validator()

def test_validar_cpf_tamanho(vd):
    assert vd.validar_cpf_tamanho('111-222.333-99'), "Tamanho de CPF invalido"

def test_validar_cpf_formato(vd):
    assert vd.validar_cpf_formato('123.222.333-99'), "Formato de CPF invalido"

def test_validar_cpf_texto(vd):
    numero = "teste"
    assert vd.validar_cpf_texto(numero), "CPF informado nao esta no formato de texto"

def test_validar_cep(vd):
    texto_cep, tamanho_cep, formato_cep = vd.validar_cep("11111-999")
    assert texto_cep, "CEP informado nao esta no formato de texto"
    assert tamanho_cep, "Tamanho de CEP invalido"
    assert formato_cep, "Formato de CEP invalido"
