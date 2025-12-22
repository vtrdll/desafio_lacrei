import time
import logging


access_logger = logging.getLogger("access")


class DRFAccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = (time.time() - start_time) * 1000

        user = getattr(request, "user", None)
        user_id = user.id if user and user.is_authenticated else "anon"

        access_logger.info(
            "%s %s %s %s user=%s %.2fms",
            request.META.get("REMOTE_ADDR"),
            request.method,
            request.get_full_path(),
            response.status_code,
            user_id,
            duration,
        )

        return response
