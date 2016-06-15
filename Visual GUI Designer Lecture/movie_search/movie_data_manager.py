'''
movie_data_manager is a data layer that can be used with a UI layer
It uses the SF Open Data API.
Author: Diana Sheng
'''
from urllib2 import urlopen
from json import load
from movie_info import *

movie_list = []


def load_movie_data():
    #sf open data source: film location in sf
    apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

    #open the apiUrl and assign data to variable
    response = urlopen(apiUrl)
    json_obj = load(response)

    director = ''
    release = ''
    title = ''
    actor_1 = ''
    actor_2 = ''
    location = ''

    for movie_info in json_obj:
        if 'director' in movie_info:
            director = str(movie_info['director'].encode('utf8'))
        if 'release_year' in movie_info:
            release = str(movie_info["release_year"].encode('utf8'))
        if 'title' in movie_info:
            title = str(movie_info["title"].encode('utf8'))
        if 'actor_1' in movie_info:
            actor_1 = str(movie_info['actor_1'].encode('utf8'))
        if 'actor_2' in movie_info:
            actor_2 = str(movie_info['actor_2'].encode('utf8'))
        if 'locations' in movie_info:
            location = str(movie_info['locations'].encode('utf8'))

        new_movie = MovieInfo(director=director, release_year=release,
                              title=title, actor_1=actor_1,actor_2=actor_2,location=location)
        movie_list.append(new_movie)

    response.close()
    return movie_list


def get_movie_info_by_year(year):
    movie_list_by_year = []
    for info in movie_list:
        if info.release_year == year:
            movie_list_by_year.append(info)
    return movie_list_by_year


def get_release_year_list():
    year_list = []
    for info in movie_list:
        year_list.append(info.release_year)

    unique_set = set(year_list)  # cast to set to get rid of duplicates
    new_list = list(unique_set)  # cast back to list
    new_list.sort()
    return new_list


def main():
    # test above functions
    load_movie_data()

    # print out the movies in the list
    for info in movie_list:
        print "title - " + info.title
        print "director - " + info.director
        print "release year - " + info.release_year
        print "actor1 - " + info.actor_1
        print "actor2 - " + info.actor_2
        print "location - " + info.location

    print get_release_year_list()
    print get_movie_info_by_year('2000')

if __name__ == "__main__":
    main()
