import json
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).with_name('.env'))


CHANNEL_HANLDE = "MrBeast"
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise RuntimeError("API_KEY is not set. Check the .env file and its path.")


def get_playlist_id():

    try:
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANLDE}&key={API_KEY}'

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        items = data.get('items', [])
        if not items:
            raise ValueError(f"No channel found for handle {CHANNEL_HANLDE!r}: {data}")

        channel_items = items[0]
        
        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']
        
        print(channel_playlistId)
        
        return channel_playlistId
    
    except (requests.exceptions.RequestException, ValueError, KeyError, IndexError) as e:
        raise e


if __name__ ==  "__main__":
    get_playlist_id()


    