from flask import Flask
from flask import render_template
from database import get_all_cats

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def cat_id_route(id):
	return render_template(
		'cat.html', c = id )


if __name__ == '__main__':
   app.run(debug = True)
