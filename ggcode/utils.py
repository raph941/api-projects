import requests
        
def GetNearCities(latitude, longitude):
    '''get 3 cities close to the latitude and longitude provided'''
    near_city_url = "https://geocodeapi.p.rapidapi.com/GetNearestCities"
    near_city_querystring = {"latitude":latitude,"longitude":longitude,"range":"0"}
    near_city_headers = {
        'x-rapidapi-host': "geocodeapi.p.rapidapi.com",
        'x-rapidapi-key': "8840d3da12msh74280e203685253p142c1djsnee61630c4777"
        }
    near_city_response = requests.request("GET", near_city_url, headers=near_city_headers, params=near_city_querystring)
    data = near_city_response.json()

    country1        = data[0].get('Country') 
    city1           = data[0].get('City')
    distance1       = data[0].get('Distance') 
    lat1            = data[0].get('Latitude')
    lng1            = data[0].get('Longitude')
    
    country2        = data[1].get('Country') 
    city2           = data[1].get('City')
    distance2       = data[1].get('Distance') 
    lat2            = data[1].get('Latitude')
    lng2            = data[1].get('Longitude')

    country3        = data[2].get('Country') 
    city3           = data[2].get('City')
    distance3       = data[2].get('Distance') 
    lat3            = data[2].get('Latitude')
    lng3            = data[2].get('Longitude')

    data = {
        'country1': country1,
        'city1': city1,
        'distance1': distance1,
        'lat1': lat1,
        'lng1': lng1,

        'country2': country2,
        'city2': city2,
        'distance2': distance2,
        'lat2': lat2,
        'lng2': lng2,

        'country3': country3,
        'city3': city3,
        'distance3': distance3,
        'lat3': lat3,
        'lng3': lng3
    }

    return data






