import os

def get_file(folder):
    files = os.listdir(folder)
    files = [file for file in files if os.path.isfile(os.path.join(folder, file))]
    if len(files) == 0:
        raise AssertionError(f"В папке {folder} нет файлов")
    if len(files) > 1:
        raise AssertionError(f'В папке {folder} больше одного файла')
    print(f'Найден файл {files[0]}')
    return f'./{folder}/{files[0]}'

def clean_output(folder):
    files = os.listdir(folder)
    for file in files:
        fullpath = os.path.join(folder, file)
        if os.path.isfile(fullpath):
            os.remove(fullpath)
            print(f"Файл удален: {fullpath}")

def check_folders(*folders):
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)