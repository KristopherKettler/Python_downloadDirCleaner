import os
import shutil

def sort_downloads():
    # download directory path for windows
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # creating directories for each file format
    def create_folders(file_formats):
        for format in file_formats:
            folder_path = os.path.join(download_folder, format)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    # list files and file formats
    def list_files():
        file_formats = set()
        files = os.listdir(download_folder)
        for file in files:
            if os.path.isfile(os.path.join(download_folder, file)):
                _, file_extension = os.path.splitext(file)
                file_formats.add(file_extension[1:].lower())  # Remove the dot from extension and convert to lowercase
        return file_formats

    # sort files by file format and moves them to the appropriate folder
    def move_files(file_formats):
        for format in file_formats:
            format_folder = os.path.join(download_folder, format)
            for file in os.listdir(download_folder):
                if file.lower().endswith("." + format):
                    file_path = os.path.join(download_folder, file)
                    shutil.move(file_path, format_folder)

    def main():
        file_formats = list_files()
        create_folders(file_formats)
        move_files(file_formats)
        print("Dateien wurden erfolgreich sortiert.")

    if __name__ == "__main__":
        main()

sort_downloads()
