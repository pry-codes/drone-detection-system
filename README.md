# 🛰️ Drone Detection Dashboard

This project is a Flask-based web application designed to detect drones in uploaded videos or images using a custom-trained YOLOv8 model. Users can upload footage through the dashboard, after which the app automatically extracts frames, performs drone detection, and visually annotates the results. The interface uses a modern dark theme and supports both image and video processing.

---

## 🚀 Features

The dashboard includes the following main features:

* 📤 Upload support for both video files (such as `.mp4`, `.avi`) and image files (such as `.jpg`, `.png`)
* 🎞️ Automatic frame extraction from uploaded videos
* 🎯 Drone detection using a custom-trained YOLOv8 model
* 🖼️ Annotated frames showing bounding boxes around detected drones
* 📊 Detection summary showing how many frames had drone detections
* 🔍 Click-to-view previews for both original and annotated frames
* 🖥️ Clean, responsive, dark-themed UI

---

## 🛠️ Tech Stack

**🔧 Backend Technologies:**

The backend is powered by Flask and a YOLOv8-based detection pipeline:

* 🧪 Flask – for routing, uploads, and backend logic
* 🤖 YOLOv8 (via Ultralytics) – to load and apply the custom-trained model
* 🔥 PyTorch – the deep learning engine behind YOLOv8
* 👁️ OpenCV – used to draw detection bounding boxes on images
* 🐍 Python libraries – such as `imageio` (frame extraction), `Pillow` (image handling), `requests` (model download), and standard modules like `os`, `uuid`, etc.

**🎨 Frontend Technologies:**

The frontend is built with:

* 🧱 HTML5 and 🎨 CSS3 – for the structure and styling of the dashboard
* ⚡ JavaScript – uses the Fetch API for dynamic server communication

---

## 📁 Project Structure

Here is the folder structure of the project:

video\_frame\_extractor
├── `app.py` — the Flask backend
├── `detector.py` — contains YOLOv8 object detection logic
├── `downloadCustomModel.py` — script to download the YOLO model
├── `models/` — contains the YOLOv8 model (`2_best.pt`)
├── `static/`
│   ├── `uploads/` — for uploaded media
│   ├── `frames/` — stores extracted frames
│   ├── `annotated_frames/` — stores detection results
│   ├── `css/` — contains `style.css`
│   └── `js/` — contains `script.js`
├── `templates/`
│   └── `index.html` — the main dashboard UI
├── `requirements.txt` — Python dependencies
├── `LICENSE` — MIT License file
└── `README.md` — this documentation

---

## ⚙️ Setup Instructions

1. 🧩 Clone the repository:
   `git clone https://github.com/your-username/video_frame_extractor.git`

2. 📁 Navigate into the project folder:
   `cd video_frame_extractor`

3. 📦 Install dependencies:
   `pip install -r requirements.txt`

4. ⬇️ Download the model (if not already present):
   `python downloadCustomModel.py`

5. 🛠️ Run the Flask app:
   `python app.py`

6. 🌐 Open your browser and visit:
   `http://127.0.0.1:5000`

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
