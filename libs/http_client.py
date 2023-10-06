import requests

__all__ = ['HttpClient']

class HttpClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def _build_url(self, path):
        return f"{self.base_url}/{path}"

    def post(self, path, data=None):
        url = self._build_url(path)
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response