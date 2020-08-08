import os
from zhmh import __VERSION

WHL_FILE = os.path.abspath(f"./dist/python_zhmh-{__VERSION}-py3-none-any.whl")
activate = os.path.abspath(os.path.join(os.curdir, 'venv', 'Scripts', 'activate.bat'))

if __name__ == '__main__':
    with open('./venv/reinstall.bat', 'w') as fp:
        fp.write(f'call "{activate}"\n')
        fp.write('pip uninstall python-zhmh\n')
        fp.write(f'pip install "{WHL_FILE}"\n')
