from application import init_database
from flask_login import UserMixin


class Database(UserMixin):
    def __init__(self, id, username, email, password, reg_date, role, bio):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.reg_date = reg_date
        self.role = role
        self.bio = bio

    def save(self):
        conn = init_database()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Forum_user (Full_name, Email, Passwd, Reg_date, User_role, Bio) VALUES (%s, %s, %s, %s, %s, %s) RETURNING Identifier
        ''', (self.username, self.email, self.password, self.reg_date, self.role, self.bio)
                       )
        self.id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_email(email):
        conn = init_database()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Forum_user WHERE Email = %s LIMIT 1', [email])
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            return Database(*user_data)
        return None

    @staticmethod
    def get_by_id(post_id):
        conn = init_database()
        cursor = conn.cursor()
        cursor.execute('SELECT post_id, ingredient_id, Amount FROM post_ingredient_association JOIN Post ON Post.id = post_ingredient_association.post_id JOIN Ingredient ON post_ingredient_association.ingredient_id = Ingredient.id WHERE post_ingredient_association.post_id = %s', [post_id])
        amount = cursor.fetchall()
        cursor.close()
        conn.close()

        return amount
