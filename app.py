from flask import Flask, render_template_string
import psutil
from datetime import datetime

app = Flask(__name__)

# HTML Template (The UI)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps System Monitor</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: white; text-align: center; }
        .card { background: #1e1e1e; padding: 20px; margin: 20px; border-radius: 10px; display: inline-block; min-width: 200px; }
        .value { font-size: 2em; color: #00ff00; }
    </style>
</head>
<body>
    <h1>Server Health Dashboard</h1>
    <div class="card">
        <h3>CPU Usage</h3>
        <div class="value">{{ cpu }}%</div>
    </div>
    <div class="card">
        <h3>RAM Usage</h3>
        <div class="value">{{ ram }}%</div>
    </div>
    <p>Last Update: {{ time }}</p>
    <script>setTimeout(function(){ location.reload(); }, 5000);</script>
</body>
</html>
"""

@app.route('/')
def index():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    time_now = datetime.now().strftime("%H:%M:%S")
    return render_template_string(HTML_TEMPLATE, cpu=cpu, ram=ram, time=time_now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)