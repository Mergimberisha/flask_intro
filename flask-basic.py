from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author' : 'Mergim Berisha ',
        'title' : 'Blog Post 1 - flask & bootstrap',
        'content' : 'First post content',
        'date_posted' : '18 June, 2020'
    },
    {
        'author' : 'Mergim Berisha',
        'title' : 'Blog Post 2 - CSS components',
        'content' : 'Second post content',
        'date_posted' : '18 June, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug = True)