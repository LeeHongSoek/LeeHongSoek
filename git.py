import subprocess
import time
import os


# 로컬 저장소의 경로
local_repo = r"C:\MyProject\LeeHongSoek"

# 원격 저장소의 URL
remote_url = "https://github.com/LeeHongSoek/LeeHongSoek.git"

# 로컬 저장소로 이동합니다.
os.chdir(local_repo)

# 원격 저장소를 추가합니다.
subprocess.call(["git", "remote", "add", "origin", remote_url])

while True:
    # 원격 저장소의 변경 사항을 가져옵니다.
    subprocess.run(["git", "pull", "origin", "main"])

    # git add --all
    subprocess.run(["git", "add", "-u"])

    # git status
    result = subprocess.run(["git", "status"], capture_output=True, text=True)

    # 변경된 파일의 수
    num_files = len(result.stdout.splitlines()) - 1

    # 변경된 파일이 있는 경우 커밋하고 푸시합니다.
    if num_files > 0:
        subprocess.run(["git", "commit", "-m", "Auto-commit"])
        subprocess.run(["git", "push", "origin/main"])

    # 10초 동안 대기합니다.
    time.sleep(10)
