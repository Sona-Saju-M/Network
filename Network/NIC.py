import subprocess
import psutil
cmd = "ipconfig"
a = subprocess.Popen(cmd, shell=True)
b = a.wait()
m = psutil.virtual_memory()
print("Memory:")
print(m)

with open('version.txt', 'r') as file:
    contents = file.read()
    print("Current version:")
    print(contents)
with open('version.txt', 'r') as file:
    file_data = file.read()
    print("Updated version is:")
    file_data = file_data.replace('1.1', '1.2')
with open('version.txt', 'w') as file:
    file.write(file_data)
with open('version.txt') as file:
    contents = file.read()
    print(contents)
