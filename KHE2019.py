from flask import Flask, render_template, request, make_response, redirect
import storage
from outlet_chatter import OutletChatter


app = Flask(__name__)

@app.route("/toggle-zone")
def toggle_zone():
    return render_template("toggle_zone.html")

"""""

Routes to set up zones and outlets

"""""

@app.route("/add-off", methods=['GET', 'POST'])
def add_off():
    if request.method == "GET":
        Response = make_response(render_template("add_off.html"))
        return Response
    elif request.method == "POST":
        Chatter = OutletChatter()
        OffId = Chatter.GetOffId()
        print(OffId)

        Response = make_response(redirect("/add-off"))
        return Response

@app.route("/add-on", methods=['GET', 'POST'])
def add_on():
    if request.method == "GET":
        Response = make_response(render_template("add_on.html"))
        return Response
    elif request.method == "POST":
        Chatter = OutletChatter()
        OnId = Chatter.GetOnId()
        print(OnId)

        Response = make_response(redirect("/add-off"))
        return Response

@app.route("/add-zone", methods=['GET', 'POST'])
def add_zone():
    if request.method == "GET":
        Response = make_response(render_template("add_zone.html"))
        return Response
    elif request.method == "POST":
        ZoneName = request.form.get("zonename")

        AddZone = storage.AddZone(ZoneName)

        if AddZone is True:
            Response = make_response(redirect("/add_on"))
        else:
            Message = "Zone was not successfully added."
            Response = make_response(render_template("add_on.html", Message=Message))

        return Response

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()