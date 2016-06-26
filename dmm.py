from gevent.wsgi import WSGIServer
from twitter import app

app.run(debug=True)
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
