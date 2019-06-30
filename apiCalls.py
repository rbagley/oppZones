import requests

key = 'acc4710d436f536ca66a6c5cbc1e49f347149294'

# response=requests.get("https://api.census.gov/data/2017/acs/acs5/profile?get=NAME,DP05_0033E,DP03_0062E,DP04_0089E,DP03_0009PE,DP03_0128PE,DP02_0067PE&for=tract:*&in=state:02&in=county:*")
# print(response.status_code)


def getTractInfo(tract,state,county):
    # //print(tract,state)
    print(tract, state, county)
    response=requests.get("https://api.census.gov/data/2017/acs/acs5/profile?get=NAME,DP05_0033E,DP03_0062E,DP04_0089E,DP03_0009PE,DP03_0128PE,DP02_0067PE&for=tract:"+tract+"&in=state:"+state+"%20county:"+county+"&key="+key)
    # print(response)
    if response.status_code!=200:
        return None;
    else:
        return response.json()
