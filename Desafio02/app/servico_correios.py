import requests


class ServicoCorreios:
    def valida_cep_api(self, cep):
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        resposta.raise_for_status()
        return not resposta.json().get("erro", False)
