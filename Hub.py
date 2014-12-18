from flask import Flask
from flask import render_template
from mcstatus import MinecraftServer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mc/<arg1>')
def mc(arg1):

    server = MinecraftServer.lookup(arg1)
    status = server.status()
    latency = server.ping()
    query = server.query()
    return "The server has {0} players and responded to the request in {1} ms | The server response time is {2} ms ".format(status.players.online, status.latency, latency)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
