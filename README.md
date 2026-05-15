# 🐍 Integrando Python e SQL Server: Meu Primeiro CRUD

Bem-vindo(a) ao meu primeiro projeto de conexão entre uma aplicação Python e um banco de dados SQL Server! 

Este repositório contém o exercício prático que desenvolvi para entender como sistemas interagem com bancos de dados relacionais na vida real. O projeto consiste na criação de um banco de dados de notícias e categorias, e um script Python que gerencia esses dados de ponta a ponta.

---

## 🚀 O Que Eu Aprendi Neste Projeto

Este exercício foi um grande passo no meu aprendizado, permitindo consolidar os seguintes conceitos:

* **Modelagem de Banco de Dados Relacional:** Aprendi a estruturar tabelas usando SQL, definindo Chaves Primárias (`PRIMARY KEY`) para identificar registros únicos e Chaves Estrangeiras (`FOREIGN KEY`) para criar relacionamentos (uma Notícia pertence a uma Categoria).
* **Strings de Conexão:** Entendi como configurar os parâmetros necessários (`Driver`, `Server`, `Database`, `UID`, `PWD`) para que o Python saiba exatamente onde e como se conectar ao servidor SQL local.
* **Operações CRUD com Python:** Consegui implementar com sucesso as 4 operações fundamentais de persistência de dados utilizando comandos SQL encapsulados no Python:
    * **C**reate: Inserção de novos dados (`INSERT INTO`).
    * **R**ead: Consulta e listagem de dados (`SELECT * FROM`).
    * **U**pdate: Atualização de registros existentes (`UPDATE`).
    * **D**elete: Remoção de dados do banco (`DELETE`).
* **Gerenciamento de Cursores e Transações:** Aprendi a utilizar o `cursor` do `pyodbc` para executar comandos e a importância do `conn.commit()` para confirmar e salvar as alterações feitas no banco de dados.
* **Boas Práticas de Conexão:** Compreendi a necessidade de sempre fechar o cursor (`cursor.close()`) e a conexão (`conn.close()`) ao final do script para evitar o vazamento de recursos do sistema.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Banco de Dados:** Microsoft SQL Server (SQLEXPRESS)
* **Biblioteca:** `pyodbc` (Para realizar a ponte de comunicação entre o Python e o SQL Server)
* **Linguagem de Consulta:** T-SQL

---

## ⚙️ Como Executar o Projeto

Caso queira rodar este projeto na sua máquina, siga os passos abaixo:

1. **Pré-requisitos:**
   * Ter o Python instalado.
   * Ter o SQL Server (e o SQL Server Management Studio - SSMS) instalado.
   * Instalar a biblioteca `pyodbc`:
     ```bash
     pip install pyodbc
     ```

2. **Preparando o Banco de Dados:**
   * Abra o SQL Server.
   * Execute o script `atv_conexao.sql` para criar o banco de dados `atividade_pratica` e as tabelas `Categoria` e `Noticia`.

3. **Configurando a Conexão:**
   * No arquivo `atv_conexao.py`, altere o parâmetro `Server` dentro da variável `conn_str` para o nome do seu servidor local do SQL Server.
   * Verifique se o seu usuário (`UID`) e senha (`PWD`) estão corretos. Se estiver usando Autenticação do Windows, você pode substituir `UID` e `PWD` por `Trusted_Connection=yes;`.

4. **Executando o Script:**
   * Rode o arquivo Python no seu terminal:
     ```bash
     python atv_conexao.py
     ```
   * Acompanhe no terminal as mensagens de impressão mostrando a inserção, atualização e deleção dos dados em tempo real!
