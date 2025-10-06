from playsound import playsound

# MacOSmust pip install playsound==1.2.2 PyObjC
# Windows should just need to pip install playsound

# A .wav file is a file that contains audio data
WAV_FILE_PATH = "piano-minuet.wav"

def main():
    print("Playing piano...")
    playsound(WAV_FILE_PATH)

    print("Done playing!")

if __name__ == "__main__":
    main()