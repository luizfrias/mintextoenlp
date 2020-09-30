
import pickle
from flask import Flask
from flask import request
from flask import jsonify

import spacy

app = Flask(__name__)

# Carrega o modelo
nlp = spacy.load('out/custom_nlp.pkl')

# Cria o end point
@app.route('/api/v1.0/entities', methods=['GET'])
def get_entities(nlp=nlp):

    # Recupera o texto
    text = request.args.get('text')
    
    if text is None:
        return jsonify(status=['erro'])
    
    ents = [{
        'text': ent.text, 
        'start': ent.start_char, 
        'end': ent.end_char, 
        'label': ent.label_
    } for ent in nlp(text).ents]
    
    return jsonify(ents=ents)

if __name__ == '__main__':
    # Executa localhost:8889
    app.run(port=8889, host='localhost')