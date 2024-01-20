
# Modification date: Thu Jun 23 22:27:46 2022

# Production date: Sun Sep  3 15:44:22 2023

"""

Source: https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python


"""




import cv2
import os

image_folder = 'C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\output'
video_name = 'wtdoneforreal.mp4'
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
"""
images2 = []
counter = 1
for i in range(len(images)):
    if counter == 4:
        images2.append(images[i])
        counter = 1
    else:
        counter += 1
print("loop done")
"""
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 60, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4
