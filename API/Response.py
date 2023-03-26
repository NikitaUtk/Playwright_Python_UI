import requests
from requests_ntlm import HttpNtlmAuth
import json
from settings import *
import re

def getResponse(method, data={}, json_={}, params={}, headers={"Content-type": "application/json", "Accept": "text/plain"}, typeRequest="GET"):
    # data = data -В data помещаются параметры которые необходимо обязательно указать
    # headers = headers
    # params = params В params помещаются параметры которые будут указаны после url
    # json Помещаются параметры которые будут передаваться в body POST запроса
    method = repalceVar(method, data=data)
    if (typeRequest == "POST"):
        response = requests.post(API_URL + method,
                                 auth=HttpNtlmAuth(DOMAIN + '\\' + USERNAME, PASSWORD),
                                 headers=headers,
                                 params=params,
                                 json=json_
                                 )
        # print("URL: " + response.url + " Status_code: " + str(response.status_code))
    elif (typeRequest == "GET"):
        response = requests.get(API_URL + method,
                                auth=HttpNtlmAuth(DOMAIN + '\\' + USERNAME, PASSWORD),
                                params=params
                                )
        # print("URL: " + response.url + " Status_code: " + str(response.status_code))
    return response.json()

def repalceVar(method, data):
    val = re.findall(r'{([^{}]+)}', method)
    for (index, elem) in enumerate(val):
        resStr = data[val[index]]
        method = str.replace(method, '{' + elem + '}', str(resStr))
    return method