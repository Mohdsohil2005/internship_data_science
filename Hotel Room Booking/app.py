from flask import Flask,render_template,url_for,request

import joblib
model = joblib.load('./models/randomforest_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pay')
def pay():
    return render_template('pay.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        # Input values
        month = request.form['month']
        january = 0
        february = 0
        march = 0
        april = 0
        may = 0
        june = 0
        july = 0
        august = 0
        september = 0
        october = 0
        november = 0
        if month == 'January':
            january = 1
        elif month == 'February':
            february = 1
        elif month == 'March':
            march = 1
        elif month == 'April':
            april = 1
        elif month == 'May':
            may = 1
        elif month == 'June':
            june = 1
        elif month == 'July':
            july = 1
        elif month == 'August':
            august = 1  
        elif month == 'September':
            september = 1
        elif month == 'October':
            october = 1
        elif month == 'November':
            november = 1 

        date = int(request.form["date"])

        adults = int(request.form["adults"])

        children = int(request.form["children"])

        meal = request.form['meal']
        bb = 0
        hb = 0
        fb = 0
        sc = 0
        if meal == 'BB':
            bb = 1
        elif meal == 'HB':
            hb = 1
        elif meal == 'FB':
            fb = 1
        elif meal == 'SC':
            sc = 1

        repeated_guest = int(request.form['repeated_guest'])

        room_type = request.form['room_type']
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        l = 0
        if room_type == 'A':
            a = 1
        elif room_type == 'B':
            b = 1
        elif room_type == 'C':
            c = 1
        elif room_type == 'D':
            d = 1
        if room_type == 'E':
            e = 1
        elif room_type == 'F':
            f = 1
        elif room_type == 'G':
            g = 1
        elif room_type == 'H':
            h = 1
        elif room_type == 'L':
            l = 1

        customer_type = request.form['customer_type']
        transient = 0
        group = 0
        contract = 0
        if customer_type == 'Transient':
            transient = 1
        elif customer_type == 'Group':
            group = 1
        elif customer_type == 'Contract':
            contract = 1


        parking = int(request.form["parking"])

        extra = int(request.form["extra"])

        unseen_data = [january,february,march,april,may,june,july,august,september,october,november,
                       date,adults,children,
                       bb,hb,fb,sc,
                       repeated_guest,
                       a,b,c,d,e,f,g,h,l,
                       transient,group,contract,
                       parking,extra]

        prediction = model.predict([unseen_data])[0]
        prediction = round(prediction,2)

        return render_template('output.html', prediction=prediction,
                               
                               )  # Pass the prediction to the template

        


if __name__ == "__main__":
    app.run(debug=True)
