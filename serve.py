from flask import Flask, render_template
import asyncio
import websockets

def serve_static(**kargs):
  pulse_server = Flask(__name__)

  @pulse_server.route("/")
  def index():
    return render_template("index.html")

  pulse_server.run(**kargs)


if __name__ == "__main__":
  serve_static(debug=True)
