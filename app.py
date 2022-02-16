from flask import Flask
from tika import parser

app = Flask(__name__)

@app.route('/')
def hello_world():
	raw = parser.from_file('sample_rhhcc.pdf', 'https://rhhcc-tika-bdxsr.ondigitalocean.app/tika')
	return raw['content']
