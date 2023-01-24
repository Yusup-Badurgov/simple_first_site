from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return f"""
    <h1>Привет, я будущий калькулятор International Cargo<h1>
    <h2>У меня такое страшненькое название сайта и я медленный, потому что никто не подкинул монету пока<h2>
    """

if __name__ == "__main__":
    app.run()