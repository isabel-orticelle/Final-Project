# Final-Project
### Isabel Orticelle Final Project

I made a book depository so that an average user can add, delete, and edit books to this database for various purposes such as to keep track of various author's book or to keep track of the books he or she has read. The Author table is a one to many relationship in which one author can have many books.

### Database Design
Author Table

Author ID |  Author Name | About
------------|---------------|-------------
1 | Stephen King |Stephen Edwin King is an American author of horror, supernatural fiction, suspense, science fiction, and fantasy
2 | JK Rowling |JK Rowling is a British novelist, philanthropist, film producer, television producer and screenwriter who is best known for writing the Harry Potter fantasy series
3 | F. Scott Fitzgerald | Francis Scott Key Fitzgerald was an American writer, whose works illustrate the Jazz Age. While he achieved limited success in his lifetime, he is now widely regarded as one of the greatest American writers of the 20th century.

Book Table

Book ID | Title(Name) | Year | Author | Summary
---------|-------|-------|------|------------
1 | It | 1986 | Stephen King | Seven young outcasts in Derry, Maine, are about to face their worst nightmare -- an ancient, shape-shifting evil that emerges from the sewer every 27 years to prey on the town's children. Banding together over the course of one horrifying summer, the friends must overcome their own personal fears to battle the murderous, bloodthirsty clown known as Pennywise.
2 | Harry Potter and the Sorcerer's Stone | 1997 | JK Rowling | A boy learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths
3 | The Great Gatsby| 1925 | F Scott Fitzgerald | The Great Gatsby is the story of eccentric millionaire Jay Gatsby as told by Nick Carraway, a Midwesterner who lives on Long Island but works in Manhattan. Gatsby's enormous mansion is adjacent to Carraway's modest home, and Carraway becomes curious about his neighbor after being invited to one of his famous parties

### Instructions

In order to run our website, you'll need to follow a few simple steps to get it up and running in your web browser of choice.

- **Windows Instructions**

    1. Go to my GitHub https://github.com/isabel-orticelle and click on the Final-Project repo and clone the repo so that you can store it locally.

    2. Open Powershell

    3. Type the following command to open the project directory:
            cd group-assignment

    4. Type the following command to create Virtualenv so that we can setup a virtual environment:
            pip install virtualenv

    5. Create the venv folder:
            virtualenv venv

    6. Activate the virtual environment:
            venv/scripts/activate

    7. Install the requirements for the project:
            pip install -r requirements.txt

    8. Initialize the database:
            python manage.py deploy

    9. Run the server:
            python manage.py runserver -d

    10. View the website in your web browser by typing your IP address into the address bar.

- **Mac Instructions**
  1. Go to my GitHub https://github.com/isabel-orticelle and click on the Final-Project repo and clone the repo so that you can store it locally.

  2. Open the Command Line

  3. Type the following command to open the project directory:
          cd group-assignment

  4. Type the following command to create Virtualenv so that we can setup a virtual environment:
          sudo pip install virtualenv

  5. Create the venv folder:
          virtualenv venv

  6. Activate the virtual environment:
          venv/bin/activate

  7. Install the requirements for the project:
          pip install -r requirements.txt

  8. Initialize the database:
          python manage.py deploy

  9. Run the server:
          python manage.py runserver -d

  10. View the website in your web browser by typing your IP address into the address bar.
