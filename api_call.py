import os
from zeep import Client
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/start')
def start():
    return('This is the index page!')

@app.route('/apicall')
def apicall():
    calc_service = Client(wsdl="http://www.dneonline.com/calculator.asmx?WSDL")
    resultado=calc_service.service.Add(1234,1111)
    return('El resultado es ' + str(resultado))


if __name__ == '__main__':
    host=os.getenv('IP', '0.0.0.0')
    port=int(os.getenv('PORT', 5000))
    app.debug=True
    app.run(host=host, port=port)
    
