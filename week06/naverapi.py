# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'lN5IdpuaLHmLLewNoQJxe'
client_secret = 'A0QryHAmx8'

def main():
    
    node = 'news'   # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')
    
    cnt = 0
    jsonResult = []
    
    jsonResult = getNaverSearch(node, srcText, 1, 100)   # [CODE 2]
    total = js