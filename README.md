# 🚀 Internet Speed Test — Python + CustomTkinter

This project is a modern, dark-themed **Internet Speed Test GUI application** built using  
**Python**, **CustomTkinter**, **Speedtest-CLI**, and **Pillow**.  
The application delivers real-time measurement of:

- 📥 Download Speed  
- 📤 Upload Speed  
- 🏓 Ping (Latency)  
- 🏢 ISP (Best Server Sponsor)

It is fully interactive, responsive, and user-friendly.


## 🧠 What the Code Does

### 🔹 1. Initializes CustomTkinter (Dark Mode)
The code sets:
- **Dark theme**
- **Blue accent color**
- **Window size, title, and icon**

This gives the GUI a clean, modern look.


### 🔹 2. Loads and Displays a Logo
Using **Pillow (PIL)**, the app loads a custom image, converts it into a  
`CTkImage`, and displays it at the top of the window.

If the image is missing, it safely prints an error instead of crashing.


### 🔹 3. Builds UI Layout
The UI contains:
- Title label  
- ISP label  
- Download speed label  
- Upload speed label  
- Ping label  
- "Test Speed" button  
- Footer text  

All components use modern fonts and spacing for a clean layout.


## ✨ Features

- 🌙 **Dark Mode UI** powered by CustomTkinter  
- 🚀 **Accurate Internet Speed Testing** (download, upload, ping)  
- 📡 **Fetches best server + ISP name automatically**  
- 🔄 **Threaded speed test** to avoid UI freezing  
- 🖼️ **Supports custom icons & images**  
- 👨‍💻 **Designed & Developed by Yaswanth**


## 🛠️ Tech Stack

| Technology               | Purpose                                |
|-------------------------|------------------------------------------|
| **Python**              | Core Programming Language                |
| **CustomTkinter**       | GUI Framework with modern dark theme     |
| **speedtest-cli**       | Internet speed measurement               |
| **Pillow (PIL)**        | Image loading & rendering                |
| **Threading**           | Run speed tests without blocking UI      |


## ⚙️ How the Speed Test Works (Code Explanation)

### 🔹 Step 1 — Button Press  
When the user clicks **Test Speed**, the UI:
- Shows “Testing… Please wait”
- Disables the button
- Starts a **separate thread** so the GUI doesn’t freeze


### 🔹 Step 2 — Speedtest Process  
Inside the thread:

1. Creates a `Speedtest()` object  
2. Fetches the **best server** → extracts the **ISP name**  
3. Measures:
   - Download speed (converted from bytes → Mbps)
   - Upload speed
   - Ping  
4. Updates all GUI labels with real-time results

If something goes wrong, it shows an error in red text.


### 🔹 Step 3 — UI Update  
After completing the measurements:

- The "Testing..." label turns green → **"Test Completed!"**
- The button becomes active again
- All speed values remain visible

📂 Internet-Speed-Test

 ├── main.py
 
 ├── 📂 assets
 
 │       ├── speed_logo.png
 
 │       └── n.ico 
 
 └── README.md


## 🧱 Code Structure

### Main libraries used:
```py
import speedtest
import customtkinter as ctk
from PIL import Image
import threading

```

## ▶️ Running the Application
```py
pip install speedtest-cli customtkinter pillow

python main.py
```

If you found this helpful, please ⭐ star the repository!




