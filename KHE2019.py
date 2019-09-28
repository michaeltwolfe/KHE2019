from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        values = request.form.getlist("OnOffSwitch")
        for item in values:
            print(item)
        return render_template('index.html')

if __name__ == '__main__':
    app.run()