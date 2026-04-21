from flask import Flask, render_template
from threading import Thread
from core.monitor import start_monitor

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)

alerts = []

# 👇 Your processing function
def handle_log(parsed_log):
    print("New log:", parsed_log)

    if parsed_log["status"] == 401:
        print("⚠️ 401 DETECTED:", parsed_log)
        alerts.append({
            "type": "FAILED LOGIN",
            "ip": parsed_log["ip"],
            "time": parsed_log["timestamp"]
        })

# 👇 START MONITOR HERE (IMPORTANT)
Thread(
    target=start_monitor,
    args=("data/logs/sample.log", handle_log),
    daemon=True
).start()

@app.route("/")
def dashboard():
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    Thread(
        target=start_monitor,
        args=("data/logs/sample.log", handle_log),
        daemon=True
    ).start()

    app.run(debug=True, use_reloader=False)