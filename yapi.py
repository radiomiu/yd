import json, urllib2
 
class YandexApiService(object):
    sandbox_url = 'https://api-sandbox.direct.yandex.ru/json-api/v4/'
    
    def __init__(self, token):
        self.token = token
        
    def query(self, method, params=None):
        query_params = {'token': self.token, 'method': method}
        if params: query_params['param'] = params
        
        jdata = json.dumps(query_params, ensure_ascii=False).encode('utf8')
        response = urllib2.urlopen(self.sandbox_url, jdata).read()
        return self.__handle_response(response)
            
    def __handle_response(self, response):
        try:
            decoded_responce = json.loads(response)
            return decoded_responce['data']
        except KeyError as detail:
            print 'Error fetching data from ', response
            raise detail
