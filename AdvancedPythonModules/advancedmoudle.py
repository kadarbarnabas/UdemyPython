import zipfile
import os
import re
"""
zip_obj = zipfile.ZipFile('c:/Users/Barnus/Desktop/python/pythontst/UdemyHomework/AdvancedPythonModules/unzip_me_for_instructions.zip', 'r')
zip_obj.extractall()

f = open('c:/Users/Barnus/Desktop/python/pythontst/UdemyHomework/AdvancedPythonModules/extracted_content/Instructions.txt', 'r')
conent = f.read()
print(conent)
f.close()

treelist = os.listdir('c:/Users/Barnus/Desktop/python/pythontst/UdemyHomework/AdvancedPythonModules/extracted_content')
"""
file_path = 'c:/Users/Barnus/Desktop/python/pythontst/UdemyHomework/AdvancedPythonModules/extracted_content'
for folder, sub_folder, files in os.walk(file_path): 
    for f in files:
        fo = open(f"{folder}/{f}",'r')
        conntent = fo.read()
        number = re.search(r'\d{3}-\d{3}-\d{4}', conntent)
        if number:
            print(number.group())
        fo.close()
