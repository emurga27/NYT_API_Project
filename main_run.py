import json
import main_functions
import requests

api_key_dict = main_functions.read_from_file('JSON_files/api_key.json')
api_key = api_key_dict['my_key']

#Top stories
def get_top_stories(option):
    url = f'https://api.nytimes.com/svc/topstories/v2/{option}.json?api-key=' + api_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, 'JSON_files/response.json')
    my_articles = main_functions.read_from_file('JSON_files/response.json')
    return my_articles

#Most viewed, shared, or emailed articles
def get_most_popular_stories(type, period):
    url2 = f'https://api.nytimes.com/svc/mostpopular/v2/{type}/{period}.json?api-key=' + api_key
    response_most_pop = requests.get(url2).json()
    main_functions.save_to_file(response_most_pop, 'JSON_files/most_pop.json')
    my_pop_articles = main_functions.read_from_file('JSON_files/most_pop.json')
    return my_pop_articles

#print(get_top_stories("arts")) #to test the functions