# Import os and json modules
import os
import json
import subprocess


subprocess.run(["npm install"], shell=True)

# Define the folder path
folder_path = "./src/assets/images/"

# Create an empty list to store the file names and directories
namaArr = []

nama = input('Untuk siapa? ')

# Create a dictionary with the file name and directory
namaDict = {"name": nama}
# Append the dictionary to the list
namaArr.append(namaDict)

# Convert the list to a json string
jason = json.dumps(namaArr, indent=4)


with open('./src/nama.json', "w") as f:
    json.dump(namaArr, f, indent=4)
    
    
# Create an empty list to store the file names and directories
replyList = []

reply = input('Mau bilang apa kalau kabarnya baik? ')

# Create a dictionary with the file name and directory
replyDict = {"balas": reply}
# Append the dictionary to the list
replyList.append(replyDict)

reply = input('Mau bilang apa kalau kabarnya buruk? ')

# Create a dictionary with the file name and directory
replyDict = {"balas": reply}
# Append the dictionary to the list
replyList.append(replyDict)

# Convert the list to a json string
jason = json.dumps(replyList, indent=4)

with open('./src/kabar.json', "w") as f:
    json.dump(replyList, f, indent=4)
    
    
# Define the folder path
folder_path = "./public/videos/"

# Create an empty list to store the file names and directories
file_list = []

# Loop through the files in the folder
for file in os.listdir(folder_path):
    # Get the full path of the file
    file_path = os.path.join('./videos/', file)
    # Create a dictionary with the file name and directory
    file_dict = {"name": file, "directory": file_path}
    # Append the dictionary to the list
    file_list.append(file_dict)

# Convert the list to a json string
file_json = json.dumps(file_list, indent=4)

print('Video berhasil di setup')

with open('./src/galleryVid.json', "w") as f:
    json.dump(file_list, f, indent=4)
    
    # Import os and json modules
import os
import json

# Define the folder path
folder_path = "./public/images/"

# Create an empty list to store the file names and directories
file_list = []

# Loop through the files in the folder
for file in os.listdir(folder_path):
    # Get the full path of the file
    file_path = os.path.join('./images/', file)
    # Create a dictionary with the file name and directory
    file_dict = {"name": file, "directory": file_path}
    # Append the dictionary to the list
    file_list.append(file_dict)

# Convert the list to a json string
file_json = json.dumps(file_list, indent=4)

print('Image berhasil di setup')

with open('./src/gallery.json', "w") as f:
    json.dump(file_list, f, indent=4)
    
    
subprocess.run(["npm run build"], shell=True)


with open("./dist/index.html", "r") as f:

    content = f.read()

    content = content.replace('"/', '"./')

    f.close()

with open("./dist/index.html", "w") as f:

    f.write(content)

    f.close()