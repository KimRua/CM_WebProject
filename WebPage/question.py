import urllib3
import json

def AI_F(question):
    if question == '':
        return "질문을 입력해주세요"
    
    openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
    accessKey = "ad9e100b-de95-4b7e-8b69-5931f47cb4a3"
    passage = "cm='Computer Manager'. 주소=경기경영고 5층. 총인원은 10명, 학년 인원 : 5명, 2학년 인원 : 4명, 1학년 인원 : 1명이다. 부장은 김현우이다. 담당 선생님은 전창영이다. 연락처 : 070-7875-3423. cm은 게임 제작, 영상 편집, 앱 개발 등의 활동을 한다."

    requestJson = {
    "access_key": accessKey,
        "argument": {
            "question": question,
            "passage": passage
        }
    }
    
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    js1 = response.data
    jsonObject = json.loads(js1)
    answer = jsonObject.get("return_object").get("MRCInfo").get("answer")
    confidence = jsonObject.get("return_object").get("MRCInfo").get("confidence")
    
    if (float(confidence) < 0.5):
        answer = "그런 정보는 알지 못해요"
        
    return answer