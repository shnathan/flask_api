import json
from flask import Flask,render_template,request,redirect,session

import requests
import json
from random import uniform as rnd
from model import Person
test=[]
app = Flask(__name__)
@app.route('/api',methods=['GET','POST'])
def api():
    return {"hello":"hai"}

@app.route('/processUserInfo/<string:userInfo>',methods=['GET','POST'])
def processUserInfo(userInfo):
    userInfo = json.loads(userInfo)
    
    age= int(userInfo['age'])
    weight=int(userInfo['weight'])
    height= int(userInfo['height'])
    gender= userInfo['gender']
    activity=userInfo['activity']
    weights=userInfo['weightplan']
    number_of_meals=int(userInfo['meals'])
    # print(type(age))
    # print(weight)
    # print(height)
    # print(gender)
    # print(activity)
    # print(weight)
    # print(number_of_meals)
    weight_loss=-1
    if(weights=="Maintain weight"):
        weight_loss=1

    elif(weights=="Mild Weight loss"):
        weight_loss=0.9
    elif(weights=="Weight loss"):
        weight_loss=0.8
    else:
        weight_loss=0.6

    if number_of_meals==3:
        meals_calories_perc={'breakfast':0.35,'lunch':0.40,'dinner':0.25}
    elif number_of_meals==4:
        meals_calories_perc={'breakfast':0.30,'morning snack':0.05,'lunch':0.40,'dinner':0.25}
    else:
        meals_calories_perc={'breakfast':0.30,'morning snack':0.05,'lunch':0.40,'afternoon snack':0.05,'dinner':0.20}

    person = Person(age,height,weight,gender,activity,meals_calories_perc,weight_loss)
    recommendations=person.generate_recommendations()
    #print(type(recommendations))
    test=recommendations
    print(test[0],end="PPPPPPP")
    #print(recommendations)
   
    return test

if __name__=='__main__':
    app.run(debug=True)

    




