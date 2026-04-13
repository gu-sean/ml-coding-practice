# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "e9487bf81ac6dc1048a20629170c6a3100043ef64eace77af9c673ef67467074"

"""### [CODE 0]"""

def main():
    jsonResult = []
    result = []
    
    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국: 122 / 일본: 130 / 미국: 275) :')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? :'))
    nEndYear = int(input(''))