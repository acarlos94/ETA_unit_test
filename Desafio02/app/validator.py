import re

from .servico_correios import ServicoCorreios


class Validator:
    formato_cpf = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
    formato_cep = r"^\d{5}\-?\d{3}$"
    formato_cnpj = r"^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}$"

    def validar_cpf(self, cpf):
        if not isinstance(cpf, str):
            raise ValueError("CPF nao esta no formato texto")
        tamanho = len(cpf) in (11, 14)
        formato = bool(re.match(self.formato_cpf, cpf))
        return tamanho and formato

    def validar_cep(self, cep):
        if not isinstance(cep, str):
            raise ValueError("CEP nao esta no formato texto")
        tamanho = len(cep) in (8, 9)
        formato = bool(re.match(self.formato_cep, cep))
        if not (tamanho and formato):
            return False
        return ServicoCorreios().valida_cep_api(cep)

    def validar_cnpj(self, cnpj):
        if not isinstance(cnpj, str):
            raise ValueError("CNPJ nao esta no formato texto")
        tamanho = len(cnpj) in (14, 18)
        formato = bool(re.match(self.formato_cnpj, cnpj))
        return tamanho and formato
