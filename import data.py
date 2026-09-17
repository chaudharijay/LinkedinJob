import kagglehub, shutil, os

path = kagglehub.dataset_download("arshkon/linkedin-job-postings")
print("Downloaded to:", path)

os.makedirs("data/raw", exist_ok=True)
for f in os.listdir(path):
    src = os.path.join(path, f)
    dst = os.path.join("data/raw", f)
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy(src, dst)

print(os.listdir("data/raw"))