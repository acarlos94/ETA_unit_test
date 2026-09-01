# 🧪 Desafio 2 de Testes Unitários com Pytest

O objetivo do exercício é implementar uma suíte de testes unitários automatizados utilizando Pytest para garantir a aplicacao das regras de validação de três identificadores brasileiros: CPF, CNPJ e CEP.

---
### 📋 Sobre o Desafio

A aplicação possui um módulo validador com regras de negócio específicas para cada tipo de dado. Sua missão é escrever cenários de testes cobrindo o caminho feliz, cenários negativos e casos de borda.

* Validador de CPF: Verifica o formato (000.000.000-00 ou apenas números), a quantidade exata de 11 ou 14 dígitos, a rejeição de sequências inválidas conhecidas (ex: 111.111.111-11) e se o valor de entrada é um texto.  
* Validador de CNPJ: Checa a formatação (00.000.000/0001-00 ou apenas dígitos), a extensão de 14 ou 18 dígitos e se o valor de entrada é um texto.  
* Validador de CEP: Avalia se o CEP possui 8 ou 9 dígitos, o suporte à formatação com hífen (00000-000) e se o valor de entrada é um texto.  
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
Para executar com relatório detalhado (verbose) e relatório de cobertura de código:
```bash
pytest -v --cov=src
```