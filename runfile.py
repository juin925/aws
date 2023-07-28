import torch
import pandas as pd

def yolo_run(img, num):
    model = torch.hub.load("ultralytics/yolov5", 'custom', path = 'runs/train/exp9/weights/best.pt')

    len_image = len(img) #img 배열의 길이를 구함

    person = [] # 객체에 있는 사람 수 저장 배열 (이 것을 비교하여 나은 데이터 추출)
    sky = []# 객체에 있는 하늘 수 저장 배열 (이 것을 비교하여 나은 데이터를 추출할거임)
    beach = []
    tree = []
    building = []
    flower = []

    for i in range(0,len_image): #image의 길이만큼 반복
        results = model(img[i]) #img[i] 값을 욜로로 추출한 값을 results에 저장
        df = pd.DataFrame(results.pandas().xyxy[0]) #yolo로 추출한 객체 표시

        max_index = df.index.max() #객체가 총 몇개인지 구하는 함수

        a = 0 # 임의로 객체 개수 저장 변수 초기화
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        for i in range(0, max_index + 1): #객체의 총 개수만큼 반복
            if(df.loc[i, 'name'] == 'person'): # 객체의 이름이 person이라면
                a += 1 # person 개수 1 증가
            elif(df.loc[i, 'name'] == 'sky'): # 객체의 이름이 sky라면
                b += 1 # sky 개수 1 증가
            elif(df.loc[i, 'name'] == 'beach'): # 객체의 이름이 beach라면
                c += 1 # sky 개수 1 증가
            elif(df.loc[i, 'name'] == 'tree'): # 객체의 이름이 tree라면
                d += 1 # sky 개수 1 증가
            elif(df.loc[i, 'name'] == 'building'): # 객체의 이름이 building라면
                e += 1 # sky 개수 1 증가
            elif(df.loc[i, 'name'] == 'flower'): # 객체의 이름이 flower라면
                f += 1 # sky 개수 1 증가

        person.append(a) # 사람 배열에 추출된 사람 개수를 넣음
        sky.append(b)
        beach.append(c)
        tree.append(d)
        building.append(e)
        flower.append(f)

    print("person = " + str(person))
    print("sky = " + str(sky))
    print("beach = " + str(beach))
    print("tree = " + str(tree))
    print("building = " + str(building))
    print("flower = " + str(flower))    
    
    len_person = len(person)
    len_sky = len(sky)
    tmp = -1

    for i in range(0, len_image):
        if person[i] == num:
            tmp = i

    value = []

    if tmp == -1:

        for i in range(0, len_person):
            value.append((sky[i]*3) + (beach[i]*2) + (tree[i]*1) + (building[i]*1) + (flower[i]*1))

        tmp = 0
        for i in range(0, len_person-1):
            if value[i] < value[i+1]:
                tmp = i+1

        print("value = " + str(value))
        value = []
            
    print(tmp)
    person = []
    sky = []
    beach = []
    tree = []
    building = []
    flower = []

    return img[tmp]



def yolo(img, num):
    return yolo_run(img, num)
   