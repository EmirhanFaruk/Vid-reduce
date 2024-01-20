
# Modification date: Wed Jun 22 13:40:28 2022

# Production date: Sun Sep  3 15:44:22 2023

import os
from PIL import Image
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from clear_screen import clear#clear()
from datetime import datetime
import random



def paths():

    prefixes = str(input("Enter the prefix of the edited images: "))

    if prefixes == "" or prefixes == "conda activate imgedit":
        prefixes = "edited_"
    else:
        prefixes = prefixes + "_"

    print(f"Using the prefix: {prefixes}")

    the_name_of_the_file = input("Enter the name of the source file: ")


    if the_name_of_the_file == "" or the_name_of_the_file == "conda activate imgedit":
        the_name_of_the_file = "\\input"
    else:
        the_name_of_the_file = "\\" + the_name_of_the_file

    print("Using the file: " + the_name_of_the_file[1:])
    #print(the_name_of_the_file.split("\\"))
    the_name_of_the_file2 = the_name_of_the_file.split("\\")[1]

    #\\the_edited_images
    the_destination_file = input("Enter the destination file: ")

    if the_destination_file == "" or the_destination_file == "conda activate imgedit":
        the_destination_file = "\\output"
    else:
        the_destination_file = "\\" + the_destination_file
    
    print("Using the destination file: " + the_destination_file[1:])

    print(f"\n\n\nUsing the prefix: {prefixes}\nUsing the file: {the_name_of_the_file[1:]}\nUsing the destination file: {the_destination_file[1:]}")
    the_answer = input("\nAre those paths good? (y for yes, put anything but y to reenter)\n: ")
    if the_answer == "y":  
        return the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes
    else:
        clear()
        return paths()

the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes = paths()


arr = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce" + the_name_of_the_file)

larr = len(arr)
for i in range(larr):
    arr[i] = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\vid reduce{the_name_of_the_file}\\" + arr[i]

sussy_file_name = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\vid reduce{the_name_of_the_file}\\"
"""
for i in range(len(arr)):
        arr[i] = "C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\vid reduce\\the_images\\" + arr[i]
        os.rename(arr[i], f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\vid reduce\\the_images\\sc_{i + 1}.png")
"""

start_time = datetime.now()
start_time2 = time.time()
start_time3 = datetime.now()
start_time = [start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute, start_time.second]
#start_time[3] + start_time[4] + start_time[5] for h/m/s


