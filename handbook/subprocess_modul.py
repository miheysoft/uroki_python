import subprocess

process = subprocess.Popen(
    "ls", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
out_, err = process.communicate()
print(out_.decode("utf-8"))
print(err.decode("utf-8"))
print(process.wait())
print(process.returncode)
print(process.poll())
