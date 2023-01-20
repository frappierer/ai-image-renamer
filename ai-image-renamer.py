import os
import requests
from os.path import exists
from PIL import Image
import sys

# Replace with your Cognitive Services subscription key
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Allowed image extensions
allowed_extensions = {'jpeg', 'jpg', 'png'}

# Replace with the desired language code. Options: en (English),es (Spanish),ja (Japanese),pt (Portugese),zh (Chinese Simplified)
language = "en"

# Replace with the desired endpoint URL
endpoint_url = "https://XXXXXXXXXX.cognitiveservices.azure.com"

if len(sys.argv) < 2:
    print("usage: python script.py image_folder [recursive]")
    sys.exit()

# Get the image folder from the argument
image_folder = sys.argv[1]

# Check if recursive flag is provided
recursive = False
if len(sys.argv) > 2 and sys.argv[2] == "recursive":
    recursive = True
i = 1
# Iterate through all files in the image folder and all subfolders if recursive flag is provided
if recursive:
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            # Check if file has an allowed extension
            if file.split('.')[-1] in allowed_extensions:
                file_path = os.path.join(root, file)
                # Open the image file
                with open(file_path, "rb") as image_file:
                    # Send the image to the Computer Vision API
                    vision_url = endpoint_url+"/vision/v3.2/describe?language="+language
                    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
                    response = requests.post(vision_url, headers=headers, data=image_file)
                    response.raise_for_status()
                    # Get the image description from the API response
                    image_description = response.json()["description"]["captions"][0]["text"].capitalize()
                    # Create a new file name based on the image description
                    new_file_name = image_description.replace(" ", "_") + "." + file.split(".")[-1]
                    # Rename the image file
                    new_file_path = os.path.join(root, new_file_name)
                    #Check if files exists
                    if os.path.isfile(new_file_path):
                        print ("File exist. Adding suffix")
                        new_file_name = image_description.replace(" ", "_") + '_' + str(i) + "." + file.split(".")[-1]
                        # Rename the image file
                        new_file_path = os.path.join(root, new_file_name)
                        os.rename(file_path, new_file_path)
                        #os.rename(file_path, new_file_path + '_' + str(i))
                        # new_file_path = new_file_path + '_' + str(i)
                        i += 1
                        print("File name exists. Added suffix. Renamed " + file + " to " + new_file_name)

                    else:
                        os.rename(file_path, new_file_path)
                        print("Renamed " + file + " to " + new_file_name)
                

else:
    for file in os.listdir(image_folder):
        # Check if file has an allowed extension
        if file.split('.')[-1] in allowed_extensions:
            file_path = os.path.join(image_folder, file)
            # Open the image file
            with open(file_path, "rb") as image_file:
                # Send the image to the Computer Vision API
                vision_url = endpoint_url+"/vision/v3.2/describe?language="+language
                headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
                response = requests.post(vision_url, headers=headers, data=image_file)
                response.raise_for_status()
                # Get the image description from the API response
                image_description = response.json()["description"]["captions"][0]["text"].capitalize()
                # Create a new file name based on the image description
                new_file_name = image_description.replace(" ", "_") + "." + file.split(".")[-1]
                # Rename the image file
                new_file_path = os.path.join(image_folder, new_file_name)
                #Check if files exists
                if os.path.isfile(new_file_path):
                    print ("File exist. Adding suffix")
                    new_file_name = image_description.replace(" ", "_") + '_' + str(i) + "." + file.split(".")[-1]
                    # Rename the image file
                    new_file_path = os.path.join(image_folder, new_file_name)
                    os.rename(file_path, new_file_path)
                    #os.rename(file_path, new_file_path + '_' + str(i))
                    # new_file_path = new_file_path + '_' + str(i)
                    i += 1
                    print("File name exists. Added suffix. Renamed " + file + " to " + new_file_name)

                else:
                    os.rename(file_path, new_file_path)
                    print("Renamed " + file + " to " + new_file_name)
                
