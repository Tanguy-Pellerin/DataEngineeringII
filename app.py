from flask import Flask, request, render_template
import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

def classify(loaded_model, loaded_vectorizer, sentence):

	result = loaded_model.predict(loaded_vectorizer.transform([sentence]))
	if result==1:
		return render_template('index.html', sentiment='Positive')
		#return 'Positive'
	elif result==0:
		return render_template('index.html', sentiment='Neutral')
		#return 'Neutral'
	elif result==-1:
		return render_template('index.html', sentiment='Negative')
		#return 'Negative'

	
@app.route('/', methods=['GET', 'POST'])
def index():
	model_path = 'Pickle/MultinomialNB_model.sav'
	vectorizer_path = 'Pickle/CountVectorizer.sav'

	loaded_model = pickle.load(open(model_path, 'rb'))
	loaded_vectorizer = pickle.load(open(vectorizer_path, 'rb'))

	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'classify':
			return classify(loaded_model, loaded_vectorizer, details['sentence'])

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	
	
	
	
	