from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont
from ping3 import ping
import threading
import time


class PingTrayIcon:
    def __init__(self):
        self.icon = Icon("Ping Monitor")
        self.icon.icon = self.create_icon("N/A")
        self.icon.menu = Menu(
            MenuItem("Quit", self.quit)
        )
        self.running = True
        self.ping_value = "N/A"

    def create_icon(self, text):
        img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))  
        draw = ImageDraw.Draw(img)

        font_size = 50
        font = ImageFont.truetype("arial.ttf", font_size)

        text_bbox = draw.textbbox((0, 0), text, font=font) 
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        x = (img.width - text_width) // 2
        y = (img.height - text_height) // 2

        draw.text((x, y), text, fill="white", font=font)
        return img

    def update_ping(self):
        while self.running:
            try:
                latency = ping("8.8.8.8", timeout=1)
                self.ping_value = f"{round(latency * 1000):d}" if latency else "TO"  # "TO" pour Timeout
            except Exception:
                self.ping_value = "ERR"

            self.icon.icon = self.create_icon(self.ping_value)
            time.sleep(1) 
    def quit(self):
        self.running = False
        self.icon.stop()

    def run(self):
        thread = threading.Thread(target=self.update_ping, daemon=True)
        thread.start()
        self.icon.run()


if __name__ == "__main__":
    tray = PingTrayIcon()
    tray.run()
