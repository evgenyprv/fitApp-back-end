import json

class Message():
    
    __statusCode = 200
    __body = ''
    __headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": '*'
            }
    
    
    def __init__(self, statusCode, body):
        self.__statusCode = statusCode
        self.__body = json.dumps(body)
    
    def setHeaders(self,header_key, header_value):
        self.__headers[header_key] = header_value
    
    def setMessage(self, message):
        self.__body = json.dumps(message)
        
    def setStatusCode(self, code):
        self.__statusCode = code
    
    def generate_response_message(self):
        return {
            'statusCode': self.__statusCode,
            'body': self.__body,
            'headers': self.__headers
        }
    