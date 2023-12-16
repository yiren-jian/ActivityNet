import pandas as pd
import json

with open('vatex_validation_v1.0.json') as f:
    d = json.load(f)

ids = []
starts = []
ends = []
splits = []
for video in d:
    v = video["videoID"]
    id = v[:-14]
    start = v[-13:-7]
    end = v[-6:]

    ids.append(id)
    starts.append(start)
    ends.append(end)
    splits.append("val")

data = pd.DataFrame([ids, starts, ends, splits]) # Each list would be added as a row
data = data.transpose() # To Transpose and make each rows as columns
data.columns = ['youtube_id', 'time_start', 'time_end', 'split'] # Rename the columns


data.to_csv('data/vatex_val.csv', sep=',', index=False)