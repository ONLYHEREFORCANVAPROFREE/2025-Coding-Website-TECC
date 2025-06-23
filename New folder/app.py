"""Flask web app for introducing ASHSGamer students."""
from flask import Flask, render_template
from ASHSGamer import ASHSGamer


app = Flask(__name__)

#these lines will route index.html
@app.route('/')
def index():
    """Render index page with one student's introduction."""
    student1 = ASHSGamer("email@sample.com", +64123456789)
    intro1 = student1.introduce()

    return render_template('index.html', intro1 = intro1)

@app.route('/index_fr')
def index_fr():
    """Render index_fr page with another student's introduction."""
    student1 = ASHSGamer("Aryaan", 17)
    intro1 = student1.introduce()

    student2 = ASHSGamer("Damon", 17)
    intro2 = student2.introduce()

    intros = [intro1, intro2]

    return render_template('index_fr.html', intros = intros)

@app.route('/lumfau')
def lumfau():
    """Render lumfau page with another student's introduction."""
    student1 = ASHSGamer("Aryaan", 17)
    intro1 = student1.introduce()

    student2 = ASHSGamer("Damon", 17)
    intro2 = student2.introduce()

    intros = [intro1, intro2]

    return render_template('lumfau.html', intros = intros)

app.run(debug=True)
