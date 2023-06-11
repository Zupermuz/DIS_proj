DROP TABLE IF EXISTS users;

CREATE TABLE users (
    usrid SERIAL PRIMARY KEY,
    usrname VARCHAR(20),
    pass VARCHAR(20),
    fridgelist TEXT[]
);

DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    rid SERIAL PRIMARY KEY,
    recipename VARCHAR,
    ingr TEXT[],
    instrlist TEXT[]
);