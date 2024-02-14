from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/EDA')
def EDA():
    return render_template('EDA.html')

@app.route('/trend')
def Trend():
    return render_template('trend.html')

@app.route('/clustering')
def Clustering():
    return render_template('clustering.html')

@app.route('/clustering/notebook')
def Clustering_Notebook():
    return render_template('clustering_notebook.html')

@app.route('/mapping/timbangan')
def Mapping_Timbangan():
    return render_template('mapping_timbangan.html')

@app.route('/mapping/SIPSN')
def Mapping_SIPSN():
    return render_template('mapping_sipsn.html')

@app.route('/mapping')
def Mapping():
    return redirect('/mapping/timbangan')

@app.route('/prediction')
def Prediction():
    return render_template('prediction.html')

@app.errorhandler(Exception)
def handle_error(error):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
