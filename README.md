
# Whisper AI - Automatic Subtitle Translator

### 🎯 Description
Whisper AI is an automatic subtitle generation tool designed to transcribe and translate non-English audio from video files into **English subtitles**. Leveraging **OpenAI's Whisper** model and **FFmpeg**, this tool excels in accuracy, even for complex speech patterns and low-quality audio. Ideal for movies, documentaries, and educational content, Whisper AI simplifies the subtitle generation process.

![Whisper AI Workflow](https://raw.githubusercontent.com/openai/whisper/main/images/whisper_workflow.png)

---

## 🚀 Project Overview
This project automates:
- Transcribing non-English audio from video files.
- Translating the transcribed text into **English subtitles**.
- Generating a `.srt` subtitle file for easy integration with video players.

---

## 📋 Available Models and Performance
Whisper offers multiple models optimized for different performance needs. Choose a model based on your desired speed and accuracy.

![Whisper Models](https://raw.githubusercontent.com/openai/whisper/main/images/whisper_models.png)

| Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|-------|-------------|--------------------|---------------------|----------------|-----------------|
| tiny   | 39M          | `tiny.en`           | `tiny`               | ~1 GB           | ~10x             |
| base   | 74M          | `base.en`           | `base`               | ~1 GB           | ~7x              |
| small  | 244M         | `small.en`          | `small`              | ~2 GB           | ~4x              |
| medium | 769M         | `medium.en`         | `medium`             | ~5 GB           | ~2x              |
| large  | 1550M        | N/A                 | `large`               | ~10 GB          | 1x                |
| turbo  | 809M         | N/A                 | `turbo`               | ~6 GB            | ~8x               |

---

## 🌍 Whisper Performance Across Languages
Whisper’s performance varies across languages. Below is a comparison of Word Error Rate (WER) across different languages:

![Whisper Language Performance](https://raw.githubusercontent.com/openai/whisper/main/images/whisper_language_performance.png)

---

## 📋 Requirements
- **Python 3.9+**
- **PyTorch** (with CUDA support for GPU acceleration)
- **OpenAI Whisper**
- **FFmpeg**

---

## ⚙️ Installation Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/tushar25012000/whisper-subtitles
cd whisper-subtitles
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # (On Windows use `.venv\Scripts\activate`)
```

### 3. Install Dependencies
```bash
pip install openai-whisper
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
winget install ffmpeg
```

---

## 📝 Usage
1. Place your movie file in the project folder.
2. Update the file path in `subtitles.py`.
3. Run the Script:

```bash
python subtitles.py
```

4. Add Subtitles to Your Movie
- In **VLC Media Player** → Go to **Subtitle → Add Subtitle File**.
- In **CapCut**, **DaVinci Resolve**, or **Premiere Pro** → Import the `.srt` file directly.

---

## ❗ Troubleshooting Guide
![Troubleshooting](https://raw.githubusercontent.com/openai/whisper/main/images/whisper_troubleshooting.png)

### **Error: `[WinError 2] The system cannot find the file specified`**
✅ Ensure FFmpeg is correctly installed and added to your system's PATH. 

### **Error: `FP16 is not supported on CPU; using FP32 instead`**
✅ This is a harmless warning. Whisper will automatically use FP32 for CPUs.

### **Slow Performance on CPU**
✅ Use GPU acceleration by installing PyTorch with CUDA.

---

## 🌟 Future Enhancements
- Add a GUI for better usability.
- Implement batch processing for multiple video files.

---

## 🙌 Credits
Developed with ❤️ using **OpenAI Whisper** and **FFmpeg**.

If you found this project helpful, please ⭐ the repository!

---

## 📫 Contact
For questions, feel free to raise an issue on [GitHub](https://github.com/tushar25012000/whisper-subtitles).
