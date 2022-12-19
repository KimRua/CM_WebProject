def lunchInfo():
    import requests
    from bs4 import BeautifulSoup
    import json
    import re
    
    url = 'https://gm.hs.kr/'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.select_one('#container > div.main_lay_3 > div > article > div.objContent > div.menu > span.list > a')
        reTextList = re.compile('[가-힣]+').findall(str(info))
        
        if len(reTextList) < 1:
            json_string = '{ "version":"2.0","data": { "msg" : "오늘은 급식이 없어요!"}}'
        else :
            json_string = '{ "version":"2.0","data": { "msg" :"오늘의 급식 메뉴는 '
            for idx, val in enumerate(reTextList):
                if idx != 0:
                    json_string +=  ", " + val 
                else:
                    json_string += val
            json_string += '입니다!"}}'
        
        #json_string = json_string.encode('utf-8')
        json_object = json.loads(json_string)
        return json_object
    else:
        return

def GetGuideInfo():
    import json
    
    f = open("guide.txt",'r')
    morning,lunch = f.read().split()
    f.close
    
    json_string = '{ "version":"2.0","data": {"morning" :"' + morning + '", "lunch" : "' + lunch + '"}}'
    json_object = json.loads(json_string)
    return json_object

def SetGuideInfo():
    import json
    
    f = open("guide.txt", 'r')
    morning,lunch = map(int,f.read().split())
    f.close
        
    lunch = 1 if lunch == 17 else lunch + 1
    morning = 1 if morning == 17 else morning + 1
    
    f = open("guide.txt", 'w')
    f.write("{} {}".format(morning, lunch))
    f.close
    
    json_string = '{ "version":"2.0","data": { "msg" : "활동이 확인되었습니다!"}}'
    json_object = json.loads(json_string)
    return json_object
