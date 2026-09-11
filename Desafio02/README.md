# 🧪 Desafio 2 de Testes Unitários com Pytest

O objetivo do exercício é incrementar a suíte de testes unitários automatizados criada no Desafio 1 aplicando conceitos avançados, como fixtures, mocking e integracao com pipelines.

---
### 📋 Sobre o Desafio

Incrementar as classes geradas no Desafio 1, organizando os diretorios e adicionando uma chamada a uma validacao ficticia por servico externo.

* Classe: ServicoCorreios
* Metodo: valida_cep_api(self, cep)

Adicionar um teste unitario com pytest, incluindo:

* Mocking da classe ServicoCorreios
* Chamada a valida_cep_api, simulando retorno True em caso de sucesso ou False em falha de validacao
* Simular um erro de conexao com a excecao requests.exceptions.HTTPError

---
### ⚙️️ Configuração do Ambiente
Acesse a pasta do desafio
```bash  
cd Desafio02  
```
Crie e ative o ambiente virtual:

Linux/MacOS
```Bash
python3 -m venv venv
source venv/bin/activate
```
Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
---
### 🚀 Executando os Testes
Para rodar todos os testes unitários:
```bash
pytest
```
Para executar com relatório detalhado (verbose) e relatório de cobertura de código, mostrando as linhas não cobertas:
```bash
pytest -v --cov=app --cov-report=term-missing
```