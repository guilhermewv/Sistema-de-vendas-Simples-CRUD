import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="sua_senha", database="sistema_vendas"):
        self.host = host
        self.user = user
        self.password = password 
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Conexão com o MySQL estabelecida com sucesso.")
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Conexão", f"Falha ao conectar ao MySQL: {err}")
            self.conn = None
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexão com o MySQL encerrada.")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de SQL", f"Erro na consulta: {err}")
            self.conn.rollback() 
            return None
    
    def commit(self):
        if self.conn:
            self.conn.commit()


class AppVendas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🛒 Sistema de Vendas Simples")
        self.geometry("1000x650")

      
        self.db = Database()
        if not self.db.connect():
            self.destroy()
            return

      
        self.selected_client_id = tk.StringVar()
        
       
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        
        self.frame_clientes = ttk.Frame(self.notebook)
        self.frame_produtos = ttk.Frame(self.notebook)
        self.frame_vendas = ttk.Frame(self.notebook)
        
        self.notebook.add(self.frame_clientes, text='Clientes')
        self.notebook.add(self.frame_produtos, text='Produtos')
        self.notebook.add(self.frame_vendas, text='Registro de Vendas')

        
        self._setup_clientes_tab()
        self._setup_produtos_tab()
        self._setup_vendas_tab()
        
    def _setup_clientes_tab(self):
        
      
        frame_input = ttk.LabelFrame(self.frame_clientes, text="Novo Cliente")
        frame_input.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome_cliente = ttk.Entry(frame_input, width=40)
        self.entry_nome_cliente.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_input, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_email_cliente = ttk.Entry(frame_input, width=40)
        self.entry_email_cliente.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_input, text="Telefone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_tel_cliente = ttk.Entry(frame_input, width=40)
        self.entry_tel_cliente.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame_input, text="Adicionar", command=self._add_cliente).grid(row=3, column=0, columnspan=2, pady=10)

        self.tree_clientes = ttk.Treeview(self.frame_clientes, columns=("id", "nome", "email", "telefone"), show='headings')
        self.tree_clientes.heading("id", text="ID")
        self.tree_clientes.heading("nome", text="Nome")
        self.tree_clientes.heading("email", text="Email")
        self.tree_clientes.heading("telefone", text="Telefone")
        self.tree_clientes.column("id", width=50, anchor="center")
        self.tree_clientes.column("nome", width=250)
        self.tree_clientes.column("email", width=200)
        self.tree_clientes.column("telefone", width=150)
        self.tree_clientes.pack(padx=10, pady=10, fill="both", expand=True)
        
        self._load_clientes()

    def _add_cliente(self):
        nome = self.entry_nome_cliente.get()
        email = self.entry_email_cliente.get()
        telefone = self.entry_tel_cliente.get()

        if not nome:
            messagebox.showwarning("Atenção", "O nome do cliente é obrigatório.")
            return

        query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor = self.db.execute_query(query, (nome, email, telefone))

        if cursor:
            self.db.commit()
            messagebox.showinfo("Sucesso", "Cliente adicionado!")
            self.entry_nome_cliente.delete(0, 'end')
            self.entry_email_cliente.delete(0, 'end')
            self.entry_tel_cliente.delete(0, 'end')
            self._load_clientes()

    def _load_clientes(self):
        for i in self.tree_clientes.get_children():
            self.tree_clientes.delete(i)
        
        query = "SELECT id, nome, email, telefone FROM clientes ORDER BY nome"
        cursor = self.db.execute_query(query)
        
        if cursor:
            for row in cursor.fetchall():
                self.tree_clientes.insert('', tk.END, values=row)

    def _setup_produtos_tab(self):
        
        frame_input = ttk.LabelFrame(self.frame_produtos, text="Novo Produto")
        frame_input.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_input, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome_produto = ttk.Entry(frame_input, width=40)
        self.entry_nome_produto.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_input, text="Preço (R$):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_preco_produto = ttk.Entry(frame_input, width=40)
        self.entry_preco_produto.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_input, text="Estoque:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_estoque_produto = ttk.Entry(frame_input, width=40)
        self.entry_estoque_produto.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame_input, text="Adicionar Produto", command=self._add_produto).grid(row=3, column=0, columnspan=2, pady=10)

        self.tree_produtos = ttk.Treeview(self.frame_produtos, columns=("id", "nome", "preco", "estoque"), show='headings')
        self.tree_produtos.heading("id", text="ID")
        self.tree_produtos.heading("nome", text="Nome")
        self.tree_produtos.heading("preco", text="Preço")
        self.tree_produtos.heading("estoque", text="Estoque")
        self.tree_produtos.column("id", width=50, anchor="center")
        self.tree_produtos.column("nome", width=300)
        self.tree_produtos.column("preco", width=100, anchor="e")
        self.tree_produtos.column("estoque", width=100, anchor="center")
        self.tree_produtos.pack(padx=10, pady=10, fill="both", expand=True)
        
        self._load_produtos()

    def _add_produto(self):
        nome = self.entry_nome_produto.get()
        try:
            preco = float(self.entry_preco_produto.get())
            estoque = int(self.entry_estoque_produto.get())
        except ValueError:
            messagebox.showwarning("Erro", "Preço deve ser um número decimal e Estoque deve ser um número inteiro.")
            return

        if not nome or preco <= 0 or estoque < 0:
            messagebox.showwarning("Atenção", "Preencha todos os campos corretamente.")
            return

        query = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        cursor = self.db.execute_query(query, (nome, preco, estoque))

        if cursor:
            self.db.commit()
            messagebox.showinfo("Sucesso", "Produto adicionado!")
            self.entry_nome_produto.delete(0, 'end')
            self.entry_preco_produto.delete(0, 'end')
            self.entry_estoque_produto.delete(0, 'end')
            self._load_produtos()

    def _load_produtos(self):
        for i in self.tree_produtos.get_children():
            self.tree_produtos.delete(i)
        
        query = "SELECT id, nome, preco, estoque FROM produtos ORDER BY nome"
        cursor = self.db.execute_query(query)
        
        if cursor:
            for row in cursor.fetchall():
                row_formatted = (row[0], row[1], f"R$ {row[2]:.2f}", row[3])
                self.tree_produtos.insert('', tk.END, values=row_formatted)
                
    def _setup_vendas_tab(self):
        ttk.Label(self.frame_vendas, text="Funcionalidade de Registro de Vendas e Histórico", font=("Arial", 14, "bold")).pack(pady=20)
        ttk.Label(self.frame_vendas, text="Esta aba exige lógica de negócio mais complexa (transações de venda, carrinho e subtotais).").pack()
        ttk.Label(self.frame_vendas, text="Você pode implementar aqui a interface de seleção de cliente, adição de produtos ao carrinho e finalização da venda.").pack()
        
    def on_closing(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair? A conexão com o DB será encerrada."):
            self.db.close()
            self.destroy()

if __name__ == "__main__":

    app = AppVendas()
    if app.db.conn: 
        app.protocol("WM_DELETE_WINDOW", app.on_closing)
        app.mainloop()
