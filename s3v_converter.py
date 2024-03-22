import os
import ffmpeg

def search_files():
    current_dir = os.getcwd()
    files = [file for file in os.listdir(current_dir) if file.endswith("s3p")]
    return files

def convert_files(files, start = 0, end = 0):
    for item in files:
        name = item[:-3] + "asf"
        print(name)
        with open(item, "rb") as file:
            data = file.read()
            try:
                offset = hex(data.index(b'\x30\x26'))
                print(offset)
            except ValueError:
                print("Couldn't find offset")
            converted_file = data[:start] + data[int(offset, 16):]
        with open(name, 'wb') as file:
            file.write(converted_file)

def to_wav():
    current_dir = os.getcwd()
    files = [file for file in os.listdir(current_dir) if file.endswith("asf")]

    for file in files:
        filename = file[:-3] + "wav" 
        ffmpeg.input(file).output(filename). run()
        os.remove(file)

def main():
    files = search_files()
    for element in files:
        print(element)
    convert_files(files)
    print("Do you want to convert to WAV?")
    answer = input("[Y/n]")
    if answer != "n":
        to_wav()

main()

