from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def json_example():
	request_data = request.get_json()

	blocked_uri = request_data['csp-report']['blocked-uri']
	document_uri = request_data['csp-report']['document-uri']
	return '''
		The blocked-uri value is: {}
		The document-uri value is: {}'''.format(blocked_uri, document_uri)
