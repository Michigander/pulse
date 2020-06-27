from flask import Flask, render_template


if __name__ == "__main__":
    pulse_server = Flask(__name__)

    @pulse_server.route("/")
    def index():
        return render_template("index.html")

    pulse_server.run(debug=True)
