# 값 : 디스크단면적, 전방디스크높이(mm), 후방디스크높이(mm)
# input() return str() -> float()
DMJ = float(input('DiscMyunJek : '))
FDH = float(input('FrontDiskHeight : '))
RDH = float(input('RearDiscHeight : '))


import pickle

with open('datasets/RecurrenceOfSurgery_regression_quest.pkl', 'rb') as ROSQUEST :
    loaded_model = pickle.load(ROSQUEST)
    input_labels = [[DMJ, FDH, RDH]] # 학습했던 설명변수 형식
    result_predict = loaded_model.predict(input_labels)
    print('Predict AGE Result : {}'.format(result_predict))    
    pass