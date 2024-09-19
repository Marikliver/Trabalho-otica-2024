import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Função para conectar ao banco de dados SQLite e criar tabelas se não existirem
def conectar_banco():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produto (
            Id_produto INTEGER PRIMARY KEY,
            Nome_Produto TEXT,
            Quantidade INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Gaveta (
            Id_Loc INTEGER PRIMARY KEY,
            fk_Produto_Id_produto INTEGER,
            Num_Gav INTEGER,
            FOREIGN KEY (fk_Produto_Id_produto) REFERENCES Produto (Id_produto) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Marca (
            Id_Marca INTEGER PRIMARY KEY,
            Nome_Mar TEXT,
            fk_Produto_Id_produto INTEGER,
            FOREIGN KEY (fk_Produto_Id_produto) REFERENCES Produto (Id_produto) ON DELETE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            Id_Cliente INTEGER PRIMARY KEY,
            Nome_Cliente TEXT,
            CPF INTEGER,
            Telefone INTEGER,
            Email TEXT
        )
    ''')
    conn.commit()
    return conn

# Função para adicionar um produto e associar uma marca e uma gaveta
def adicionar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    nome_marca = entry_marca.get()
    num_gaveta = entry_gaveta.get()

    if nome and quantidade.isdigit() and nome_marca and num_gaveta.isdigit():
        cursor = conn.cursor()

        # Inserir o produto
        cursor.execute("INSERT INTO Produto (Nome_Produto, Quantidade) VALUES (?, ?)", (nome, int(quantidade)))
        produto_id = cursor.lastrowid

        # Inserir a marca e associar ao produto
        cursor.execute("INSERT INTO Marca (Nome_Mar, fk_Produto_Id_produto) VALUES (?, ?)", (nome_marca, produto_id))

        # Inserir a gaveta e associar ao produto
        cursor.execute("INSERT INTO Gaveta (fk_Produto_Id_produto, Num_Gav) VALUES (?, ?)", (produto_id, int(num_gaveta)))

        conn.commit()

        messagebox.showinfo("Sucesso", "Produto, marca e gaveta adicionados com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_marca.delete(0, tk.END)
        entry_gaveta.delete(0, tk.END)
        listar_produtos()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos corretamente.")

# Função para listar produtos com suas marcas e gavetas
def listar_produtos():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.Id_produto, p.Nome_Produto, p.Quantidade, m.Nome_Mar, g.Num_Gav
        FROM Produto p
        LEFT JOIN Marca m ON p.Id_produto = m.fk_Produto_Id_produto
        LEFT JOIN Gaveta g ON p.Id_produto = g.fk_Produto_Id_produto
    ''')
    rows = cursor.fetchall()
    listbox_produtos.delete(0, tk.END)
    for row in rows:
        listbox_produtos.insert(tk.END, row)

# Função para remover produto
def remover_produto():
    try:
        selecionado = listbox_produtos.curselection()[0]
        produto = listbox_produtos.get(selecionado)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produto WHERE Id_produto = ?", (produto[0],))
        conn.commit()
        listar_produtos()
        messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
    except IndexError:
        messagebox.showwarning("Erro", "Por favor, selecione um produto para remover.")

# Função para editar produto, marca e gaveta
def editar_produto():
    try:
        selecionado = listbox_produtos.curselection()[0]
        produto = listbox_produtos.get(selecionado)

        # Obtendo novos valores
        novo_nome = simpledialog.askstring("Editar", "Novo nome do produto:", initialvalue=produto[1])
        nova_quantidade = simpledialog.askinteger("Editar", "Nova quantidade:", initialvalue=produto[2])
        nova_marca = simpledialog.askstring("Editar", "Nova marca:", initialvalue=produto[3])
        nova_gaveta = simpledialog.askinteger("Editar", "Nova gaveta:", initialvalue=produto[4])

        if novo_nome and nova_quantidade is not None and nova_marca and nova_gaveta is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE Produto SET Nome_Produto = ?, Quantidade = ? WHERE Id_produto = ?",
                           (novo_nome, nova_quantidade, produto[0]))
            cursor.execute("UPDATE Marca SET Nome_Mar = ? WHERE fk_Produto_Id_produto = ?",
                           (nova_marca, produto[0]))
            cursor.execute("UPDATE Gaveta SET Num_Gav = ? WHERE fk_Produto_Id_produto = ?",
                           (nova_gaveta, produto[0]))
            conn.commit()
            listar_produtos()
            messagebox.showinfo("Sucesso", "Produto, marca e gaveta atualizados com sucesso!")
    except IndexError:
        messagebox.showwarning("Erro", "Por favor, selecione um produto para editar.")

# Função para pesquisar produtos
def pesquisar_produto():
    termo = entry_pesquisa.get()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.Id_produto, p.Nome_Produto, p.Quantidade, m.Nome_Mar, g.Num_Gav
        FROM Produto p
        LEFT JOIN Marca m ON p.Id_produto = m.fk_Produto_Id_produto
        LEFT JOIN Gaveta g ON p.Id_produto = g.fk_Produto_Id_produto
        WHERE p.Nome_Produto LIKE ?
    ''', ('%' + termo + '%',))
    rows = cursor.fetchall()
    listbox_produtos.delete(0, tk.END)
    for row in rows:
        listbox_produtos.insert(tk.END, row)

# Conectar ao banco de dados
conn = conectar_banco()

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Gerenciamento de Produtos")
janela.configure(bg="#548c82")  # Cor de fundo da janela

frame = tk.Frame(janela, bg="#548c82")  # Cor de fundo do frame
frame.pack(pady=20)

# Widgets de entrada
tk.Label(frame, text="Nome do Produto:", bg="#548c82", fg="white", font=("Arial", 12)).grid(row=0, column=0)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Quantidade:", bg="#548c82", fg="white", font=("Arial", 12)).grid(row=1, column=0)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Marca:", bg="#548c82", fg="white", font=("Arial", 12)).grid(row=2, column=0)
entry_marca = tk.Entry(frame)
entry_marca.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Número da Gaveta:", bg="#548c82", fg="white", font=("Arial", 12)).grid(row=3, column=0)
entry_gaveta = tk.Entry(frame)
entry_gaveta.grid(row=3, column=1, padx=10, pady=5)

# Botão para adicionar produto
botao_adicionar = tk.Button(frame, text="Adicionar Produto", command=adicionar_produto, bg="#fcfade", fg="black", font=("Arial", 12))
botao_adicionar.grid(row=4, columnspan=2, pady=10)

# Campo de entrada para pesquisa
tk.Label(janela, text="Pesquisar Produto:", bg="#548c82", fg="white", font=("Arial", 12)).pack()
entry_pesquisa = tk.Entry(janela)
entry_pesquisa.pack(pady=5)

# Botão para pesquisar produto
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=pesquisar_produto, bg="#fcfade", fg="black", font=("Arial", 12))
botao_pesquisar.pack(pady=5)

# Lista de produtos
listbox_produtos = tk.Listbox(janela, width=80)
listbox_produtos.pack(pady=20)

# Botões de ações
botao_remover = tk.Button(janela, text="Remover Produto", command=remover_produto, bg="#fcfade", fg="black", font=("Arial", 12))
botao_remover.pack(pady=5)

botao_editar = tk.Button(janela, text="Editar Produto", command=editar_produto, bg="#fcfade", fg="black", font=("Arial", 12))
botao_editar.pack(pady=5)

# Carregar lista de produtos ao iniciar
listar_produtos()

janela.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
conn.close()
