import os

try:
    from common.tokens_and_keys import GOOGLE_API_KEY
except ImportError:
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


def google_api(request):
    return {"google_api_key": GOOGLE_API_KEY}