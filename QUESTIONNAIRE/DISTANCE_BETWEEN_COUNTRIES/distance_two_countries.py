"""
Calculates distance between two countries' capitals.
"""
# https://pypi.org/project/countryinfo/

from countryinfo import CountryInfo
from geopy.distance import geodesic

from_country = 'Czech Republic'
survey_compiled_file = 'LEGO_all_languages.csv'

def get_countries_from_survey_data(file_name):
    with open(file_name, encoding='utf-8') as sourse_file:
        survey_data = sourse_file.readlines()

    survey_data_countries = [[respondent][0].split(',')[4].replace('"','') for respondent in survey_data[1:]]
    survey_unique_countries = set(survey_data_countries)

    list_of_countries = []

    for country in survey_unique_countries:
        if country not in list_of_countries:
            if country == 'czechia (czech republic)':
                list_of_countries.append('czech republic')
            else:
                list_of_countries.append(country)
    print(list_of_countries)
    return list_of_countries

def find_capital_coordinates(country):
    coordinates = CountryInfo(country).capital_latlng()
    return coordinates

def change_coordinates_format(coordinates):
    coordinates_tuple = (coordinates[0], coordinates[1])
    return coordinates_tuple

def find_distance_between_capitals(countries):
    base_country_coordinates = find_capital_coordinates(from_country)
    base_country_coordinates_tuple = change_coordinates_format(base_country_coordinates)

    country_longest_ditsance_km = 0
    country_longest_distance =''
    for country in countries:
        country_coordinates = find_capital_coordinates(country)
        country_coordinates_tuple = change_coordinates_format(country_coordinates)
        distance = geodesic(country_coordinates_tuple, base_country_coordinates_tuple).km
        if distance > country_longest_ditsance_km:
            country_longest_ditsance_km = round(distance, 1)
            country_longest_distance = country

    base_country_capital = CountryInfo(from_country).capital()
    print(f'The furthest from {base_country_capital} is {country_longest_distance.title()}: {country_longest_ditsance_km} km.')

list_of_countries = get_countries_from_survey_data(survey_compiled_file)
print(f'There are {len(list_of_countries)} unique countries in our survey.')
find_distance_between_capitals(list_of_countries)