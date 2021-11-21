from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from . import constant as cst
import requests
import json
# Create your views here.

@api_view(['POST'])
def sg_register(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        print(request_data)
        if "mob" in request_data and "email" in request_data and "pass" in request_data:
            # Create request for security service
            request_url = cst.SECURITY_URL + cst.SG_REGISTER
            body = {"mob": request_data['mob'],
                "email": request_data['email'],
                "pass": request_data['pass']
                }
            json_data = json.dumps(body, indent = 4)
            #make request to security service
            sec_rsp = requests.post(request_url, json = json_data)
            json_rsp = json.loads(sec_rsp.text)
            return JsonResponse(json_rsp, status=status.HTTP_201_CREATED)
        else:
            rsp = {"msg": "keys are not valid"}
            return JsonResponse(rsp, status=status.HTTP_400_BAD_REQUEST)
    rsp = {"msg":"not recieved"}
    return JsonResponse(rsp, status=status.HTTP_400_BAD_REQUEST)
