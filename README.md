Création de la Base de données : 

CREATE TABLE "Reponse" (
    "id"    INTEGER UNIQUE,
    "id_question"    INTEGER,
    "text"    TEXT,
    "isCorrect"    INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("id_question") REFERENCES "Question"("id")
);

CREATE TABLE "Question" (
	"id"	INTEGER NOT NULL,
	"position"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"text"	TEXT NOT NULL,
	"image"	TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE "Participation" (
    "id"    INTEGER,
    "playerName"    TEXT NOT NULL,
    "score"    INTEGER NOT NULL,
    PRIMARY KEY("id")
);