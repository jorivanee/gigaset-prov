from flask import Flask


app = Flask(__name__)


@app.route("/prov/<string:mac>.xml")
def get_prov_file(mac):
    return mac

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")