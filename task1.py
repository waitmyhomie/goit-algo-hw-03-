import os
import shutil
import argparse

#RUN WITH THIS COMMAND python task1.py ./task1in/ ./task1out/

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до цільової директорії (за замовчуванням 'dist')")
    return parser.parse_args()

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy_and_sort_files(src, dest):
    try:
        for root, _, files in os.walk(src):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[-1].lstrip(".").lower()

                if not file_extension:
                    file_extension = "others"

                dest_folder = os.path.join(dest, file_extension)
                create_directory(dest_folder)

                dest_file_path = os.path.join(dest_folder, file)
                shutil.copy2(file_path, dest_file_path)

    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    try:
        args = parse_arguments()
        source_directory = os.path.abspath(args.src)
        destination_directory = os.path.abspath(args.dest)

        if not os.path.exists(source_directory):
            print(f"Помилка: Вихідна директорія '{source_directory}' не знайдена.")
            exit(1)

        create_directory(destination_directory)
        copy_and_sort_files(source_directory, destination_directory)
        print(f"Файли успішно скопійовано та відсортовано у директорії '{destination_directory}'.")
    except SystemExit:
        print("Помилка: необхідно вказати шлях до вихідної директорії (src) як обов'язковий аргумент.")