# Loading bar. Returns the start of the time of the image as [hour, minute, second].
def load_bar(delta_time, start_time, photos_done, total_photos, arr, i):
    clear()
    print("Using the folder: " + the_name_of_the_file[1:])
    print(f"The loop started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}")
    print(f"Last image done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    print(f"Image {i + 1} of {total_photos}")
    print(f"The file: {str(arr[i]).split(sussy_file_name)[1]}")
    green_bars_num = int((((photos_done) / len(arr)) * 100))
    green_bars = " " * green_bars_num
    white_bars = " " * (100 - green_bars_num)
    print(Back.GREEN + green_bars + Back.RED + white_bars)
    the_image_time = datetime.now()
    the_image_time = [the_image_time.hour, the_image_time.minute, the_image_time.second]
    return the_image_time



line = []
with open("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\The_Try.txt", "r") as f:
    line = f.readlines()
f.close()
n_try = int(line[0])
with open("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\The_Try.txt", "w") as f:
    line = f.write(str(n_try + 1))
f.close()


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\the_logs.txt", "a")
f.write(f"\n\n\n---------------------------------------------------------------------\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]} started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}\n\n\n")
f.close()

now_for_imgs = datetime.now()
delta_time = [0, 0, 0]
photos_done = 0
total_photos = larr


for i in range(len(arr)):
    now_for_imgs = datetime.now()
    dt_string1 = now_for_imgs.strftime("%d/%m/%Y %H:%M:%S")
    image = Image.open(arr[i])
    width, height = image.size
    #print(width, height)
    
    the_image_time = load_bar(delta_time, start_time, photos_done, total_photos, arr, i)
    
    streak = []
    sc = -1
    try:
        for y in range(height):
            #clear()
            #print(f"%{int(y/ height * 100) + 1}")
            #print(f"{y} / {height}")
            
            onst = False
            x = 0
            #time things
            now_for_imgs2 = datetime.now()
            dt_string2 = now_for_imgs2.strftime("%d/%m/%Y %H:%M:%S")
            img_break_time = time.time()
            current_running_time = int(img_break_time - start_time2)
            #print(f"%{int(((w) / (width)) * 100)} | Current time: {dt_string2}, the program has been running for {current_running_time// 60} minutes {current_running_time - (current_running_time // 60 * 60)} seconds.    ", end = "\r")
        
            while x < width - 1:
                #print(x, y)
                rgb = image.getpixel((x, y))
                rgb2 = image.getpixel((x + 1, y))
                cases = [abs(rgb[0] - rgb2[0]) < 3, abs(rgb[1] - rgb2[1]) < 3, abs(rgb[2] - rgb2[2]) < 3]
                passing = False
                for bruh in range(len(cases)):
                    if cases[bruh]:
                        passing = True
                    else:
                        onst = False
                        break
                if passing:
                    if not onst:
                        sc += 1
                        streak.append([])
                    onst = True
                    if not ((x, y), rgb) in streak[sc]:
                        streak[sc].append(((x, y), rgb))
                    if not ((x + 1, y), rgb2) in streak[sc]:
                        streak[sc].append(((x + 1, y), rgb2))
                x += 1

        if len(streak) > 0:
            for daL in range(len(streak)):
                ct = len(streak[daL])
                counter = 0
                r = 0
                g = 0
                b = 0
                while counter < ct:
                    r += streak[daL][counter][1][0]
                    g += streak[daL][counter][1][1]
                    b += streak[daL][counter][1][2]
                    counter += 1
                mr = r // len(streak[daL])
                mg = g // len(streak[daL])
                mb = b // len(streak[daL])
                for j in range(len(streak[daL])):
                    image.putpixel(streak[daL][j][0], (mr, mg, mb))
    except Exception as e:
        
        #streak = sample(streak, len(streak))
        for daL in range(len(streak)):
            ct = len(streak[daL])
            counter = 0
            r = 0
            g = 0
            b = 0
            while counter < ct:
                r += streak[daL][counter][1][0]
                g += streak[daL][counter][1][1]
                b += streak[daL][counter][1][2]
                counter += 1
            mr = r // len(streak[daL])
            mg = g // len(streak[daL])
            mb = b // len(streak[daL])
            for j in range(len(streak[daL])):
                image.putpixel(streak[daL][j][0], (mr, mg, mb))
	
        path = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce{the_destination_file}\\{prefixes}%#05d" % (i+1) + ".jpg"
        image.save(path)
        print(width, height)
        print(y, x)
        input(e)

    #print(len(arr), i)

    #print(str(arr[i]).split(sussy_file_name)[1])
    #print(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce{the_destination_file}\\{the_name_of_the_file2}{the_name_of_the_file2}{str(str(arr[i]).split(sussy_file_name)[1])[:-3]}%#05d" % (i+1) + ".png")
    path = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce{the_destination_file}\\{prefixes}%#05d" % (i+1) + ".jpg"
    image.save(path)
    image.close()
    photos_done += 1
    
    the_image_time_end = datetime.now()
    the_image_time_end = [the_image_time_end.hour, the_image_time_end.minute, the_image_time_end.second]
    delta_time = [the_image_time_end[0] - the_image_time[0], the_image_time_end[1] - the_image_time[1], the_image_time_end[2] - the_image_time[2]]
    if delta_time[2] < 0:
        delta_time[2] = delta_time[2] + 60
        delta_time[1] -= 1
    if delta_time[1] < 0:
        delta_time[1] = delta_time[1] + 60
        delta_time[0] -= 1
    f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\the_logs.txt", "a")
    f.write(f"\n\nImage {i + 1} ({str(arr[i]).split(sussy_file_name)[1]}) from the folder {the_name_of_the_file[1:]} has been done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    f.close()



finish = time.time()

total_time = finish - start_time2

now2 = datetime.now()
# dd/mm/YY H:M:S
dt_string = start_time3.strftime("%d/%m/%Y %H:%M:%S")
print("Started at ", dt_string)	
# dd/mm/YY H:M:S
dt_string = now2.strftime("%d/%m/%Y %H:%M:%S")


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\vid reduce\\the_logs.txt", "a")

f.write(f"\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]}, all done in {int(total_time)} seconds({int(total_time/60)} minutes and {int(total_time % 60)} seconds). The program ended at {dt_string}")

f.close()

print("Ended at ", dt_string)	
print(f"All done in {total_time}")
