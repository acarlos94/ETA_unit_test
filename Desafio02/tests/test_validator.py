import pytest
import requests

from ..app import validator as validator_module
from ..app.validator import Validator


@pytest.fixture
def vd():
    return Validator()


@pytest.mark.parametrize("cpf", [
    "11122233344",
    "111.222.333-44",
])
def test_validar_cpf_valido(vd, cpf):
    assert vd.validar_cpf(cpf) is True, "CPF invalido informado"


@pytest.mark.parametrize("cpf", [
    "1112223334",
    "111.222.333-444",
    "111-222-333.44",
])
def test_validar_cpf_invalido(vd, cpf):
    assert vd.validar_cpf(cpf) is False, "CPF invalido foi aceito"


def test_validar_cpf_entrada_invalida(vd):
    with pytest.raises(ValueError):
        vd.validar_cpf(11122233344)


@pytest.mark.parametrize("cnpj", [
    "11222333444455",
    "11.222.333/4444-55",
])
def test_validar_cnpj_valido(vd, cnpj):
    assert vd.validar_cnpj(cnpj) is True


@pytest.mark.parametrize("cnpj", [
    "112223334444555",
    "11.222.333/444-55",
    "11-222-333/4444.55",
])
def test_validar_cnpj_invalido(vd, cnpj):
    assert vd.validar_cnpj(cnpj) is False, "Cnpj invalido foi aceito"


def test_validar_cnpj_entrada_invalida(vd):
    with pytest.raises(ValueError):
        vd.validar_cnpj(11222333444455)


@pytest.mark.parametrize("cep", [
    "112223334",
    "11222-3",
    "11222.333",
])
def test_validar_cep_formato_invalido(vd, cep):
    assert vd.validar_cep(cep) is False, "CEP invalido foi aceito"


def test_validar_cep_entrada_invalida(vd):
    with pytest.raises(ValueError):
        vd.validar_cep(11222333)


@pytest.mark.parametrize("cep", [
    "11222333",
    "11222-333",
])
def test_validar_cep_valido(vd, cep, mocker):
    mock_servico = mocker.patch.object(validator_module, "ServicoCorreios")
    mock_servico.return_value.valida_cep_api.return_value = True

    assert vd.validar_cep(cep) is True, "CEP invalido informado"
    mock_servico.return_value.valida_cep_api.assert_called_once_with(cep)


def test_validar_cep_invalido_pela_api(vd, mocker):
    mock_servico = mocker.patch.object(validator_module, "ServicoCorreios")
    mock_servico.return_value.valida_cep_api.return_value = False

    assert vd.validar_cep("11222333") is False, "CEP invalido foi aceito"


def test_validar_cep_erro_conexao_api(vd, mocker):
    mock_servico = mocker.patch.object(validator_module, "ServicoCorreios")
    mock_servico.return_value.valida_cep_api.side_effect = requests.exceptions.HTTPError

    with pytest.raises(requests.exceptions.HTTPError):
        vd.validar_cep("11222333")
