import subprocess
import shlex

command = "ping www.baidu.com"
args = shlex.split(command)
print args
try:
    subprocess.check_call(['ping', 'www.baidu.com'])
    print("baidu web server is up")
except subprocess.CalledProcessError:
    print("Failed to go baidu")