
'''
@author neelkant newra
date 02.04.2022

Program to combine the model prediction
'''
import pickle
import sklearn

def combineModel(models:list,element):
    '''
    parameter
    ---------
    models: list of model prediction you want to combine
    element: scalar vector of the input feeded in the model

    return
    ------
    prediction: combine prediction
    prediction_prob: combine prediction preobability
    '''
    prediction = 0
    prediction_prob = 0
    for model in models:
        prediction += model.predict((element)).max()
        prediction_prob+= int(model.predict_proba((element)).max()*100)
    prediction = prediction/len(models)
    prediction_prob = prediction_prob/len(models)
    
    return prediction,prediction_prob

