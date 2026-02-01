# 💊 Localizador de Medicamentos SUS - Rio de Janeiro

Este projeto é uma aplicação de inteligência de dados desenvolvida para facilitar o acesso da população carioca a informações sobre medicamentos
gratuitos. O sistema indica não apenas se o remédio existe, mas **exatamente em qual unidade de saúde (CMS ou Clínica da Família)** ele pode ser encontrado, 
com endereço completo e documentos necessários.

## 🛠️ O Processo de Desenvolvimento

O projeto foi construído utilizando o conceito de **Pipeline de Dados** e a **Arquitetura Medallion**, garantindo que a informação seja tratada e validada 
antes de chegar ao cidadão.

### 1. Organização dos Dados (Camadas)

Os dados passam por três níveis de maturidade dentro da pasta `data/`:

* **Bronze:** Dados brutos, exatamente como inseridos inicialmente no arquivo `remedios_brutos.csv`.
* **Silver:** Dados limpos e padronizados (nomes em maiúsculo, remoção de espaços extras).
* **Gold:** Base final otimizada, pronta para ser lida pelo aplicativo de busca.

### 2. Processamento (O "Motor")

Para garantir a atualização dos dados, foi desenvolvido o script `pipeline.py`. Ele é responsável por:

* Criar a estrutura de pastas automaticamente.
* Processar os dados da camada Bronze para a Gold.
* Validar se as colunas de **Unidade** e **Endereço** estão corretas.

### 3. Interface do Usuário

A aplicação utiliza **Streamlit** no arquivo `app.py` para oferecer uma busca rápida e responsiva, onde o usuário filtra os medicamentos em tempo real.

---

## 🚀 Como Executar o Projeto

Para rodar este projeto na sua máquina, siga os passos abaixo no terminal:

### Passo 1: Processar o Pipeline

Primeiro, precisamos transformar os dados brutos nos dados finais que o site utiliza:

```bash
python pipeline.py

```

### Passo 2: Iniciar a Aplicação Web

Com os dados processados na pasta Gold, inicie o servidor do Streamlit:

```bash
streamlit run app.py

```

---

## 📋 Tecnologias Utilizadas

* **Python 3.x**
* **Pandas**: Para manipulação e tratamento de dados.
* **Streamlit**: Para a criação da interface web.
* **Arquitetura Medallion**: Para organização de governança de dados.

---

**Desenvolvido por Charles Ferreira** *Focado em utilizar tecnologia para gerar impacto social na saúde pública do Rio de Janeiro.*

---
