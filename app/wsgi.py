import json
from wsgiref.simple_server import make_server


def return_response(environ, start_response):
    request = Request(environ)
    view = get_view(request.url)
    response = view(request)
    start_response(response.status_code, list(response.headers.items()))
    return response


class JsonResponse():
   def __init__(self, content={}, status_code="200 OK", headers={}):
        self.content = json.dumps(content)
        self.status_code = status_code
        self.headers = headers
        self.headers["content-type"] = "application/json"
        self.headers["access-control-allow-origin"] = "*"

   def __iter__(self):
       yield self.content.encode()


class Request():
    def __init__(self, environ):
      self.method = environ.get("REQUEST_METHOD")
      self.url = environ.get("PATH_INFO")
      self.query_string = environ.get("QUERY_STRING")
      self.body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH") or 0)).decode("utf-8")
      self.headers = {
         key[5:].lower(): value for key, value in environ.items() if key.startswith("HTTP_")
      }


def get_view(url):
   if url == '/hello-world':
      return hello_word
   elif url == '/contagem-pessoas':
      return count_pessoas
   else:
      return none_response


def none_response(request):
   return JsonResponse({})


def hello_word(request):
   return JsonResponse("Hello World")


def count_pessoas(request):
   return JsonResponse({"pessoas": 10})


if __name__ == "__main__":
    server = make_server("localhost", 9001, return_response)
    server.serve_forever()