import time
from zhmh import RichPrint


for i in range(10):
    RichPrint.progress_bar((i + 1) / 10, 64)
    time.sleep(1)
