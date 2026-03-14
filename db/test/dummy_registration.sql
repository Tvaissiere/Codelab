-- NOTE: run this in your termin when psql is active to make the db and table (db first then table)

CREATE DATABASE codelab_test;

CREATE TABLE users (
    id int PRIMARY KEY;
    username varchar(255);
    email varchar(255);
    password_hash varchar(128);
)

