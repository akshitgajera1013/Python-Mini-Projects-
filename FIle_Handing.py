from pathlib import Path
import shutil

def create_folder():
    try:
        name=input("Please provide your folder name : - ")
        p=Path(name)
        p.mkdir()
        print("Folder Created succesfully.")
    except Exception as e:
        print(f"Sorry an error occured as {e}")

def read_files_folder():
    p=Path("")
    items=list(p.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i + 1} : {v}")

def update_folder():
    try:
        read_files_folder()
        old_name=input("Please tell which folder you want to update : - ")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("Please tell your new folder name : - ")
            new_p=Path(new_name)
            p.rename(new_p)
            print("Your folder name is updated sucesfully.")
        else:
            print("Sorry,No such Folder Exists.")
    except Exception as e:
        print(f"An Error occured as {e}")


def delete_folder():
    try:
        read_files_folder()
        name=input("Please tell which folder you want to delete : - ")
        p=Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("Folder is deleted succesfully.")
        else:
            print("No such folder exsists")
    except Exception as e:
        print(f"Sorry, some error occured as {e}")


def create_file():
    try:
        read_files_folder()
        name=input("Please,tell your file name : - ")
        p=Path(name)
        if not p.exists():
            with open(name,"w") as f:
                data=input("Write your data to this file :- ")
                f.write(data)
                print("Your file created succesfully.")
        else:
            print("Sorry file already exists!")
    except Exception as e:
        print(f"Some error occured as {e}")


def read_file():
    try:
        read_files_folder()
        name=input("Please tell your file name you want to read : - ")
        p=Path(name)
        if p.exists and p.is_file():
            with open(name,"r") as f:
                content=f.read()
                print(f"Your file content is :-")
                print(content)
        else:
            print("Sorry, No such file exists.")

    except Exception as e:
        print("Some error occured as {e}")


def update_file():
    try:
        read_files_folder()
        old_name=input("Please,tell which file you want to update : -  ")
        p=Path(old_name)
        if p.exists() and p.is_file():
            print("Options :- ")
            print("1. For Rename the File.")
            print("2. Append Somethink in File.")
            print("3. For Over-writing the file content.")
            choice=int(input("Please,enter your choice : - "))

            if choice == 1:
                new_name=input("Tell your new name with extention : - ")
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name changed succesfully.")
                else:
                    print("Sorry, this name already exists.")


            if choice == 2:
                with open(old_name,"a") as f:
                    data=input("Enter ou want to add in file : -  ")
                    f.write(" " +data)
                    print("Appended succesfully.")
                
            if choice == 3:  
                with open(old_name,"w") as f:
                    data=input("Enter ou want to add in file : -  ")
                    f.write(" " +data)
                    print("Over-writing succesfully.")

    except Exception as e:
        print("Some error occured as {e}")


def delete_file():
    try:
        read_files_folder()
        name=input('Please,tell which file you want to delete : - ')
        p=Path(name)
        if p.exists() and p.is_file():
           p.unlink()
           print("File was deleted succesfully.")
        else:
            print("Sorry,No such file exists.")
    except Exception as e:
        print(f"Some error occured as {e}")



while True:
    print("Options : -")

    print("1. Create a folder")
    print("2. Read files and folders")
    print("3. Update the folder")
    print("4. Delete the folder")
    print("5. Create a file")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. To exist ")

    choice=int(input("Enter your option: "))

    if choice == 1:
        create_folder()

    if choice == 2 :
        read_files_folder()

    if choice == 3:
        update_folder()

    if choice == 4:
        delete_folder()

    if choice == 5:
        create_file()

    if choice == 6:
        read_file()

    if choice == 7:
        update_file()

    if choice == 8:
        delete_file()

    if choice == 0:
        break
