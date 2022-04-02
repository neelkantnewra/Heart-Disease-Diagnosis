
'''
@author neelkant newra
date 02.04.2022
'''
import pickle
import sklearn

def combineModel(models:list,element):
    prediction = 0
    prediction_prob = 0
    for model in models:
        prediction += model.predict((element)).max()
        prediction_prob+= int(model.predict_proba((element)).max()*100)
    prediction = prediction/len(models)
    prediction_prob = prediction_prob/len(models)
    
    return prediction,prediction_prob

