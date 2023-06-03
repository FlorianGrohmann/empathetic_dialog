# create a dataframe out of the empatheticdialogues dataset


import pandas as pd
import os

def create_dataframe(splitname, data_folder):
    df = open(os.path.join(data_folder, f"{splitname}.csv")).readlines()
    history = []
    data = []
    for i in range(1, len(df)):
        cparts = df[i - 1].strip().split(",")
        sparts = df[i].strip().split(",")
        if cparts[0] == sparts[0]:
            label = "Ai: " if int(cparts[1]) % 2 == 0 else "User: "
            prevsent = label + cparts[5].replace("_comma_", ",")
            history.append(prevsent)
            idx = int(sparts[1])
            if (idx % 2) == 0:
                label = "Ai: " if idx % 2 == 0 else "User: "
                prev_str = " ".join(history)
                sent = label + sparts[5].replace("_comma_", ",")
                data.append((sparts[0], sparts[1], prev_str, sent))
        else:
            history = []
    df = pd.DataFrame(data, columns=["conv_id", "utterance_idx", "context", "utterance"])
    return df