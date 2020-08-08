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

## 下载

```python
from zhmh import download_one_file
download_one_file('./521.jpg', {
    'url': "https://dss1.bdstatic.com/kvoZeXSm1A5BphGlnYG/skin_zoom/521.jpg?2"
})
```

