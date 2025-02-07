import pandas as pd
import json
import os
from tqdm import tqdm

#### training videos
with open('vatex_training_v1.0.json') as f:
    d = json.load(f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/train/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        for i in range(len(vid["enCap"])):
            anns.append({"image_id": vid["videoID"]+".mp4", "video": vid["videoID"]+".mp4", "caption": vid["enCap"][i]})
    else:
        pass

with open('cap_train.json', 'w') as f:
    json.dump(anns, f)

##### validation videos
with open('vatex_validation_v1.0.json') as f:
    d = json.load(f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/val/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        for i in range(len(vid["enCap"])):
            anns.append({"image_id": vid["videoID"]+".mp4", "video": vid["videoID"]+".mp4", "caption": vid["enCap"][i]})
    else:
        pass

with open('vatex_val_gt.json', 'w') as f:
    json.dump({"annotations": anns}, f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/val/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        caps = []
        for i in range(len(vid["enCap"])):
            caps.append(vid["enCap"][i])
            anns.append({"image_id": vid["videoID"]+".mp4", "video": vid["videoID"]+".mp4", "caption": caps})
    else:
        pass

with open('cap_val.json', 'w') as f:
    json.dump(anns, f)

#### test videos
with open('vatex_public_test_english_v1.1.json') as f:
    d = json.load(f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/test/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        for i in range(len(vid["enCap"])):
            anns.append({"image_id": vid["videoID"]+".mp4", "video": vid["videoID"]+".mp4", "caption": vid["enCap"][i]})
    else:
        pass

with open('vatex_test_gt.json', 'w') as f:
    json.dump({"annotations": anns}, f)

anns = []
for vid in tqdm(d):
    v_name = vid["videoID"]
    v_name = "videos/test/" + v_name + ".mp4"
    if os.path.isfile(v_name):
        caps = []
        for i in range(len(vid["enCap"])):
            caps.append(vid["enCap"][i])
            anns.append({"image_id": vid["videoID"]+".mp4", "video": vid["videoID"]+".mp4", "caption": caps})
    else:
        pass

with open('cap_test.json', 'w') as f:
    json.dump(anns, f)