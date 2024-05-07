from flask import Flask, render_template, request
import pickle

app = Flask(__name__)



with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)




@app.route("/",methods=['GET', 'POST'])
def home():

    data = [0]*12
    pred = None
    if(request.method=="POST"):
        data[0] = request.form.get("age")
        data[1] = request.form.get("gender")
        data[2] = request.form.get("stemp")
        data[3] = request.form.get("ptemp")
        data[4] = request.form.get("ptouch")
        data[5] = request.form.get("ssweet")
        data[6] = request.form.get("pbit")
        data[7] = request.form.get("bleeding")
        data[8] = request.form.get("prob")
        data[9] = request.form.get("smoker")
        # data[10] = request.form.get("diabetes")
        data[10] = request.form.get("beat")
        data[11] = request.form.get("brush")
        
        pred = loaded_model.predict([data])

        pred = pred[0]
        

    return render_template('index.html',pred=pred) 