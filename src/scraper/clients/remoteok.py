import logging

import requests
from django.conf import settings


logger = logging.getLogger(__name__)


class RemoteokClient:
    BASE_URL = settings.REMOTEOK_BASE_URL

    def make_request(self, method, url, data=None, params=None):
        headers = {
            "Content-Type": "application/json"
        }
        if data is None:
            data = {}
        logger.info(f"Sending {method} request to {url}, data: {data}")
        response = requests.request(
            method=method, url=f"{self.BASE_URL}{url}",
            params=params, headers=headers, json=data, timeout=(5, 15)
        )
        response.raise_for_status()
        return response.json()

    def get_jobs(self, params=None):
        return self.make_request(method="GET", url="/api", data={}, params=params)
