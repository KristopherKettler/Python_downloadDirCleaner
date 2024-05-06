import os
import shutil

def sort_downloads():
    # Pfad zum Download-Ordner unter Windows
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Ordner erstellen, um Dateien nach Dateiformat zu sortieren
    def create_folders(file_formats):
        for format in file_formats:
            folder_path = os.path.join(download_folder, format)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    # Dateien im Download-Ordner auflisten und Dateiformate sammeln
    def list_files():
        file_formats = set()
        files = os.listdir(download_folder)
        for file in files:
            if os.path.isfile(os.path.join(download_folder, file)):
                _, file_extension = os.path.splitext(file)
                file_formats.add(file_extension[1:].lower())  # Remove the dot from extension and convert to lowercase
        return file_formats

    # Dateien nach Dateiformat sortieren und verschieben
    def move_files(file_formats):
        for format in file_formats:
            format_folder = os.path.join(download_folder, format)
            for file in os.listdir(download_folder):
                if file.lower().endswith("." + format):
                    file_path = os.path.join(download_folder, file)
                    shutil.move(file_path, format_folder)

    # Hauptfunktion
    def main():
        file_formats = list_files()
        create_folders(file_formats)
        move_files(file_formats)
        print("Dateien wurden erfolgreich sortiert.")

    if __name__ == "__main__":
        main()

sort_downloads()
