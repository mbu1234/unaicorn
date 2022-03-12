#Correct order in the dataframe
def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)

    if prediction == 1:
        prediction = "This passenger would have survived"
    elif prediction== 0:
        prediction = "Unfortunately, this passenger would have died."
    else:
        prediction = "Opps! There is an error with respect to the returned value"

    return prediction
