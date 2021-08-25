import pytest
import requests
import json
@pytest.fixture(scope="module")
def company_login_token():
    url="http://127.0.0.1:8888/login"
    heraders=""
    data="name=xiaoming&pwd=123"
    rq=requests.post(url=url,heraders=heraders,data=data)
    return str("Barer"+rq.json()['data']['access_token'])
