import os

# python3 -m pip install --user --upgrade setuptools wheel

if __name__ == '__main__':
    os.system('python setup.py sdist bdist_wheel')
