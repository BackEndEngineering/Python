from bottle import route, run , template, response, request
import json


@route('/fighters')
def data_hello():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = ['Jon Jones', 'Robbie Lawler', 'Michael Bisping', "Max Holloway"]
    return json.dumps(resp_data)
run(host='localhost', port=8080)
