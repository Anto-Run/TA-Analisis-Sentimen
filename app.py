from flask import Flask, request, render_template
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.models import load_model


app = Flask(__name__)
model = load_model('best_model1.hdf5')


@app.route('/')
def my_form():
    return render_template('indeks.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text_test = request.form['text1']
    tokenizer = Tokenizer(num_words=5000)
    sequence = tokenizer.texts_to_sequences(text_test)
    test = pad_sequences(sequence, maxlen=200)
    prediction_result = model.predict(test)

    if prediction_result[0][0] > prediction_result[0][1] and prediction_result[0][0] > prediction_result[0][2]:
        sentimen = 'Neutral'
    elif prediction_result[0][1] > prediction_result[0][0] and prediction_result[0][1] > prediction_result[0][2]:
        sentimen = 'Negative'
    else:
        sentimen = 'Positive'

    return render_template('indeks.html', result=sentimen, text1=text_test, text2=prediction_result[0][0], text3=prediction_result[0][1], text4=prediction_result[0][2])


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
