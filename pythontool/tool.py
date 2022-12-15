import subprocess
import pyfiglet

text = pyfiglet.figlet_format("Website ping")
print(text)
print("Enter An Ip or Website name")
i = input()
subprocess.call("ping "+ i ,shell=True)