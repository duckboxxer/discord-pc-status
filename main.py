import psutil
import time
import platform
from pypresence import Presence

ID = "ここにAPP ID" ## わからなければ "1357893255655591952"
RPC = Presence(ID)
RPC.connect()

mem = psutil.virtual_memory()
os = platform.system()  
machine = platform.machine()  
cpu = psutil.cpu_times()
mem_used = round(mem.used / (1024 ** 3), 2)
mem_total = round(mem.total / (1024 ** 3), 2)

while True:
    # RPC
    RPC.update(
        state = f"{os} | {machine}",
        details = f"RAM | {mem_used}/{mem_total}",
        large_image = "pc",
        large_text = ".."
    )
time.sleep(10)
