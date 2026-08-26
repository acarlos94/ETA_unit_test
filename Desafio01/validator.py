import re

class Validator:
    formato_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    formato_cep = r"^\d{5}\-?\d{3}$"
    def validar_cpf_tamanho(self, cpf):
        if len(cpf) == 14:
            return True
        return False

    def validar_cpf_formato(self, cpf):
        if re.match(self.formato_cpf, cpf):
            return True
        return False

    def validar_cpf_texto(self, cpf):
        if str(cpf):
            return True
        return False

    def validar_cep(self, cep):
        texto = False
        tamanho = False
        formato = False
        if str(cep):
            texto = True
        if len(cep) == 8 or len(cep) == 9:
            tamanho = True
        if re.match(self.formato_cep, cep):
            formato = True
        return texto, tamanho, formato
