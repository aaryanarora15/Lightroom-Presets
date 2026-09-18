Lightroom Preset Generator

A Python tool that extracts color-grading settings from video tutorials (e.g. Instagram Reels) and turns them into ready-to-use Lightroom presets (.xmp).

Features
Pulls frames from a tutorial video using ffmpeg
Uses OCR to read on-screen slider values (exposure, contrast, HSL, etc.) shown in editing tutorials
Converts extracted settings into Lightroom-compatible .xmp preset files
Supports batch processing of multiple videos/tutorials at once
Requirements
Python 3.8+
ffmpeg installed and on your PATH
Tesseract OCR (or your OCR engine of choice) installed
Setup
Clone the repo and install requirements:
bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   pip install -r requirements.txt
Make sure ffmpeg and Tesseract are installed:
bash
   # macOS
   brew install ffmpeg tesseract

   # Ubuntu/Debian
   sudo apt install ffmpeg tesseract-ocr
Usage
bash
python generate_preset.py --video tutorial.mp4 --name "Obsession"

This will:

Extract frames from tutorial.mp4 where slider values are visible
OCR the values off each frame
Write out Obsession.xmp — ready to import into Lightroom
Importing into Lightroom
Open Lightroom (mobile or desktop)
Go to Presets → Import
Select the generated .xmp file
Note

OCR accuracy depends on video quality and how clearly the tutorial shows slider values — double-check the generated preset against the original before relying on it.
