

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
