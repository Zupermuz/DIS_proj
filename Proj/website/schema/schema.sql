DROP TABLE IF EXISTS users;

CREATE TABLE users (
    usrid VARCHAR PRIMARY KEY,
    usrname VARCHAR(20),
    pass TEXT,
    fridgelist TEXT[]
);

DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    rid SERIAL PRIMARY KEY,
    recipename VARCHAR,
    ingr TEXT[],
    rcplink TEXT
);