import logging
from rest_framework.views import exception_handler

logger = logging.getLogger("rest_framework")


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        view = context.get("view")
        request = context.get("request")

        logger.error(
            "DRF exception | "
            "view=%s | "
            "method=%s | "
            "path=%s | "
            "status=%s | "
            "error=%s",
            view.__class__.__name__ if view else "unknown",
            request.method if request else "unknown",
            request.get_full_path() if request else "unknown",
            response.status_code,
            str(exc),
        )
    return response
