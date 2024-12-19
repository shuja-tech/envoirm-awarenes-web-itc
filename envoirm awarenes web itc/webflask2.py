from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def firstpage():
    return render_template('home.html')

@app.route('/about')
def home():
 return render_template('aboutus.html')

@app.route('/mempg')
def mebpg():
 return render_template('mempg.html')

if __name__=='__main__':
    app.run(debug=True)
    