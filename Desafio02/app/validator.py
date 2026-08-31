import re

class Validator:
    formato_cpf = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
    formato_cep = r"^\d{5}\-?\d{3}$"
    formato_cnpj = r"^\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}$"

    def validar_cpf(self, cpf):
        tamanho = False
        formato = False
        if not isinstance(cpf, str):
            raise TypeError("CPF nao esta no formato texto")
        if len(cpf) == 11 or len(cpf) == 14:
            tamanho = True
        if re.match(self.formato_cpf, cpf):
            formato = True
        if tamanho and formato:
            return True
        return False

    def validar_cep(self, cep):
        tamanho = False
        formato = False
        if not isinstance(cep, str):
            raise TypeError("CEP nao esta no formato texto")
        if len(cep) == 8 or len(cep) == 9:
            tamanho = True
        if re.match(self.formato_cep, cep):
            formato = True
        if tamanho and formato:
            return True
        return False

    def validar_cnpj(self, cnpj):
        tamanho = False
        formato = False
        if not isinstance(cnpj, str):
            raise TypeError("CNPJ nao esta no formato texto")
        if len(cnpj) == 14 or len(cnpj) == 18:
            tamanho = True
        if re.match(self.formato_cnpj, cnpj):
            formato = True
        if tamanho and formato:
            return True
        return False
