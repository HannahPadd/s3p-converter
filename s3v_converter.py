import os
import ffmpeg

current_dir = os.getcwd()

def search_files():
    global current_dir
    files = [file for file in os.listdir(current_dir + "/in") if file.endswith("s3p")]
    return files

def convert_files(files, start = 0, end = 0):
    global current_dir
    for item in files:
        name = item[:-3] + "asf"
        print(name)
        with open(current_dir + "/in/" + item, "rb") as file:
            data = file.read()
            try:
                offset = hex(data.index(b'\x30\x26'))
                print(offset)
            except ValueError:
                print("Couldn't find offset")
            converted_file = data[:start] + data[int(offset, 16):]
        with open(current_dir +  "/out/" + name, 'wb') as file:
            file.write(converted_file)

def to_wav():
    global current_dir
    files = [file for file in os.listdir(current_dir + "/out") if file.endswith("asf")]

    for file in files:
        filename = file[:-3] + "wav" 
        ffmpeg.input(current_dir + "/out/" + file).output(current_dir + "/out/" + filename).run()
        os.remove(current_dir + "/out/" + file)

def main():
    files = search_files()
    for element in files:
        print(element)
    convert_files(files)
    print("Do you want to convert to WAV?")
    answer = input("[Y/n]\n")
    if answer != "n":
        to_wav()

main()

