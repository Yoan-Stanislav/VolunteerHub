import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

import logging
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)

class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.status_code == 404:
                logger.warning(f"404 Not Found: {request.path}")
            return response
        except Exception as e:
            logger.error(f"500 Error: {request.path} - {str(e)}")
            return HttpResponseServerError("Internal Server Error")


