# -*- coding:utf-8 -*-
from django.http import HttpResponse
from wechat import *

def index(request):

        if 'echostr' in request.GET:
            echostr = request.GET['echostr']
            signature = request.GET['signature']
            timestamp = request.GET['timestamp']
            nonce = request.GET['nonce']


            if Weixin.valid(signature, timestamp, nonce) == True:
                return HttpResponse(echostr)
            else:
                return HttpResponse('Valid Fail!')


        xml = request.raw_post_data
        wechat = Wechat(xml)

        #当用户关注时会自动发送消息为Hello2BizUser的消息
        if wechat.Content == 'Hello2BizUser':
            reply = u'欢迎加入'

        response = wechat.textResp(content=reply, funcflag=0)

        return HttpResponse(response)



