import os

try:
    from common.tokens_and_keys import GOOGLE_API_KEY
except ImportError:
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

from blog.models import Blog


def blog_count(request):
    count = Blog.objects.count()
    return {"blog_count": count != 0}


def google_api(request):
    return {"google_api_key": GOOGLE_API_KEY}