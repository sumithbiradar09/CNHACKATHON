from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/scan", methods=["GET"])
def scan_network():
    try:
        result = subprocess.check_output(["arp", "-a"]).decode()
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
