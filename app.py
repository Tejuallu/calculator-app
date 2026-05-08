from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        choice = request.form["choice"]

        if choice == '1':
            result = num1 + num2

        elif choice == '2':
            result = num1 - num2

        elif choice == '3':
            result = num1 * num2

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

        else:
            result = "Invalid Input"

    return render_template("index.html", result=result)

app = app
