import antiVirus as antv
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

def Gui():
    API_KEY = "c999ad59968c728b1e3003b3a6f45d31a66f2c943bd6d0efb29378ba3fe76a7b"
    antivirus = antv.antiVirus(API_KEY)

    win = tk.Tk()
    win.title("AntiVirus GUI")
    win.geometry("600x400")

    selected_folder_path = tk.StringVar()

    def browse_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            selected_folder_path.set(folder_path)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"📂 Selected folder:\n{folder_path}\n")

    def scan_folder():
        folder_path = selected_folder_path.get()
        if not folder_path:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return

        def run_scan():
            result_text.insert(tk.END, "\n🔎 Starting scan...\n")
            win.update()

            try:
                for root, dirs, files in os.walk(folder_path):
                    result_text.insert(tk.END, f"\n📁 Scanning folder: {root}\n")
                    for file in files:
                        full_path = os.path.join(root, file)
                        result_text.insert(tk.END, f"🔍 Scanning file: {file}...\n")
                        win.update()

                        malicious, suspicious = antivirus.upload_file(full_path)

                        result_text.insert(tk.END, f"✅ Result for {file}:\n")
                        result_text.insert(tk.END, f"   - Malicious: {malicious}\n")
                        result_text.insert(tk.END, f"   - Suspicious: {suspicious}\n\n")
                        win.update()

                result_text.insert(tk.END, "✅ Scan complete.\n")

            except Exception as e:
                result_text.insert(tk.END, f"\n❌ Error: {e}\n")
                win.update()

        threading.Thread(target = run_scan).start()

    label = tk.Label(win, text = "Welcome to Yair's AntiVirus", font = ("Arial", 16))
    label.pack(pady=10)

    browse_button = tk.Button(win, text = "📂 Select Folder", command = browse_folder)
    browse_button.pack(pady = 5)

    scan_button = tk.Button(win, text = "🛡️ Scan Folder", command = scan_folder)
    scan_button.pack(pady = 5)

    result_text = tk.Text(win, height = 15, width = 75)
    result_text.pack(pady = 10)

    win.mainloop()

def main():
    Gui()

if __name__ == "__main__":
    main()
