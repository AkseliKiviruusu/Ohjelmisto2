import requests
import api_key
degree = u'\N{DEGREE SIGN}'

def main():
    pk = input('Anna paikkakunnan nimi: ')
    request = f'https://api.openweathermap.org/data/2.5/weather?q={pk}&appid=' + f'{api_key.api_key}'

    try:
        response = requests.get(request)
        response.raise_for_status()
        if response.status_code == 200:
            json_response = response.json()
            #print(json.dumps(json_response, indent=4))
            print(f'\nLämpötila paikkakunnalla {pk}:\n{json_response['main']['temp']-272.15:.1f} C{degree}')
    except requests.exceptions.RequestException as e:
        print ("Hakua ei voitu suorittaa.")
    return
main()