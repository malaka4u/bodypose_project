import os, requests
from pycocotools.coco import COCO
from tqdm import tqdm

# === CONFIG ===
OUT_DIR = "person_images"
os.makedirs(OUT_DIR, exist_ok=True)

# Choose which set: 'train2017' or 'val2017'
SPLIT = "train2017"
COCO_ANN_FILE = f"annotations/instances_{SPLIT}.json"
COCO_IMG_URL = f"http://images.cocodataset.org/{SPLIT}/"

# === LOAD COCO ===
coco = COCO(COCO_ANN_FILE)
person_cat_id = coco.getCatIds(catNms=["person"])[0]
img_ids = coco.getImgIds(catIds=[person_cat_id])

print(f"Found {len(img_ids)} person images in {SPLIT}")

# === DOWNLOAD PERSON IMAGES ONLY ===
for img_id in tqdm(img_ids, desc="Downloading person images"):
    img_info = coco.loadImgs(img_id)[0]
    file_name = img_info["file_name"]
    url = f"{COCO_IMG_URL}{file_name}"
    save_path = os.path.join(OUT_DIR, file_name)
    if not os.path.exists(save_path):
        try:
            img_data = requests.get(url, timeout=10).content
            with open(save_path, "wb") as f:
                f.write(img_data)
        except Exception as e:
            print(f"Failed: {file_name} - {e}")

print("✅ Done! All 'person' images saved to:", OUT_DIR)
