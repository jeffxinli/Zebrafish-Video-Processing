import os
import numpy as np
import cv2
from glob import glob

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=10):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    ind = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if ind == 0:
            cv2.imwrite(f"{save_path}/{ind}.png", frame)
        else:
            if ind % gap == 0:
                cv2.imwrite(f"{save_path}/{ind}.png", frame)

        ind += 1

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "save"

    for path in video_paths:
        save_frame(path, save_dir)

    for path in video_paths:
        save_frame(path, save_dir, gap=10)

# https://www.youtube.com/watch?v=SWGd2hX5p3U
# change gap = 10 to gap = 1 for now skip frames (lines 13 & 44)