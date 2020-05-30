import pandas as pd
from planet import api
from constants import PLANET_API_KEY


CSV_PATH = '/datasets/rpartsey/satellite/planet/smart_crop/ready_for_api.csv'
df = pd.read_csv(CSV_PATH)

client = api.ClientV1(api_key=PLANET_API_KEY)

