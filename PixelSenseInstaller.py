import os
import sys
import hashlib
import urllib.request

URL = "https://dn710102.ca.archive.org/0/items/win-7-pro-64-sur-40/Win7Pro64_SUR40.iso"
SAVE_PATH = "PixelSense.iso"

def download_file(url, save_path):
    print(f"Downloading {url} -> {save_path}")
    urllib.request.urlretrieve(url, save_path)
    print("Download complete")

def verify_sha256(path, expected_hash):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    actual = h.hexdigest()
    print(f"SHA256: {actual}")
    if expected_hash and actual.lower() != expected_hash.lower():
        print("WARNING: checksum mismatch")
        return False
    return True

if __name__ == "__main__":
    os.makedirs(os.path.dirname(SAVE_PATH) or ".", exist_ok=True)
    download_file(URL, SAVE_PATH)
    print(f"ISO saved to: {os.path.abspath(SAVE_PATH)}")
