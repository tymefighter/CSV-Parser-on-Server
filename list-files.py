import requests

class ListFiles:

    @staticmethod
    def print (response):
        try:
            for filename in response.data['files']:
                print (filename)
        except KeyError:
            print("File names not received in response.data")
