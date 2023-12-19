DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Recipe_ingredients;
DROP TABLE IF EXISTS Recipe_cuisines;
DROP TABLE IF EXISTS Recipe_categories;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS Cuisine;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Likes;
DROP TABLE IF EXISTS Recipe;
DROP TABLE IF EXISTS Forum_user;

CREATE TABLE IF NOT EXISTS Forum_user (
	Identifier SERIAL,
	Full_name VARCHAR(50) NOT NULL,
	Reg_date TIMESTAMP NOT NULL,
	User_role VARCHAR(15) NOT NULL,
	Email VARCHAR(120) NOT NULL,
	Passwd VARCHAR(60) NOT NULL,
	Bio VARCHAR(200),
	PRIMARY KEY (Identifier)
);

CREATE TABLE Recipe (
	Title VARCHAR(100) NOT NULL UNIQUE,
	Callories INTEGER,
	Proteins INTEGER,
	Lipids INTEGER,
	Carbohydrates INTEGER,
	Identifier SERIAL,
	Datetime TIMESTAMP NOT NULL,
	Post_text TEXT NOT NULL,
	Creator_id INTEGER NOT NULL,
	PRIMARY KEY (Identifier),
	FOREIGN KEY (Creator_id) REFERENCES Forum_user(Identifier)
);

CREATE TABLE Feedback (
	Identifier SERIAL,
	Datetime TIMESTAMP NOT NULL,
	Comm_text VARCHAR(1000) NOT NULL,
	Recipe_id INTEGER NOT NULL,
	Author_id INTEGER NOT NULL,
	PRIMARY KEY (Identifier),
	FOREIGN KEY (Author_id) REFERENCES Forum_user(Identifier),
	FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier)
);

CREATE TABLE Cuisine (
	Title VARCHAR(50) NOT NULL UNIQUE,
	Identifier SERIAL,
	PRIMARY KEY (Identifier)
);

CREATE TABLE Category (
	Title VARCHAR(50) NOT NULL UNIQUE,
	Identifier INTEGER,
	PRIMARY KEY (Identifier)
);

CREATE TABLE Ingredient(
	Title VARCHAR(50) NOT NULL UNIQUE,
	Category VARCHAR(20) NOT NULL,
	Expiration_date INTEGER,
	Identifier SERIAL,
	PRIMARY KEY (Identifier)
);

CREATE TABLE Recipe_categories(
	Recipe_id INTEGER NOT NULL,
	Category_id INTEGER NOT NULL,
	FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
	FOREIGN KEY (Category_id) REFERENCES Category(Identifier)
);

CREATE TABLE Recipe_cuisines(
	Recipe_id INTEGER NOT NULL,
	Cuisine_id INTEGER NOT NULL,
	FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
	FOREIGN KEY (Cuisine_id) REFERENCES Cuisine(Identifier)
);

CREATE TABLE Recipe_ingredients(
	Recipe_id INTEGER NOT NULL,
	Ingredient_id INTEGER NOT NULL,
	Amount INTEGER NOT NULL,
	FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
	FOREIGN KEY (Ingredient_id) REFERENCES Ingredient(Identifier)
);

CREATE TABLE Likes(
	Identifier SERIAL,
	Author_id INTEGER NOT NULL,
	Recipe_id INTEGER NOT NULL,
	PRIMARY KEY (Identifier),
	FOREIGN KEY (Author_id) REFERENCES Forum_user(Identifier),
	FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier)
)