# python-zhmh

## 进度条

```python
import time
from zhmh import RichPrint

length = 100
for i in range(1, 1 + length):
    RichPrint.progress_bar(i/length)
    time.sleep(0.05)
```