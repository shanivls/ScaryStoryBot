import os
import time

import yaml
from config.config import config, update_config
from moviepy.editor import VideoFileClip

input_directory = config["directories_paths"]["base_videos"]
output_directory = config["directories_paths"]["cut_videos"]

last_video_time = config["video"]["last_video_time"]
default_file_name = config["video"]["default_file_name"]
video_index = config["video"]["video_index"]
video_subindex = config["video"]["video_subindex"]
video_length = config["video"]["video_length"]


def cut_video(input_file_name, output_file_name, start_time, end_time):
    global video_length
    input_path = os.path.join(input_directory, input_file_name)
    output_path = os.path.join(output_directory, output_file_name)

    clip = VideoFileClip(input_path)
    trimmed_clip = clip.subclip(start_time, end_time)
    trimmed_clip.write_videofile(output_path)

    video_length = clip.duration


def create_clip(length: int):
    global last_video_time, video_index, video_subindex, video_length
    if last_video_time + length > video_length:
        video_index = video_index + 1
        video_subindex = 1
        last_video_time = 0
    video_name = default_file_name + str(video_index)
    part = video_subindex

    start_time = time.strftime("%H:%M:%S", time.gmtime(last_video_time))
    end_time = time.strftime("%H:%M:%S", time.gmtime(last_video_time + length))

    input_file_name = f"{video_name}.mp4"
    output_file_name = f"{video_name}.{part}.mp4"
    cut_video(input_file_name, output_file_name, start_time, end_time)
    last_video_time = last_video_time + length
    video_subindex = video_subindex + 1
    update_config_values()


def update_config_values():
    config["video"]["last_video_time"] = last_video_time
    config["video"]["video_index"] = video_index
    config["video"]["video_subindex"] = video_subindex
    config["video"]["video_length"] = video_length
    update_config(config)
