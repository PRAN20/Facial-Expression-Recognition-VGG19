from zipfile import ZipFile
import os
  
def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths        
  
def main():
    directory = '/home/pranit/Facial-Expression-Recognition.Pytorch'
    file_paths = get_all_file_paths(directory)
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    with ZipFile('my_python_files.zip','w') as zip:
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')        
  
if __name__ == "__main__":
    main()