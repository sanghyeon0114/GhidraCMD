# projects 폴더 만들기
import requests
import os
import subprocess

print("[*] check ghidra")

if os.path.exists('./ghidra'):
    check_ghidra = os.listdir('./ghidra')
    if len(check_ghidra) > 0:
        print("already exist.")
        exit(0)

########################################################################

print("[*] load ghidra")

api_url = "https://api.github.com/repos/NationalSecurityAgency/ghidra/releases/latest"
response = requests.get(api_url)
response.raise_for_status()
release_data = response.json()

zip_url = next(asset["browser_download_url"] for asset in release_data["assets"] if asset["name"].endswith(".zip"))

zip_response = requests.get(zip_url, stream=True)
zip_response.raise_for_status()

########################################################################

print("[*] download latest released ghidra")

# download file
zip_path = './ghidra_latest.zip'
with open(zip_path, "wb") as f:
    for chunk in zip_response.iter_content(chunk_size=8192):
        f.write(chunk)

########################################################################

print("[*] unzip ghidra_latest.zip")

extract_path = './ghidra'
command = f"unzip {zip_path} -d {extract_path}"
subprocess.run(command, shell=True, check=True)

########################################################################

# remove zip file 
if os.path.exists(zip_path):
    os.remove(zip_path)

# mkdir projects
projects_path = './projects'
if not os.path.exists(projects_path):
    os.mkdir(projects_path)

# mkdir logs
log_paths = './logs'
if not os.path.exists(log_paths):
    os.mkdir(log_paths)

print("[*] finished.")