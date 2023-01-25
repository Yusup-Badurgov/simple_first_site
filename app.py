from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def main_page():
    return render_template('index.html', sitename='InterCargoCalculate')


if __name__ == "__main__":
    application.run()
