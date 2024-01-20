
# Modification date: Thu Jun 23 13:41:42 2022

# Production date: Sun Sep  3 15:44:21 2023

"""

Source: https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd

"""
import moviepy.editor as mp
video_name = input("Enter the video name to extract the audio: ")
my_clip = mp.VideoFileClip(video_name)
my_clip.audio.write_audiofile(f"{video_name}_audio.mp3")
input("Done! Press enter to continue...")
