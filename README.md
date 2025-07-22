# 🤖 Hand_Tracker_Demo

A gesture-based hand tracking **demo** application built using **OpenCV** and **MediaPipe**. This tool allows you to interact with your display through finger gestures, and can be calibrated to any screen size or orientation.

---

## 🛠 Features

- 🖐️ Real-time hand gesture recognition  
- 🎯 Custom display calibration  
- 🖼️ GUI interaction with draggable Godot robot logo  
- 📷 External camera support for optimal tracking  

---

## 📏 How to Calibrate

Before using the application, follow these steps to calibrate the display:

1. **Use an external camera** and position it so it's facing your monitor/screen.
2. Run the application and press the **`c`** key on your keyboard.
3. Point your finger at the following positions on your screen when prompted:
    - 🟢 **Top-Left corner**
    - 🔵 **Top-Right corner**
    - 🟡 **Bottom-Left corner**
    - 🔴 **Bottom-Right corner**
4. Once calibration is complete, the GUI will appear with a **Godot robot logo** that you can **pinch and move** using hand gestures.

---

## 📦 Dependencies

Make sure you have the following installed:

- [Python 3.10 or lower](https://www.python.org/downloads/) (required for MediaPipe compatibility)
- [`opencv-python`](https://pypi.org/project/opencv-python/)
- [`mediapipe`](https://pypi.org/project/mediapipe/)
- Built-in [`tkinter`](https://docs.python.org/3/library/tkinter.html) for GUI

Install the dependencies using:

```bash
pip install opencv-python mediapipe
