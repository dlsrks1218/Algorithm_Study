# from subprocess import call
import subprocess

subprocess.call('ls')

# time = subprocess.Popen('date', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = time.communicate()

time = subprocess.check_output('date')

print('IT is', time)