from flask import*
from PyDictionary import PyDictionary
from urllib3.exceptions import ConnectionError

app=Flask(__name__)
@app.route('/')
def home():
	given=[0]
	meanings=[0]
	return render_template('index.html',given=given,meanings=meanings)

@app.route('/',methods=['POST'])
def result():
  error = None
  try:
  	given=str(request.form['search'])
  	given=given.split(',')
  	antos=dict()
  	synos=dict()
  	word=PyDictionary(given)
  	meanings=word.getMeanings()
  	for wd in given:
  		antos[wd]=word.antonym(wd)
  		synos[wd]=word.synonym(wd)
  except:
    error = "No Internet Connection."
    
  return render_template('index.html',error=error,given=given,
    meanings=meanings,title=given,antos=antos,synos=synos)
if(__name__=='__main__'):
	app.run(debug=True)