from flask import Flask, render_template
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return 'en'
    # request.accept_language.best_match(['en', 'es', 'de'])

@app.route('/')
def index():

    anthony = gettext('Anthony')
    us_num = numbers.format_decimal(1.2345, locale='en_US')
    se_num = numbers.format_decimal(1.2345, locale = 'sv_SE')
    de_num = numbers.format_decimal(1.2345, locale= 'de_DE')

    d = date(2007, 4, 1)
    us_date = dates.format_date(d, locale = 'en_US')
    # Can delete "dates" in front of .format_date if importing format_Date from flask_babel
    de_date = format_date(d)

    dt = datetime(2008, 8, 3, 15, 30)
    us_datetime = dates.format_datetime(dt, locale = 'en_US')

    results = {'us_num' : us_num, 'se_num' : se_num, 'de_num' : de_num, 'us_date' : us_date, 'de_date' : de_date, 'us_datetime' : us_datetime}
    return render_template('index.html', results=results, anthony=anthony)

if __name__ == '__main__':
    app.run(debug=True)

# pybabel extract -F babel.cfg -o messages.pot .
# returns: ModuleNotFoundError: No module named 'jinja'
# . It's likely that either /Users/rose/Library/Python/2.7/lib/python/site-packages/ is not contained in your Python path, or Python does not have access to this directory. 