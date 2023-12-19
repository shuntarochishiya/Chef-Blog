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
    def get_by_id(cuisine_id):
        conn = init_database()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Cuisine WHERE Identifier = %s LIMIT 1', [cuisine_id])
        cuisine_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if cuisine_data:
            return Database(*cuisine_data)
        return None
