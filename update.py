import os

# pip install -U pip setuptools twine

# https://pypi.org/manage/projects/
# https://test.pypi.org/manage/projects/

if __name__ == '__main__':
    os.system("twine upload dist/*")
