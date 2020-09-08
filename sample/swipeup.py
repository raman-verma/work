import subprocess

while True:
    subprocess.call("adb shell input swipe 300 300 500 2000",shell=True)
    