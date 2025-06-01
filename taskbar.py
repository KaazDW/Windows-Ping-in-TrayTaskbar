from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont
from ping3 import ping
import threading
import sys
import webbrowser  # Ajouté pour ouvrir GitHub

class PingTrayIcon:
    def __init__(self):
        self.icon = Icon("Ping Monitor")
        self.icon.icon = self.create_icon("N/A")
        self.icon.menu = Menu(
            MenuItem("Open Github", self.open_github),
            MenuItem("Quit", self.quit)
        )
        self.stop_event = threading.Event()
        self.ping_value = "N/A"

    def create_icon(self, text):
        img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 50)
        except IOError:
            font = ImageFont.load_default()

        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2

        draw.text((x, y), text, fill="white", font=font)
        return img

    def update_ping(self):
        previous_value = None
        timeout_count = 0
        TIMEOUT_THRESHOLD = 2
        last_latency = None
        while not self.stop_event.is_set():
            try:
                latency = ping("8.8.8.8", timeout=1)
                if latency:
                    timeout_count = 0
                    last_latency = f"{round(latency * 1000):d}"
                    new_value = last_latency
                else:
                    timeout_count += 1
                    if timeout_count >= TIMEOUT_THRESHOLD:
                        new_value = "TO"
                    else:
                        new_value = last_latency if last_latency else "N/A"
            except Exception as e:
                print(f"Erreur lors du ping: {e}", file=sys.stderr)
                new_value = "ERR"

            if new_value != previous_value:
                self.ping_value = new_value
                self.icon.icon = self.create_icon(self.ping_value)
                self.icon.title = (
                    f"Ping: {self.ping_value} ms" if new_value not in ["TO", "ERR"] else "Ping: Timeout/Error"
                )
                previous_value = new_value

            self.stop_event.wait(1)

    def open_github(self, icon, item):
        webbrowser.open("https://github.com/KaazDW/Windows-Ping-Taskbar-Widget")

    def quit(self, icon=None, item=None):
        self.stop_event.set()
        self.icon.stop()

    def run(self):
        thread = threading.Thread(target=self.update_ping, daemon=True)
        thread.start()
        self.icon.run()


if __name__ == "__main__":
    tray = PingTrayIcon()
    tray.run()