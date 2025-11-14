import speedtest
import customtkinter as ctk
from PIL import Image
import threading

# CustomTkinter Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Function to Test Speed
def check_speed():
    loading_label.configure(text="Testing... Please wait", text_color="yellow")
    test_button.configure(state="disabled")

    def run_speedtest():
        try:
            st = speedtest.Speedtest()
            best_server = st.get_best_server()
            isp_name = best_server['sponsor']

            download_speed = round(st.download() / 1_000_000, 2)
            upload_speed = round(st.upload() / 1_000_000, 2)
            ping_speed = round(st.results.ping, 2)

            isp_label.configure(text=f"ISP: {isp_name}")
            download_label.configure(text=f"Download: {download_speed} Mbps")
            upload_label.configure(text=f"Upload: {upload_speed} Mbps")
            ping_label.configure(text=f"Ping: {ping_speed} ms")

            loading_label.configure(text="Test Completed!", text_color="green")

        except Exception as e:
            loading_label.configure(text=f"Error: {str(e)}", text_color="red")

        finally:
            test_button.configure(state="normal")

    threading.Thread(target=run_speedtest).start()

# GUI Setup
app = ctk.CTk()
app.iconbitmap("assets/n.ico")
app.geometry("400x500")
app.title("Internet Speed Test")
# Load Logo Image
try:
    logo = ctk.CTkImage(light_image=Image.open("assets/speed_logo.png"), size=(80, 80))
    logo_label = ctk.CTkLabel(app, image=logo, text="")
    logo_label.pack(pady=10)
except Exception as e:
    print(f"Logo image could not be loaded: {e}")

# Title
title_label = ctk.CTkLabel(app, text="Internet Speed Test", font=("Arial", 20, "bold"))
title_label.pack()

# Loading Label
loading_label = ctk.CTkLabel(app, text="", font=("Arial", 14, "italic"))
loading_label.pack(pady=5)

# ISP Label
isp_label = ctk.CTkLabel(app, text="   ISP: -", font=("Arial", 16))
isp_label.pack(pady=5)

# Speed Result Labels
download_label = ctk.CTkLabel(app, text="Download: - Mbps", font=("Arial", 16))
download_label.pack(pady=5)

upload_label = ctk.CTkLabel(app, text="Upload: - Mbps", font=("Arial", 16))
upload_label.pack(pady=5)

ping_label = ctk.CTkLabel(app, text="Ping: - ms", font=("Arial", 16))
ping_label.pack(pady=5)

# Test Button
test_button = ctk.CTkButton(app, text="Test Speed", command=check_speed, font=("Arial", 16))
test_button.pack(pady=20)

# Footer
footer_label = ctk.CTkLabel(app, text="Developed by Yaswanth", font=("Arial", 12, "italic"))
footer_label.pack(pady=10)

app.mainloop()
