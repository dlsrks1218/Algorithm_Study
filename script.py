# <포지션> DevOps System Engineer

# [자격 및 우대사항]
# 1) GIT 중급 이상
# 2) Docker 중급 이상
# 3) Linux Shell, Python Script 중급 이상
# 4) Jenkins 혹은 다른 CI/CD 사용 및 운영 경험
# 5) Linux 와 network 관련 지식
# 6) 사원 ~ 선임급

# [직무 설명]
# - FW 팀내 DevOps 운영 및 Infrastructure 관리

# from subprocess import call
import subprocess

subprocess.call('ls')

# time = subprocess.Popen('date', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = time.communicate()

time = subprocess.check_output('date')

print('IT is', time)