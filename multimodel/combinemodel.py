'''
@ author: neelkant newra
date 02.04.2022
'''

def modelSelect(models:list):
  prediction = 0
  for model in models:
    prediction += model.predict((element)).max()
  prediction = prediction/8
  prediction_prob = prediction * 100
  
  return prediction, prediction_prob
