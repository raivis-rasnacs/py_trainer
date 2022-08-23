from time import sleep
import webbrowser
import ctypes


def pop(msg1, msg2):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, msg1, msg2, 0x40000)


options = [
        "https://www.youtube.com/watch?v=hbDAjCEvPWQ",
        "https://www.youtube.com/watch?v=OWMuziAvBSc",
        "https://www.youtube.com/watch?v=uGlgTplAKJA"
        ]

s = 0
while True:
    if s == 3540:
        pop("Be ready!", "Workout soon!")
    if s == 3600:
        file = open("counter.txt", "r")
        counter = int(file.read(1))
        file.close()
        webbrowser.open(options[counter], new=1)
        counter += 1
        if counter >= len(options):
            counter = 0
        file = open("counter.txt", "w")
        file.write(str(counter))
        file.close()
        s = 0
    s += 1
    sleep(1)
