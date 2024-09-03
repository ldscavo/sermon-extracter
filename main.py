import sys
import ffmpeg
import time
import os
from datetime import timedelta, date

def main():
    print("Starting up...")    
    search_directory = get_directory_from_params()

    print(f"Looking for mp4 files in {search_directory}")

    while True:
        files = get_mp4_files(search_directory)

        if len(files) == 0:
            print("No mp4 files found in directory")

        else:
            print(f"Found {len(files)} mp4 files")

            for file in files:
                convert_mp4_to_mp3(file)
                os.remove(file)

                print("Processed {file}")
            
            print("Finished processing all files")

        next_date = date.today() + timedelta(days=7)
        print(f"Next check at {next_date}")

        time.sleep(60 * 60 * 24 * 7) # Check again in a week


def get_mp4_files(search_directory):
    return [
        os.path.join(search_directory, file)
        for file in os.listdir(search_directory)
        if (os.path.splitext(file)[1] == ".mp4")
    ]

def get_directory_from_params():
    if len(sys.argv) == 1:
        print("FAILURE: Missing `search_directory` parameter")
        sys.exit()

    return sys.argv[1]

def convert_mp4_to_mp3(filename):
    print(f"Processing {filename}")
    (
        ffmpeg
        .input(filename)
        .output(os.path.splitext(filename)[0] + ".mp3", loglevel="quiet")
        .run()
    )

main()