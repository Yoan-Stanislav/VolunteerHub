import logging
from django.shortcuts import render
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)


class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as exc:
            logger.exception("Unhandled exception:", exc_info=exc)
            return HttpResponseServerError(render(request, "500.html", status=500))
