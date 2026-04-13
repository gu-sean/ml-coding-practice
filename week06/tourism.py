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
    nat_cd = input("")