"""SOAP example based on http://soappy.ooz.ie/p/client_27.html"""

from SOAPpy import SOAPProxy, floatType, WSDL

def ex1():
    service = 'http://footballpool.dataaccess.eu/data/info.wso'
    namespace = 'http://footballpool.dataaccess.eu'
    client = SOAPProxy(service, namespace)
    # Note: I get an <HTTPError 500 Internal Server Error> if I call without
    # namespace
    cities = client.Cities()
    print cities.string


def ex2():
    service = 'http://chennaiemergency.co.in/sree/s2.php'
    #namespace = 'urn:ChnEmergency'
    #chennai_emergency = SOAPProxy(service, namespace)
    chennai_emergency = SOAPProxy(service)
    latitude = floatType(11)
    longitude = floatType(12.1)
    print 'Police: '
    print chennai_emergency.police(latitude, longitude)
    print '\nFire:'
    print chennai_emergency.fire(latitude, longitude)
    print '\nHospital:'
    print chennai_emergency.hospital(latitude, longitude)


def ex3():
    wsdl_file = 'http://footballpool.dataaccess.eu/data/info.wso?WSDL'
    server = WSDL.Proxy(wsdl_file)
    cities = server.cities().string

def ex4():
    wsdl_file = 'http://chennaiemergency.co.in/sree/s2.php?wsdl'
    server = WSDL.Proxy(wsdl_file)
    latitude = floatType(11)
    longitude = floatType(12.1)
    print server.police(latitude, longitude)

if __name__ == '__main__':
    ex4()
