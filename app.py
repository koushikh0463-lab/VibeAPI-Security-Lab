"""VibeAPI - intentionally vulnerable local scanner lab. LOCALHOST ONLY."""
import traceback, platform, sys
from flask import Flask, jsonify, render_template
import config

app = Flask(__name__)
USERS = [
    {"id": 1, "username": "admin", "email": "admin@example.test", "password_hash": "21232f297a57a5a743894a0e4a801fc3",
     "api_token": "tok_admin_FAKE_1111", "ssn": "000-00-0001", "role": "admin", "is_active": True},
    {"id": 2, "username": "carol", "email": "carol@example.test", "password_hash": "5f4dcc3b5aa765d61d8327deb882cf99",
     "api_token": "tok_carol_FAKE_2222", "ssn": "000-00-0002", "role": "user", "is_active": True},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/users")
def users():
    # VA-02: intentionally exposes all fields without authentication
    return jsonify(USERS)

@app.route("/api/users/<int:uid>")
def user(uid):
    u = next((x for x in USERS if x["id"] == uid), None)
    return jsonify(u) if u else (jsonify(error="not found"), 404)

@app.route("/api/debug/config")
def debug_config():
    # VA-03: intentionally exposes configuration and runtime details
    return jsonify({k: getattr(config, k) for k in dir(config) if k.isupper()},
                   python=sys.version, platform=platform.platform(),
                   routes=[str(r) for r in app.url_map.iter_rules()])

@app.route("/api/crash")
def crash():
    return 1 / 0

@app.errorhandler(Exception)
def verbose(e):
    # VA-03: verbose exception details intentionally returned to client
    return jsonify(error=str(e), trace=traceback.format_exc(), debug=config.DEBUG), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=False)
