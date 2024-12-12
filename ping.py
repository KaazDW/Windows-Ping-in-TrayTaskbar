import tkinter as tk
import psutil
import time
from ping3 import ping

class NetworkMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)    
        self.root.attributes('-topmost', True)  
        self.root.attributes('-alpha', 0.9)  
        self.root.geometry("150x70+10+10")  
        self.root.configure(bg="black")

        self.label = tk.Label(
            self.root, text="", font=("Arial", 9), bg="black", fg="white", justify="left"
        )
        self.label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.do_move)

        self.running = True
        self.update_data()
        self.keep_on_top()

    def get_network_speed(self):
        try:
            old_stats = psutil.net_io_counters()
            time.sleep(1)  
            new_stats = psutil.net_io_counters()

            download_speed = (new_stats.bytes_recv - old_stats.bytes_recv) / 1024  # KB/s
            upload_speed = (new_stats.bytes_sent - old_stats.bytes_sent) / 1024  # KB/s

            return round(download_speed, 1), round(upload_speed, 1)
        except Exception:
            return "N/A", "N/A"

    def get_ping(self):
        try:
            latency = ping("8.8.8.8", timeout=1)
            return round(latency * 1000, 1) if latency else "Timeout"
        except Exception:
            return "Error"

    def update_data(self):
        if self.running:
            download_speed, upload_speed = self.get_network_speed()
            ping_ms = self.get_ping()

            text = (
                f"DL: {download_speed} KB/s\n"
                f"UL: {upload_speed} KB/s\n"
                f"Ping: {ping_ms} ms"
            )
            self.label.config(text=text)

            self.root.after(1000, self.update_data)

    def keep_on_top(self):
        self.root.attributes('-topmost', True)
        self.root.after(500, self.keep_on_top)  

    def start_move(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def do_move(self, event):
        x = self.root.winfo_x() + event.x - self._drag_start_x
        y = self.root.winfo_y() + event.y - self._drag_start_y
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.run()
