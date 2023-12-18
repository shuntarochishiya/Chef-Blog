from application import create_app, db
from no_orm import create_tables

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    create_tables()
    app.run(debug=True)
