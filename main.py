import openai
import json

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "London", "Birmingham", "Glasgow", "Liverpool", "Bristol",
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice",
    "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt",
    "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo",
    "Beijing", "Shanghai", "Tianjin", "Shenzhen", "Guangzhou",
    "Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod",
    "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Ahmedabad",
    "Cairo", "Alexandria", "Giza", "Shubra El Kheima", "Port Said",
    "Sao Paulo", "Rio de Janeiro", "Brasilia", "Fortaleza", "Salvador",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
    "Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa",
    "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Toluca",
    "Rome", "Milan", "Naples", "Turin", "Palermo",
    "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza",
    "Buenos Aires", "Cordoba", "Rosario", "Mendoza", "Tucuman",
    "Istanbul", "Ankara", "Izmir", "Bursa", "Adana"
]

def find_city(response):
    resp = response.lower()
    for city in cities:
        if city.lower() in resp:
            return city

    return None

def get_text_from_speech():
    audio_file= open("/path/to/file/audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = json.dumps(transcript)
    find_city(transcript)
