import torch
import pandas as pd

person = []
sky = []

def yolo_run(img):
    model = torch.hub.load("ultralytics/yolov5", 'custom', path = 'runs/train/exp5/weights/best.pt')

    len_image = len(img) #img 배열의 길이를 구함

    global person # 객체에 있는 사람 수 저장 배열 (이 것을 비교하여 나은 데이터 추출)
    global sky # 객체에 있는 하늘 수 저장 배열 (이 것을 비교하여 나은 데이터를 추출할거임)
    count = 0 # 몇번 반복했는지

    for i in range(0,len_image): #image의 길이만큼 반복
        results = model(img[i]) #img[i] 값을 욜로로 추출한 값을 results에 저장
        df = pd.DataFrame(results.pandas().xyxy[0]) #yolo로 추출한 객체 표시

        max_index = df.index.max() #객체가 총 몇개인지 구하는 함수

        a = 0 # 임의로 객체 개수 저장 변수 초기화
        b = 0

        for i in range(0, max_index + 1): #객체의 총 개수만큼 반복
            if(df.loc[i, 'name'] == 'Person'): # 객체의 이름이 person이라면
                a += 1 # person 개수 1 증가
            elif(df.loc[i, 'name'] == 'Sky'): # 객체의 이름이 sky라면
                b += 1 # sky 개수 1 증가

        person.append(a) # 사람 배열에 추출된 사람 개수를 넣음
        sky.append(b)

        a = 0
        b = 0

        count += 1

def yolo_results(img):
    global person
    global sky

    len_person = len(person)
    len_sky = len(sky)
    tmp = 0

    for i in range(0, len_person-1):
        if person[i] > person[i+1]:
            tmp = i
        else:
            tmp = i+1
    
    person = []
    sky = []

    return img[tmp]

def yolo(img):
    yolo_run(img)
    return yolo_results(img)