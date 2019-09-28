from flask import Flask, render_template, request, make_response, redirect


app = Flask(__name__)

@app.route("/toggle-zone")
def toggle_zone():
    return render_template("toggle_zone.html")

@app.route("/add-zone", methods=['GET', 'POST'])
def add_zone():
    if request.method == "GET":
        Response = make_response(render_template("add_zone.html"))
        return Response
    elif request.method == "POST":
        ZoneName = request.form.get("zonename")

        print(ZoneName)

        Message = "Zone was successfully added."
        Response = make_response(render_template("add_zone.html", Message=Message))

        return Response

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()