_Remarks:_
* Inpiration came from https://github.com/sanjujosh/auto-image-renamer, but since it used a legacy API i did it again.
* i am a bad coder....

# AI-Image-Renamer
This repository contains a Python script that utilizes AI to automatically rename images based on their content. The script leverages the Microsoft Cognitive Services Computer Vision API to extract image descriptions and uses them to create new, more meaningful file names.

## Getting Started

### Prerequisites
- Python 3.x
- A Microsoft Cognitive Services subscription key
- PIL library

### Installation
- Clone or download the repository
- Install PIL by running `pip install pillow`
- Replace `YOUR_SUBSCRIPTION_KEY` in the script with your actual subscription key
- Replace `endpoint_url` in the script with the desired endpoint URL (default is "https://westcentralus.api.cognitive.microsoft.com")

### Usage
- Run the script with the command `python script.py image_folder [recursive]`

- `image_folder` is the path to the folder containing your images
- `recursive` is an optional argument that, if provided, will make the script search for images in all subfolders.

### Examples
Default: `python3 ai-image-renamer.py "/Users/martinaltmann/Downloads/Website images cleaned/test"` will rename all images in that folder
Recursive: `python3 ai-image-renamer.py "/Users/martinaltmann/Downloads/Website images cleaned/test" recursive` will rename all images in that folder + subfolders

## Note
If the image already exists it will add a running number to it. Eg. You have three images with with a table and glass on it. The AI will create "table_with_glas_on_it" for the first and "table_with_glas_on_it_1" for the second. By this its not overwriting the images.

## Built With
- [Python3](https://www.python.org/)
- [Microsoft Cognitive Services Computer Vision API v3.2](https://westus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2) - AI image analysis
