from flask import Flask, render_template, request
import os
import mysql.connector

app = Flask(__name__, template_folder=".")


# Cloud MySQL connection
db = mysql.connector.connect(
    host=os.environ["MYSQLHOST"],
    port=int(os.environ["MYSQLPORT"]),
    user=os.environ["MYSQLUSER"],
    password=os.environ["MYSQLPASSWORD"],
    database=os.environ["MYSQLDATABASE"]
)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        course = request.form["course"]

        cursor = db.cursor()

        sql = """
        INSERT INTO students (name, email, age, course)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, email, age, course)

        cursor.execute(sql, values)
        db.commit()

        cursor.close()

        return "Student Registered Successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)