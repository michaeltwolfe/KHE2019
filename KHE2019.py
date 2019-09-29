  
from flask import Flask, render_template, request, make_response, redirect
import storage
from outlet_chatter import OutletChatter


app = Flask(__name__)

"""""

Routes to set up zones and outlets

"""""

@app.route("/add-off", methods=['GET', 'POST'])
def add_off():
    if request.method == "GET":
        Zones = storage.GetZones()

        Response = make_response(render_template("add_off.html", Zones=Zones))
        return Response
    elif request.method == "POST":
        OutletName = request.form.get("outletname")
        OffSelect = request.form.get("addoff")

        Chatter = OutletChatter()
        OffId = Chatter.GetOffId()
        
        storage.AddOffId(OffSelect, OffId, OutletName)

        Response = make_response(redirect("/add-off"))
        return Response

@app.route("/add-on", methods=['GET', 'POST'])
def add_on():
    if request.method == "GET":
        Zones = storage.GetZones()

        Response = make_response(render_template("add_on.html", Zones=Zones))
        return Response
    elif request.method == "POST":
        OutletName = request.form.get("outletname")
        OnSelect = request.form.get("addon")

        Chatter = OutletChatter()
        OnId = Chatter.GetOnId()
        
        storage.AddOnId(OnSelect, OnId, OutletName)

        Response = make_response(redirect("/add-off"))
        return Response

@app.route("/add-zone", methods=['GET', 'POST'])
def add_zone():
    if request.method == "GET":
        Response = make_response(render_template("add_zone.html"))
        return Response
    elif request.method == "POST":
        ZoneName = request.form.get("zonename")

        storage.AddZone(ZoneName)

        Response = make_response(redirect("/"))

        return Response

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        ZoneInformation = storage.GetLandingPageInformation()

        Response = make_response(render_template("index.html", Information=ZoneInformation))
        return Response
    elif request.method == 'POST':
        values = request.form.getlist("OnOffSwitch")
        for item in values:
            print(item)
        return render_template('index.html')

if __name__ == '__main__':
    app.run()