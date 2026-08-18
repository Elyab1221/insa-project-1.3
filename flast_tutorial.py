from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Elyab")

@app.route("/greet", methods=["POST"])
def greet_user():
    name = request.form["username"]
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# def get_users():
#     users = ["Elyab", "Abebe", "Sara"]
#     return jsonify(users)

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, jsonify
# app=Flask(__name__)
# @app.route("/greet/<name>")
# def greet(name):
#     return f"Hello, {name}!"
# @app.route("/api/add",methods=["POST"])
# def add_numbers():
#     data=request.get_json()
#     result=data["a"]+data["b"]
#     return jsonify({"result":result})
# if __name__=="__main__":
#     app.run(debug=True)