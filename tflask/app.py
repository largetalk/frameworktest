from __future__ import print_function
from flask import Flask, url_for
from flask import render_template
from flask import request
import time
import argparse
app = Flask(__name__)
app.debug=False

@app.route('/')
def hello_world():
    js_url = url_for('static', filename='jquery.js')
    return '<html><head><title>flasktest</title><script src=%s></script></head><body>Hello World!</body></html>'%js_url

@app.route('/hello/')
@app.route('/hello/<username>')
def show_user_profile(username=None):
    return render_template('hello.html', name=username)

@app.route('/hello1/<int:ppid>')
def show_user_id(ppid):
    return 'hello ppid %s'%ppid

@app.route('/projects/')
def projects():
    return 'projects'

@app.route('/calc')
def calc():
    t1 = time.time()
    for i in range(100000):
        a = 'a'*100
        b = 'b'*100
        c = a+b
    t2 = (time.time() - t1) * 1000
    return 'hello from flask: %s ms'%t2

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login post'
    else:
        return 'login get'

@app.route('/trender')
def trender():
    return render_template('loop_t.html')

@app.route('/empty')
def empty():
    return render_template('plain.html')

@app.route('/bigrender')
def bigrender():
    return render_template('big_render.html')

#with app.test_request_context():
#    print(url_for('show_user_profile', username='xxxxxx'))

if __name__ == '__main__':
#    app.run(host='0.0.0.0')

    parser = argparse.ArgumentParser(description='flask wsgi args.')
    parser.add_argument('--port', dest='port',  
            action='store', type=int, metavar='P', default=5000,
            help='wsgi start port.[default 5000]')
    args = parser.parse_args()
    port = args.port

    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
