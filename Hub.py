from flask import Flask
from mcstatus import MinecraftServer

app = Flask(__name__)






@app.route('/')
def hello_world():
    return 'Welcome!'

@app.route('/url/<arg1>')
def url(arg1):

    server = MinecraftServer.lookup(arg1)
    status = server.status()
    latency = server.ping()
    query = server.query()
    return "The server has {0} players and responded to the request in {1} ms | The server response time is {2} ms ".format(status.players.online, status.latency, latency)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("80"), debug=True)
