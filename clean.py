import os
import shutil
import sys

def clean_folder(target_folder, extensions):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in extensions:
                file_path = os.path.join(root, file)
                print(f"Removing {file_path}")
                os.remove(file_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: clean-folder <target_folder> <extensions>")
        sys.exit(1)

    target_folder = sys.argv[1]
    extensions = sys.argv[2].split(',')

    clean_folder(target_folder, extensions)

if __name__ == "__main__":
    main()
