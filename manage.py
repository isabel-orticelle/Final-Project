from flask_script import Manager
from bookdepo import app, db, Author, Book

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    sk = Author(name='Stepthen King', about='Coldplay is a British rock band.')
    jkr = Author(name='JK Rowling', about='Maroon 5 is an American pop rock band.')
    book1 = Book(name='Yellow', year=2000, summary="Look at the stars", author=sk)
    book2 = Book(name='Sugar', year=2014, summary="I'm hurting, baby, I'm broken down", author=jkr)
    db.session.add(sk)
    db.session.add(jkr)
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
