from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def index():
    print ("*"*120)
    print ("you @ the homepage")
    return render_template("index.html")



@app.route('/survey', methods=['POST']) 
def results():
    print("*"*120)
    print("you @ the results page")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    return render_template("results.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form)


if __name__ =="__main__":
    app.run(debug=True)