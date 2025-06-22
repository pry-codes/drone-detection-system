import requests
import os

# Make sure models folder exists
os.makedirs("models", exist_ok=True)

# URL of the HuggingFace-hosted model file
MODEL_URL = "https://huggingface.co/spaces/abinashp01/drone-detection-ab/resolve/main/models/1_best.pt"
DEST_PATH = "models/best1.pt"

print(f"Downloading from {MODEL_URL}...")

resp = requests.get(MODEL_URL, stream=True)
if resp.status_code == 200:
    with open(DEST_PATH, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"✅ Model saved to {DEST_PATH}")
else:
    print(f"❌ Failed to download. Status code: {resp.status_code}")
