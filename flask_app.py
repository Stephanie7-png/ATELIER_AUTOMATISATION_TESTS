from flask import Flask, render_template, redirect, url_for
from tester.runner import run_tests
from storage import save_run, list_runs

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("dashboard"))

@app.route("/run")
def run():
    result = run_tests()
    save_run(result)
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template("dashboard.html", runs=runs)

@app.route("/health")
def health():
    return {
        "status": "ok",
        "message": "Application Flask active"
    }

if __name__ == "__main__":
    app.run(debug=True)
