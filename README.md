# 🛒 Sistema de Vendas Simples - CRUD

## 🖥️ Sobre o sistema
Este é um **Sistema de Vendas Simples** desenvolvido em Python, utilizando **MySQL** para o banco de dados e **Tkinter** para a interface gráfica. O sistema é projetado para gerenciar as operações básicas de um pequeno negócio, cobrindo o ciclo completo de **Cadastro, Consulta e Registro de Vendas (CRUD)**.

---

## 💡 Funcionalidades
* **Cadastro de Clientes:** Adicionar, visualizar, atualizar e deletar informações de clientes.
* **Cadastro de Produtos:** Adicionar, visualizar, atualizar e deletar produtos com preço e estoque.
* **Registro de Vendas:**
    * Registrar novas vendas, associando um cliente.
    * Adicionar múltiplos itens (produtos) a uma venda.
    * Cálculo automático do subtotal e total da venda.
    * Registro da data da venda.
* **Consulta de Histórico:** Listar todas as vendas registradas com detalhes (cliente, data, total).
* **Análise de Vendas (Dica):** Funcionalidade para calcular e exibir o total de vendas por dia, semana ou mês.
* Interface visual intuitiva com Tkinter.

---

## 💻 Requisitos para rodar o sistema
* Python 3.x instalado.
* MySQL Server instalado e em execução.
* Bibliotecas Python:
    * `mysql-connector-python`
    * `tkinter` (já incluso no Python padrão)

### ⚙️ Instalação das dependências
```bash
pip install mysql-connector-python
```

## 🎲 Estrutura do Banco de Dados (MySQL)

**Banco de dados:** `sistema_vendas`

Este sistema utiliza quatro tabelas para gerenciar clientes, produtos e o registro transacional de vendas. 

### Tabela: `clientes`
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INT` | Identificador único (PK) |
| `nome` | `VARCHAR(255)` | Nome completo do cliente |
| `email` | `VARCHAR(255)` | E-mail do cliente |
| `telefone` | `VARCHAR(20)` | Telefone de contato |

### Tabela: `produtos`
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INT` | Identificador único (PK) |
| `nome` | `VARCHAR(255)` | Nome do produto |
| `preco` | `DECIMAL(10, 2)` | Preço unitário do produto |
| `estoque` | `INT` | Quantidade em estoque |

### Tabela: `vendas` (Cabeçalho da venda)
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INT` | Identificador único da venda (PK) |
| `cliente_id` | `INT` | ID do cliente (Chave Estrangeira - FK) |
| `data_venda` | `DATETIME` | Data e hora exatas do registro |
| `valor_total` | `DECIMAL(10, 2)` | Valor total final da venda |

### Tabela: `itens_venda` (Itens da venda)
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | `INT` | Identificador único (PK) |
| `venda_id` | `INT` | ID da venda (FK) |
| `produto_id` | `INT` | ID do produto vendido (FK) |
| `quantidade` | `INT` | Quantidade do produto vendido |
| `preco_unitario` | `DECIMAL(10, 2)` | Preço unitário no momento da venda |

---

## 🛠 Tecnologias Usadas
* **Python 3.x**
* **Tkinter** (Interface gráfica)
* **MySQL** (Banco de dados relacional)
* **`mysql-connector-python`** (Conector Python <-> MySQL)

---

## 📂 Estrutura do Projeto
```bash
sistema_vendas/
│
├── app_vendas.py     # Código principal (conexão, CRUD, interface)
└── README.md         # Documentação do projeto
```

## 🔩 Como Usar

1.  **Preparação:** Certifique-se de que o **MySQL Server** está em execução e que o banco de dados `sistema_vendas` foi criado, incluindo todas as tabelas necessárias (`clientes`, `produtos`, `vendas`, `itens_venda`).
2.  **Execução:** Abra o terminal na pasta raiz do projeto (`sistema_vendas/`) e inicie o aplicativo Python:
    ```bash
    python app_vendas.py
    ```
3.  **Utilização:** A interface gráfica do Tkinter será carregada. Utilize-a para gerenciar o CRUD de cadastros (clientes e produtos) e para registrar transações de vendas. Todos os dados são automaticamente armazenados no banco de dados MySQL.

---

## 🧑‍💻 Desenvolvido por Guilherme Gonçalves.
