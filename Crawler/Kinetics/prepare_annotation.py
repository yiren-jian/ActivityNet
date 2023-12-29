import pandas as pd
import json
import os
from tqdm import tqdm

with open('vatex_training_v1.0.json') as f:
    d = json.load(f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/train/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        for i in range(len(vid["enCap"])):
            anns.append({"image_id": v_name, "video": v_name, "caption": vid["enCap"][i]})
    else:
        pass

with open('cap_train.json', 'w') as f:
    json.dump(anns, f)
