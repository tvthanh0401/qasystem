from bottle import get, post, run, request, install
import json
import sys
from model import *
from serpapi import GoogleSearch
import googletrans
from googletrans import Translator
from config import *
from truckpad.bottle.cors import CorsPlugin, enable_cors





params = {
  "q": "",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": API_KEY,
}
translator = Translator()
reader = DocumentReader("deepset/minilm-uncased-squad2") 
#"deepset/roberta-base-squad2"
#reader = DocumentReader("deepset/roberta-base-squad2")

def get_answer(question):
    params['q'] = question
    results = GoogleSearch(params).get_dict()
    text = ''
    for result in results['organic_results']:
        text += result.get('snippet', '')
    text = text.replace('...', '.')
    translated_question = translator.translate(question, src='vi', dest='en').text
    translated_context = translator.translate(text, src='vi', dest='en').text
    print(translated_context)
    reader.tokenize(translated_question, translated_context)
    translated_ans = reader.get_answer()
    print(translated_ans)
    translated_ans = translated_ans.replace('[CLS]', '')
    translated_ans = translated_ans.replace('[SEP]', '')
    if translated_ans == '':
        return 'Không tìm thấy câu trả lời'
    return translator.translate(translated_ans, src='en', dest='vi').text




@get('/api')
def hello():
    return "This is api page for processing POSTed messages"

@enable_cors
@post('/api')
def api():
    ans = request.body.getvalue().decode('utf-8')
    print(ans)
    lookup = json.loads(ans)
    res = {"result": get_answer(lookup['question'])}
    return res

install(CorsPlugin(origins=['localhost:8080', 'localhost:5500']))
run(host='localhost', port=8080, debug=True)
