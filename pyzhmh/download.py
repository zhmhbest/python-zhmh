import os
import requests
import zipfile
from hashlib import sha256
from .rich import RichPrint

__USER_AGENT = ' '.join([
    "Mozilla/5.0", "(Windows NT 10.0; Win64; x64)",
    "AppleWebKit/537.36", "(KHTML, like Gecko)",
    "Chrome/84.0.4147.105", "Safari/537.36"
])


def __hash_hexdigest(data):
    # return md5(data).hexdigest()
    return sha256(data).hexdigest()


def __check_hash(check_filename, hash_filename) -> bool:
    if os.path.exists(check_filename) and os.path.exists(hash_filename):
        with open(check_filename, 'rb') as fp:
            hexdigest_real = __hash_hexdigest(fp.read())
        with open(hash_filename, 'r') as fp:
            hexdigest_test = fp.read()
        return hexdigest_real == hexdigest_test
    return False


def __fix_options(options: dict) -> bool:
    if 'url' not in options:
        print("'options' must have the key 'url'.")
        return False
    # 请求方式
    if 'method' not in options:
        options['method'] = 'GET'
    else:
        options['method'] = options['method'].upper()
    # 请求头
    if 'headers' not in options:
        options['headers'] = {
            'User-Agent': __USER_AGENT
        }
    elif 'User-Agent' not in options['headers']:
        options['headers']['User-Agent'] = __USER_AGENT
    # GET使用请求行
    if 'data' in options and 'GET' == options['method']:
        options['params'] = options['data']
        del options['data']
    # POST使用请求体
    if 'params' in options and 'POST' == options['method']:
        options['data'] = options['params']
        del options['params']
    return True


def download_one_file(
        local: str,
        request_options: dict,
        chunk_size: int = 32 * 1024
):
    """
    下载文件
    :param local:
    :param request_options: {
        url: str
        data: Dict
        headers: Dict
        cookies: Dict or CookieJar
    }
    :param chunk_size:
    :return:
    """
    if __check_hash(local, f'{local}.ok'):
        return True  # 文件存在且校验通过（已下载）
    if not __fix_options(request_options):
        return False  # 参数错误

    # 检查断点
    if os.path.exists(f'{local}.lock'):
        with open(f'{local}.lock', 'rb') as fp:
            content = [
                int.from_bytes(bytes=fp.read(8), byteorder='little'),
                int.from_bytes(bytes=fp.read(8), byteorder='little')
            ]
        request_options['headers']['Range'] = f'bytes={content[0]}-'

    # 请求数据
    res = requests.request(**request_options, stream=True)
    headers = res.headers

    # 是否成功
    if 200 == res.status_code:
        # 首次
        remain_length = int(headers['Content-Length'])
        content_length = remain_length
        current_length = 0
        open_lock_mode = 'wb+'
    elif 206 == res.status_code:
        # 续传
        remain_length = int(headers['Content-Length'])
        content_length = int(content[1])
        current_length = int(content[0])
        # print(remain_length, content_length - current_length)
        open_lock_mode = 'rb+'
    else:
        print(res.status_code, 'Download failed.')
        # for item in headers:
        #     print(item, headers[item])
        return False
    with open(local, 'ab+') as fp_data:
        fp_lock = open(f'{local}.lock', open_lock_mode)
        fp_data.seek(current_length)
        for chunk_data in res.iter_content(chunk_size=chunk_size):
            # 写入下载数据
            fp_data.write(chunk_data)
            fp_data.flush()
            current_length += chunk_size
            # 写入下载记录
            fp_lock.seek(0)
            # current_length content_length
            fp_lock.write(int(current_length).to_bytes(length=8, byteorder='little'))
            fp_lock.write(int(content_length).to_bytes(length=8, byteorder='little'))
            fp_lock.flush()
            # 进度条
            RichPrint.progress_bar(current_length / content_length)
        # 计算Hash
        fp_data.seek(0, 0)
        fp_lock.seek(0, 0)
        fp_lock.write(__hash_hexdigest(fp_data.read()).encode('utf-8'))
        fp_lock.close()
    res.close()
    os.rename(f'{local}.lock', f'{local}.ok')
    return True


def unpack_one_file(packed_file, extract_dir):
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)
    file = zipfile.ZipFile(packed_file)
    for f in file.namelist():
        file.extract(f, extract_dir)
    file.close()
