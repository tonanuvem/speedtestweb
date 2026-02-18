import speedtest
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates")

def format_speed(bps):
    if bps >= 1_000_000_000:
        return f"{bps / 1_000_000_000:.2f} Gbps"
    elif bps >= 1_000_000:
        return f"{bps / 1_000_000:.2f} Mbps"
    elif bps >= 1_000:
        return f"{bps / 1_000:.2f} Kbps"
    else:
        return f"{bps:.2f} bps"

def process_request():
    s = speedtest.Speedtest()
    s.get_servers([])
    s.get_best_server()
    s.download()
    s.upload()

    results = s.results.dict()

    return {
        "download": format_speed(results["download"]),
        "upload": format_speed(results["upload"])
    }

@app.route("/")
def home():
    # Renderiza a página imediatamente
    return render_template("index.html")

@app.route("/run-test")
def run_test():
    try:
        result = process_request()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
