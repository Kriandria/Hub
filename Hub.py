from flask import Flask
from mcstatus import MinecraftServer

app = Flask(__name__)






@app.route('/')
@app.route('/url/<arg1>')
def hello_world(arg1):

    server = MinecraftServer.lookup(arg1)
    status = server.status()
    latency = server.ping()
    query = server.query()
    return "The server has {0} players and responded to the request in {1} ms | The server response time is {2} ms ".format(status.players.online, status.latency, latency)


if __name__ == '__main__':
    app.run()
