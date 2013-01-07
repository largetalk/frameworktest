"""
WSGI config for djapps project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import argparse

curpath = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(curpath)
sys.path.insert(0, project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djapps.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='django wsgi args.')
    parser.add_argument('--port', dest='port',  
            action='store', type=int, metavar='P', default=8041,
            help='wsgi start port.[default 8041]')
    args = parser.parse_args()
    port = args.port

    import django.core.handlers.wsgi
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web
    import tornado.wsgi

    wsgi_app = tornado.wsgi.WSGIContainer(application)
    #tornado_app = tornado.web.Application([
    #    ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
    #])
    #server = tornado.httpserver.HTTPServer(tornado_app)

    server = tornado.httpserver.HTTPServer(wsgi_app)
                      
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

