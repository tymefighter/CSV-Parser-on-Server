import json
import requests

class MetadataQuery:

    @staticmethod
    def print (response):
        try:
            dict = response.json().loads()
            for key in dict.keys():
                print(key + ": " + dict[key])

        except ValueError: 
            print("Response is NOT a valid JSON object")


