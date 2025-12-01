# YOLO Pose – Project Progress Log

**Environment:** Conda (`yolovenv`), Ultralytics YOLOv11 Pose  
**Repository:** [https://github.com/malaka4u/bodypose_env](https://github.com/malaka4u/bodypose_env)

---

 🗓️ Week Summary

**Week:** 24–30 Nov 2025]  
**Focus:** Refining body part labeling accuracy and dataset structure.

###  Tasks Completed
- Implemented YOLO Pose **v3.4b** with:
  - Dynamic scaling for human size variation.
  - Left/right body part separation.
  - Optional segmentation overlay.
- Cleaned environment → created new **Conda env (`yolovenv`)**.
- Uploaded **clean repo** with only key files (`ultralytics.ipynb`, `.gitignore`, `README.md`).
- Tested 10+ images with good results on:
  - Head, torso, and arms detection.
  - Left/right limbs identified separately.

###  Observations
- Bounding boxes sometimes overlap around torso and legs.
- Shoes occasionally detected around ankles, not full feet.
- Model performs better in brighter and full-body images.
- Segmentation (YOLO-Seg) could improve boundary precision.

###  Next Steps
- Tune box expansion values for `torso` and `legs`.
- Experiment with **YOLO11n-seg.pt** for segmentation-based accuracy.
- Begin labeling small dataset manually for fine-tuning later.
- Test repository setup on **Unitec GPU computer (Ubuntu)**.

###  Commands Used (Key Setup)
```bash
# Create and activate Conda env
conda create -n yolovenv python=3.10 -y
conda activate yolovenv

# Install dependencies
pip install ultralytics opencv-python matplotlib

# Run notebook
jupyter notebook ultralytics.ipynb
