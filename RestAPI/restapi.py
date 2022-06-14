from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def tem_min_average_price():
    return jsonify({'result' : 'OK'})

@app.route("/liveness", methods=["GET"])
def liveness():
    return "OK"


@app.route("/readiness", methods=["GET"])
def readinesshealth():
    return "OK"

if __name__ == '__main__':
    app.run()