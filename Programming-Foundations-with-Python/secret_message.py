import os
def rename_files():
    #(1) get file names from Folder
    
    list_files = os.listdir(r"PATH to message files")
    print (list_files)
    save_path=os.getcwd()
    print(save_path)    
    os.chdir(r"PATH to message files")

    #(2) for each file rename filename
    for file_name in list_files:
        print("Old name - " + file_name)
        print("New Name - " + file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(save_path)
    
rename_files()
