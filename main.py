# Libraries
from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT
from time import sleep, time
from simpleaudio import WaveObject
from sys import stdout

frameWait = 1/30

# Setup
video = VideoCapture("BadApple.mp4")
audio = WaveObject.from_wave_file("BadApple.wav")
success, frame = video.read()

input("Press enter to start pre-rendering.")

frames = []
string = [""] * ((150 + 1) * 60 + 1)

# Percentage
frameCount = 0
precentFactor = int(video.get(CAP_PROP_FRAME_COUNT))/100

print("\n"*100)

# While there is a frame to be rendered
while success:
    # For every row
    for row in range(60):
        rowArray = frame[row]
        # For every coloumn
        for coloumn in range(150):
            pixel = rowArray[coloumn]
            if pixel[0] < 50:
                string[(row*151)+coloumn] = " "
            else:
                string[(row*151)+coloumn] = "#"
        string[(row*151)+150] = "\n"
    frames.append("\x1b[1;37;40m" + "".join(string) + "\x1b[0m")

    # Prepare the next frame
    success, frame = video.read()

    frameCount += 1
    print("\r" + (" " * 50) + "\r" + str(round(frameCount/precentFactor, 1)) + "% rendered. ", end = "")

video.release()

# Starting prompt
print("\nThis should be visible!")
print("\n"*58)
input("Resize the window until the text above is the first line visible. Press enter when ready.")

audio.play()

frameCount = 0
startTime = time()

for stringFrame in frames:
    stdout.write(stringFrame)

    frameCount += 1

    # Wait for the next frame
    waitTime = (startTime + frameWait * frameCount) - time()
    if(waitTime > 0): sleep(waitTime)
