from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path('./.env')

load_dotenv(dotenv_path)

def get_user(username):
    if(username == "Saoirse"):
        saoirse_id = os.getenv("SAOIRSE_ID", "not found")
        saoirse_secret = os.getenv("SAOIRSE_SECRET", "not found")
        
        if saoirse_id and saoirse_secret:
            os.environ['SPOTIPY_CLIENT_ID'] = saoirse_id
            os.environ['SPOTIPY_CLIENT_SECRET'] = saoirse_secret
            print(os.getenv('SPOTIPY_CLIENT_ID'))
        else:
            print("SAOIRSE credentials not found in .env")

    elif (username == "Harris"): 
        os.environ['SPOTIPY_CLIENT_ID'] = os.getenv("HARRIS_ID", "not found")
        os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv("HARRIS_SECRET", "not found")

        print("Switching to Harris")