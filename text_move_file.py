import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def clear_old_list_folder(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except Exception as e:
            print(f"Cannot delete {item_path}: {e}")
            return False
    return True

def move_old_data_to_old_list(dst):
    old_list_folder = os.path.join(dst, "Old_last")
    if not os.path.exists(old_list_folder):
        try:
            os.makedirs(old_list_folder)
        except PermissionError as e:
            print(f"Cannot create Old_last folder: {e}")
            return False
    else:
        if not clear_old_list_folder(old_list_folder):
            return False

    for item in os.listdir(dst):
        item_path = os.path.join(dst, item)
        if item != "Old_last":
            try:
                shutil.move(item_path, os.path.join(old_list_folder, item))
            except Exception as e:
                print(f"Cannot move {item_path} to {old_list_folder}: {e}")
                return False
    return True

def copy_directory(src, dst):
    try:
        if os.path.exists(dst):
            if not move_old_data_to_old_list(dst):
                return False
        else:
            os.makedirs(dst)

        for item in os.listdir(src):
            source_path = os.path.join(src, item)
            destination_path = os.path.join(dst, item)

            try:
                if os.path.isdir(source_path):
                    shutil.copytree(source_path, destination_path)
                else:
                    shutil.copy2(source_path, destination_path)
            except Exception as e:
                print(f"Cannot copy {source_path} to {destination_path}: {e}")
                return False

        for item in os.listdir(dst):
            destination_path = os.path.join(dst, item)
            if os.path.isfile(destination_path):
                print(f"Processing file: {destination_path}")

        return True
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def select_folder(title):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

def read_destinations_from_file(filename):
    try:
        with open(filename, 'r') as file:
            destinations = [line.strip().replace('\\', '/') for line in file if line.strip()]
        return destinations
    except Exception as e:
        print(f"Error reading destinations file: {e}")
        return []

def main():
    print("Select the source folder:")
    source_folder = select_folder("Select Source Folder")
    if not source_folder:
        messagebox.showerror("Error", "No source folder selected.")
        return

    destination_file = 'destinations.txt'
    destination_folders = read_destinations_from_file(destination_file)

    if not destination_folders:
        messagebox.showerror("Error", "No destination folders found in destinations.txt.")
        return

    successful_destinations = []
    failed_destinations = []

    for destination_folder in destination_folders:
        if copy_directory(source_folder, destination_folder):
            successful_destinations.append(destination_folder)
            print(f"Copied to {destination_folder}")
        else:
            failed_destinations.append(destination_folder)
            print(f"Failed to copy to {destination_folder}")

    try:
        with open('successful_destinations.txt', 'w') as file:
            for folder in successful_destinations:
                file.write(f"{folder}\n")
    except Exception as e:
        print(f"Error writing successful destinations file: {e}")

    try:
        with open('failed_destinations.txt', 'w') as file:
            for folder in failed_destinations:
                file.write(f"{folder}\n")
    except Exception as e:
        print(f"Error writing failed destinations file: {e}")

if __name__ == "__main__":
    main()
