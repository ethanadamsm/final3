import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line
define("port", default=8888, help="run on the given port", type=int)
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        data = fetch_coroutine("squaresserver.buttonfans.com")
        self.write(data)
        print data

app = tornado.web.Application([
    (r'/', MainHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()