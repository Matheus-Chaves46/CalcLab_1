DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS admins;
CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Inserir o admin padrão
INSERT INTO admins (username, password) VALUES ('admin', 'admin123'); 