# 값 : 디스크단면적, 전방디스크높이(mm), 후방디스크높이(mm)
# input() return str() -> float()
compactness_se = float(input('compactness_se : '))
concavity_se = float(input('concavity_se : '))
concave_points_se  = float(input('concave_points_se : '))
		
import pickle

with open('datasets/BreastCancerWisconsin_Regreesion_quest.pkl', 'rb') as BCDQUEST :
    loaded_model = pickle.load(BCDQUEST)
    input_labels = [[compactness_se, concavity_se, concave_points_se]] # 학습했던 설명변수 형식
    result_predict = loaded_model.predict(input_labels)
    print('Predict Result : {}'.format(result_predict))    
    pass