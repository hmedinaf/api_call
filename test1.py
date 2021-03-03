from zeep import Client

client = Client('https://login.salesforce.com/services/Soap/c/51.0')
data = {
    'login': {
        'urn:username': 'hmedfrias@resilient-narwhal-hdgymy.com',
        'urn:password': 'H9MekaaqcXHXhY4XKqZxa2TuAQcG2rcm'
    }    
}

client.login(data)

#calc_service = Client(wsdl="http://www.dneonline.com/calculator.asmx?WSDL")
#print(calc_service.service.Add(1234,4321))
