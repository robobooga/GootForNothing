#!/usr/bin/python3
import requests
import json
from pprint import pprint

payload = {"numbers":["0001","0002", "0003", "0004", "0005"], "checkCombinations":"false", "sortTypeInteger":"2"}
resp = requests.post('http://www.singaporepools.com.sg/_layouts/15/FourD/FourDCommon.aspx/Get4DNumberCheckResultsJSON', json=payload)

d = resp.json()

print(d['d'])
