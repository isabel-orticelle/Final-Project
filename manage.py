from flask_script import Manager
from bookdepo import app, db, Author, Book

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    sk = Author(name='Stepthen King', about='Stephen Edwin King is an American author of horror, supernatural fiction, suspense, science fiction, and fantasy.')
    jkr = Author(name='JK Rowling', about='JK Rowling is a British novelist, philanthropist, film producer, television producer and screenwriter who is best known for writing the Harry Potter fantasy series.')
    fsf= Author(name='F. Scott Fitzgerald', about='Francis Scott Key Fitzgerald was an American writer, whose works illustrate the Jazz Age. While he achieved limited success in his lifetime, he is now widely regarded as one of the greatest American writers of the 20th century.')
    book1 = Book(name='It', year=1986, summary="Seven young outcasts in Derry, Maine, are about to face their worst nightmare -- an ancient, shape-shifting evil that emerges from the sewer every 27 years to prey on the town's children. Banding together over the course of one horrifying summer, the friends must overcome their own personal fears to battle the murderous, bloodthirsty clown known as Pennywise.", author=sk)
    book2 = Book(name="Harry Potter and the Sorcerer's Stone", year=1997, summary="A boy learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.", author=jkr)
    book3 = Book(name='The Great Gatsby', year=1925, summary="The Great Gatsby is the story of eccentric millionaire Jay Gatsby as told by Nick Carraway, a Midwesterner who lives on Long Island but works in Manhattan. Gatsby's enormous mansion is adjacent to Carraway's modest home, and Carraway becomes curious about his neighbor after being invited to one of his famous parties.", author=fsf)
    db.session.add(sk)
    db.session.add(jkr)
    db.session.add(fsf)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
