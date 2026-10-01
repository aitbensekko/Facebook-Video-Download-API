import re
from urllib.parse import urlparse

class URLValidator:
    """Validator for Social Media URLs"""
    
    @classmethod
    def is_valid_facebook_url(cls, url: str) -> bool:
        if not url:
            return False
        try:
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                return False
        except Exception:
            return False
        return True
    
    @classmethod
    def normalize_url(cls, url: str) -> str:
        url = re.sub(r'[&?](fbclid|ref|source|__tn__|__cft__|hash)=[^&]*', '', url)
        url = re.sub(r'[&?]$', '', url)
        url = url.replace('web.facebook.com', 'www.facebook.com')
        url = url.replace('m.facebook.com', 'www.facebook.com')
        return url
