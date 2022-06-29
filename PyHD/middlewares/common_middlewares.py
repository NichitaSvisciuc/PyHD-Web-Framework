# Middleware is a callable object,
# so after you get a response object describe the behavior of middleware in a __call__ func

class CommonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path = list(request.path)
        path.pop(0)

        if '/' not in path and len(path) > 0:
            request.path = str(request.path) + '/'

        response = self.get_response(request)

        return response
