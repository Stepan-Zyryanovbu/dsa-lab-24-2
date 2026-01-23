from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

instances = [
    ("127.0.0.1", 5001, True),
    ("127.0.0.1", 5002, True),
    ("127.0.0.1", 5003, True)
]

current_index = 0

# health check без потоков
def check_all_instances():
    for i, (ip, port, _) in enumerate(instances):
        try:
            resp = requests.get(f"http://{ip}:{port}/health", timeout=2)
            instances[i] = (ip, port, resp.status_code == 200)
        except:
            instances[i] = (ip, port, False)

# Round Robin
def get_next_instance():
    global current_index
    active_instances = [i for i in instances if i[2]]
    if not active_instances:
        return None
    instance = active_instances[current_index % len(active_instances)]
    current_index += 1
    return instance

@app.route('/health')
def health():
    check_all_instances()  # проверяем при каждом запросе
    return jsonify({
        "instances": [
            {"ip": ip, "port": port, "active": active}
            for ip, port, active in instances
        ]
    })

@app.route('/process')
def process():
    instance = get_next_instance()
    if not instance:
        return jsonify({"error": "No active instances"}), 503
    ip, port, _ = instance
    try:
        resp = requests.get(f"http://{ip}:{port}/process", timeout=3)
        print(resp)
        return resp.json()
    except:
        return jsonify({"error": "Instance unavailable"}), 503

#  Web UI без шаблонов
@app.route('/')
def index():
    check_all_instances()
    html = """
    <html>
    <body>
        <h2>Load Balancer</h2>
        <form action="/add" method="post">
            IP: <input name="ip"><br>
            Port: <input name="port"><br>
            <button>Add</button>
        </form>
        <h3>Instances:</h3>
        <ul>
    """
    for i, (ip, port, active) in enumerate(instances):
        html += f'<li>{ip}:{port} - {"Active" if active else "Inactive"} '
        html += f'<form action="/remove" method="post" style="display:inline;">'
        html += f'<input type="hidden" name="index" value="{i}">'
        html += '<button>Remove</button></form></li>'
    html += "</ul></body></html>"
    return html

@app.route('/add', methods=['POST'])
def add():
    ip = request.form['ip']
    port = int(request.form['port'])
    instances.append((ip, port, True))
    return f"Added {ip}:{port}. <a href='/'>Back</a>"

@app.route('/remove', methods=['POST'])
def remove():
    index = int(request.form['index'])
    if 0 <= index < len(instances):
        instances.pop(index)
    return "Removed. <a href='/'>Back</a>"

# Перехват других запросов
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    instance = get_next_instance()
    if not instance:
        return jsonify({"error": "No active instances"}), 503
    ip, port, _ = instance
    try:
        resp = requests.request(
            method=request.method,
            url=f"http://{ip}:{port}/{path}",
            headers=request.headers,
            data=request.get_data()
        )
        return resp.content, resp.status_code
    except:
        return jsonify({"error": "Proxy error"}), 500
    
    
