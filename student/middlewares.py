import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class TimeItMiddleware(object):
    def __init__(self, get_response):
        print('---init----')
        self.get_response = get_response

    def __call__(self, request):
        print('--call---')
        response = self.get_response(request)
        return response

    # def process_request(self, request):
    #     self.start_time = time.time()
    #     return

    def precess_view(self, request, func, *args, **kwargs):
        print('---process_view----')
        if request.path != reverse('student:index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process View: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        print('异常--------')
        return HttpResponse('异常来了')

    # def process_template_response(self, request, response):
    #     return response
    #
    # def process_response(self, request, response):
    #     costed = time.time() - self.start_time
    #     print('reqeust to response cose: {:.2f}s'.format(costed))
    #     return response
