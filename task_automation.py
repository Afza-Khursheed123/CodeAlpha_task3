import os
import shutil
path = r'C:\Users\AFZA KHURSHEED.DESKTOP-LLBTUSQ\Documents'

try:
   
    for file in os.listdir(path):

        if os.path.isfile(os.path.join(path, file)):

            file_extension = os.path.splitext(file)[1].lower()

            if not os.path.exists(os.path.join(path, file_extension[1:])):
                os.makedirs(os.path.join(path, file_extension[1:]))

            shutil.move(os.path.join(path, file), os.path.join(path, file_extension[1:], file))
    
    print("Files organized successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
input("press enter to exit!")