import requests, time

# data = input()
# url_data = 'http://www.nbrb.by/API/ExRates/Rates?onDate=' + data + '&Periodicity=0'
url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
response = requests.get(url).json()
time.sleep(0.01)


def currency():
    name = []
    rate = []
    for i in response:
        x = i['Cur_Name']
        name.append(x)

    for i in response:
        x = i['Cur_OfficialRate']
        rate.append(x)
    return name, rate


name, rate = currency()
