from flask import Flask, request, render_template


# app a flask object, but hope it the terminal the root path
app = Flask(__name__)


# home page for my website(the argument)
# this is the route directory
# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/shopping')
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)


# @app.route('/bacon', methods=['GET', 'POST'])
# def bacon():
#     if request.method == 'POST':
#         return 'You are using POST'
#     else:
#         return 'You are probably using GET'
#
#
# @app.route('/tuna')
# def tuna():
#     return '<h2> Tuna is good </h2>'
#
#
# @app.route('/profile/<username>')
# def profile(username):
#     return render_template("profile.html", username=username)
#
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return "<h2>Post ID is %s</h2>" % post_id


# it check we only run the app or only start the web server
# if this file would be import to an other file, this won't be run
if __name__ == "__main__":
    # start this app
    app.run(debug=True)
