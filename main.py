from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# بيانات أولية (للتجربة)
accounts = [
    {"name": "Account 1", "image": "https://via.placeholder.com/150", "link": "https://facebook.com"},
    {"name": "Account 2", "image": "https://via.placeholder.com/150", "link": "https://twitter.com"},
]

@app.route("/")
def index():
    return render_template("index.html", accounts=accounts)

@app.route("/add_account", methods=["POST"])
def add_account():
    name = request.form["name"]
    image = request.form["image"]
    link = request.form["link"]
    accounts.append({"name": name, "image": image, "link": link})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
