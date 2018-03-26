from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.conf import settings
from .WXBizDataCrypt import WXBizDataCrypt

import json
import requests

# Create your views here.
class IndexView(View):
  def get(self, request):
    return HttpResponse('wechat 1')

class LoginView(View):
  def post(self, request):
    params = json.loads(request.body.decode('utf-8'))
    code = params["code"]
    encryptedData = params["encryptedData"]
    signature = params['signature']
    iv = params['iv']
    res = requests.get(settings.WX_TOKEN_URL + '&js_code=' + code)

    # validate
    res_json = res.json()
    app_id = settings.WX_APP_ID
    openid = res_json['openid']
    session_key = res_json['session_key']

    user_info = WXBizDataCrypt(app_id, session_key).decrypt(encryptedData, iv)

    return HttpResponse(json.dumps({
      'avatarUrl': user_info['avatarUrl'],
      'city': user_info['city'],
      'country': user_info['country'],
      'province': user_info['province'],
      'nickName': user_info['nickName'],
    }))
