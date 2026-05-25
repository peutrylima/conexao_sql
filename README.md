# Meu Primeiro CRUD

Bem-vindo(a) ao meu primeiro projeto de conexão entre uma aplicação Python e um banco de dados SQL Server! 

Este repositório contém o exercício prático que desenvolvi para entender como sistemas interagem com bancos de dados relacionais na vida real. O projeto consiste na criação de um banco de dados de notícias e categorias, e um script Python que gerencia esses dados de ponta a ponta.

## O Que Aprendi 

* **Modelagem de Banco de Dados Relacional:** Aprendi a estruturar tabelas usando SQL, definindo Chaves Primárias (`PRIMARY KEY`) para identificar registros únicos e Chaves Estrangeiras (`FOREIGN KEY`) para criar relacionamentos (uma Notícia pertence a uma Categoria).

* **Strings de Conexão:** Entendi como configurar os parâmetros necessários (`Driver`, `Server`, `Database`, `UID`, `PWD`) para que o Python saiba exatamente onde e como se conectar ao servidor SQL local.

* **Operações CRUD com Python:** Consegui implementar com sucesso as 4 operações fundamentais de persistência de dados utilizando comandos SQL encapsulados no Python:
    * **C**reate: Inserção de novos dados (`INSERT INTO`).
    * **R**ead: Consulta e listagem de dados (`SELECT * FROM`).
    * **U**pdate: Atualização de registros existentes (`UPDATE`).
    * **D**elete: Remoção de dados do banco (`DELETE`).
    
* **Gerenciamento de Cursores e Transações:** Aprendi a utilizar o `cursor` do `pyodbc` para executar comandos e a importância do `conn.commit()` para confirmar e salvar as alterações feitas no banco de dados.

* **Boas Práticas de Conexão:** Compreendi a necessidade de sempre fechar o cursor (`cursor.close()`) e a conexão (`conn.close()`) ao final do script para evitar o vazamento de recursos do sistema.
