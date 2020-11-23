import requests

url = "https://notify-api.line.me/api/notify"

payload = "message=Hello World"
headers = {"Content-Type":"application/x-www-form-urlencoded", "Authorization":"Bearer e97W7rguYjsJu2R8SC0XIlqSgorxplJ5Rigg3dixsyp"}
response = requests.request('POST',url,data=payload,headers=headers)
print(response.text)