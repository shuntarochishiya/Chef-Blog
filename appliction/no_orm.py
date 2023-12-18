from application import init_database


def create_tables():
    conn = init_database()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Forum_user (
        Identifier INTEGER NOT NULL,
        Full_name VARCHAR(50) NOT NULL,
        Reg_date TIMESTAMP NOT NULL,
        User_role VARCHAR(15) NOT NULL,
        Email VARCHAR(120) NOT NULL,
        Passwd VARCHAR(60) NOT NULL,
        Bio VARCHAR(200),
        PRIMARY KEY (Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipe (
        Title VARCHAR(100) NOT NULL UNIQUE,
        Callories INTEGER,
        Proteins INTEGER,
        Lipids INTEGER,
        Carbohydrates INTEGER,
        Identifier INTEGER NOT NULL,
        Datetime TIMESTAMP NOT NULL,
        Post_text TEXT NOT NULL,
        Creator_id INTEGER NOT NULL,
        PRIMARY KEY (Identifier),
        FOREIGN KEY (Creator_id) REFERENCES Forum_user(Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Feedback (
        Identifier INTEGER NOT NULL,
        Datetime TIMESTAMP NOT NULL,
        Comm_text VARCHAR(1000) NOT NULL,
        Recipe_id INTEGER NOT NULL,
        Author_id INTEGER NOT NULL,
        PRIMARY KEY (Identifier),
        FOREIGN KEY (Author_id) REFERENCES Forum_user(Identifier),
        FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cuisine (
        Title VARCHAR(50) NOT NULL UNIQUE,
        Identifier INTEGER NOT NULL,
        PRIMARY KEY (Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Category (
        Title VARCHAR(50) NOT NULL UNIQUE,
        Identifier INTEGER NOT NULL,
        PRIMARY KEY (Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ingredient(
        Title VARCHAR(50) NOT NULL UNIQUE,
        Category VARCHAR(20) NOT NULL,
        Expiration_date INTEGER,
        Identifier INTEGER NOT NULL,
        PRIMARY KEY (Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipe_categories(
        Recipe_id INTEGER NOT NULL,
        Category_id INTEGER NOT NULL,
        FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
        FOREIGN KEY (Category_id) REFERENCES Category(Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipe_cuisines(
        Recipe_id INTEGER NOT NULL,
        Cuisine_id INTEGER NOT NULL,
        FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
        FOREIGN KEY (Cuisine_id) REFERENCES Cuisine(Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipe_ingredients(
        Recipe_id INTEGER NOT NULL,
        Ingredient_id INTEGER NOT NULL,
        Amount INTEGER NOT NULL,
        FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier),
        FOREIGN KEY (Ingredient_id) REFERENCES Ingredient(Identifier)
    );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Likes(
        Identifier INTEGER NOT NULL,
        Author_id INTEGER NOT NULL,
        Recipe_id INTEGER NOT NULL,
        PRIMARY KEY (Identifier),
        FOREIGN KEY (Author_id) REFERENCES Forum_user(Identifier),
        FOREIGN KEY (Recipe_id) REFERENCES Recipe(Identifier)
    );
    ''')

    conn.commit()
    cursor.close()
    conn.close()
