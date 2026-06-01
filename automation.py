import os
import shutil
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# ---------------- SORT FILES ----------------
def sort_files(source_folder, destination_folder):

    if not os.path.exists(source_folder):
        print("Source folder not found!")
        return

    create_folder(destination_folder)

    count = 0

    for file in os.listdir(source_folder):

        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1][1:].lower()

            if ext == "":
                ext = "others"

            ext_folder = os.path.join(destination_folder, ext)

            create_folder(ext_folder)

            shutil.move(
                file_path,
                os.path.join(ext_folder, file)
            )

            count += 1

            print(f"Moved: {file}")
            logging.info(f"Moved: {file}")

    print(f"\nTotal Files Moved: {count}")


# ---------------- RENAME FILES ----------------
def rename_files(folder_path):

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    count = 1

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1]

            new_name = f"file_{count}{ext}"

            new_path = os.path.join(folder_path, new_name)

            os.rename(file_path, new_path)

            print(f"{file} -> {new_name}")

            logging.info(f"Renamed {file} to {new_name}")

            count += 1

    print("Renaming Completed")


# ---------------- CLEAN EMPTY FOLDERS ----------------
def clean_empty_folders(folder_path):

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    removed = 0

    for root, dirs, files in os.walk(folder_path, topdown=False):

        if not dirs and not files:

            os.rmdir(root)

            removed += 1

            print(f"Deleted Empty Folder: {root}")

            logging.info(f"Deleted Empty Folder: {root}")

    print(f"Total Empty Folders Removed: {removed}")


# ---------------- MENU ----------------
while True:

    print("\n===== FILE AUTOMATION TOOL =====")
    print("1. Sort Files")
    print("2. Rename Files")
    print("3. Clean Empty Folders")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        source = input("Enter Source Folder: ")
        destination = input("Enter Destination Folder: ")

        sort_files(source, destination)

    elif choice == "2":

        folder = input("Enter Folder Path: ")

        rename_files(folder)

    elif choice == "3":

        folder = input("Enter Folder Path: ")

        clean_empty_folders(folder)

    elif choice == "4":

        print("Program Closed")
        break

    else:

        print("Invalid Choice")