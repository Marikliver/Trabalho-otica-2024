/* Lógico_6: */

CREATE TABLE Produto (
    Id_produto NUMERIC PRIMARY KEY,
    Nome_Produto VARCHAR,
    Quantidade NUMERIC
);

CREATE TABLE Gaveta (
    Id_Loc NUMERIC PRIMARY KEY,
    fk_Produto_Id_produto NUMERIC,
    Num_Gav NUMERIC,
    CONSTRAINT FK_Gaveta_2 FOREIGN KEY (fk_Produto_Id_produto)
        REFERENCES Produto (Id_produto)
        ON DELETE CASCADE
);

CREATE TABLE Marca (
    Id_Marca NUMERIC PRIMARY KEY,
    Nome_Mar VARCHAR,
    CONSTRAINT FK_Marca_1 FOREIGN KEY (fk_Produto_Id_produto)
        REFERENCES Produto (Id_produto)
        ON DELETE CASCADE
);

CREATE TABLE Cliente (
    Id_Cliente NUMERIC PRIMARY KEY,
    Nome_Cliente VARCHAR,
    CPF NUMERIC,
    Telefone NUMERIC,
    Email VARCHAR
);

INSERT INTO Cliente (Id_Cliente, Nome_Cliente, CPF, Telefone, Email) VALUES
(1, 'Ana Silva', 12345678901, 21987654321, 'ana.silva@example.com'),
(2, 'Bruno Souza', 23456789012, 21987654322, 'bruno.souza@example.com'),
(3, 'Carla Pereira', 34567890123, 21987654323, 'carla.pereira@example.com'),
(4, 'Daniel Oliveira', 45678901234, 21987654324, 'daniel.oliveira@example.com'),
(5, 'Eduarda Lima', 56789012345, 21987654325, 'eduarda.lima@example.com'),
(6, 'Felipe Costa', 67890123456, 21987654326, 'felipe.costa@example.com'),
(7, 'Gabriela Santos', 78901234567, 21987654327, 'gabriela.santos@example.com');

INSERT INTO Produto (Id_produto, Nome_Produto, Quantidade) VALUES
(1, 'Óculos de Sol', 50),
(2, 'Óculos de Grau', 30),
(3, 'Lentes de Contato', 100),
(4, 'Armação de Óculos', 75),
(6, 'Estojos para Óculos', 40),
(7, 'Produtos de Limpeza para Óculos', 80);

INSERT INTO Gaveta (Id_Loc, fk_Produto_Id_produto, Num_Gav) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 1, 8),
(9, 2, 9),
(10, 3, 10),
(11, 4, 11),
(12, 5, 12);

INSERT INTO Marca (Id_Marca, Nome_Mar) VALUES
(1, 'Polaroid'),
(2, 'RayBan'),
(3, 'Mormaii'),
(4, 'Ana Hickmann'),
(5, 'Levis'),
(6, 'Tng');

Select * from Produto

Select * from Gaveta

Select * from Marca

Select * from Cliente