from flask import Flask, render_template
import generateTweets

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = generateTweets.get_Single_Tweet()
    return render_template('home.html', tweet=a)


if __name__ == '__main__':
    app.run()
