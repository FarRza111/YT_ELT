
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("API_KEY", "").strip()
# CHANNEL_HANDLE = os.getenv("CHANNEL_HANDLE", "").strip()
# MAX_RESULTS = int(os.getenv("MAX_RESULTS", "50"))


# # try:

# #     url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

# #     response = requests.get(url)

# #     # response.raise_for_status()

# #     data = response.json()

# #     # print(json.dumps(data,indent=4))

# #     channel_items = data["items"][0]

# #     channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"][
# #         "uploads"
# #     ]

# # except requests.exceptions.RequestException as e:
# #     raise e


# def get_playlist_id():

#     try:

#         url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

#         response = requests.get(url)

#         # response.raise_for_status()

#         data = response.json()

#         # print(json.dumps(data,indent=4))

#         channel_items = data["items"][0]

#         channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"][
#             "uploads"
#         ]

#         return channel_playlistId

#     except requests.exceptions.RequestException as e:
#         raise e


# ids = get_playlist_id()
# print(ids)
import logging
import json
from datetime import date
logger = logging.getLogger(__name__)

def load_data():

    file_path = f"./data/YT_data_{date.today()}.json"

    try:
        logger.info(f"Processing file: YT_data{date.today()})")

        with open(file_path, 'r', encoding='utf-8') as raw_data:
            data = json.load(raw_data)

        return data
    except FileNotFoundError:
        logger.error(f'File not found: {file_path}')
        raise
    except json.JSONDecodeError:
        logger.error(f'invalid Json in file {file_path}')
        raise


load_data()
