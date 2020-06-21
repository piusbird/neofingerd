CREATE TABLE lusers (
uid INTEGER PRIMARY KEY NOT NULL,
type INTEGER DEFAULT 255,
unix_name VARCHAR(32) NOT NULL UNIQUE,
data BLOB DEFAULT 'their a really nice person'
);

