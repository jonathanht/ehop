from flask import Flask, render_template
from app.forms import InfoForm
from app.HackUCI2020 import yelp
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=['GET','POST'])
def home():
	form = InfoForm()

	if form.is_submitted():
		print(type(form.latitude.data))
		print(type(form.longtitude.data))
		print(type(form.phonenumber.data))
		yelp(form.latitude.data, form.longtitude.data,form.phonenumber.data)
	return render_template('Ehop.html', form = form)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/ourteam')
def ourTeam():
    print('hello')
    return render_template('ourteam.html')


if __name__ == '__main__':
	app.run(debug= True)
