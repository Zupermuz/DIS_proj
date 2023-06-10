DROP TABLE IF EXISTS users;

CREATE TABLE users (
    usrid INTEGER PRIMARY KEY AUTOINCREMENT,
    usrname VARCHAR(20),
    pass VARCHAR(20),
    fridgelist TEXT[]
);

DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    rid INTEGER PRIMARY KEY AUTOINCREMENT,
    recipename VARCHAR,
    ingr TEXT[],
    instrlist TEXT[]
);