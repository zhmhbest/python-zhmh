import setuptools
from pyzhmh import __VERSION

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    # 环境依赖（版本、包、文件<包:匹配>）
    python_requires='>=3',
    install_requires=['requests>=2.18.0'],
    # package_data={'': ['*.txt']},
    # 'MANIFEST.in': 打包时包含/排除指定规则的文件

    # 打包配置
    packages=setuptools.find_packages(),  # exclude=['package']
    include_package_data=True,

    # 作者资料
    author="zhmh",
    author_email="zhmhbest@gmail.com",

    # 模块信息
    name="python-zhmh",
    version=__VERSION,
    description="Python Common Command",
    # keywords="hello common",
    license="MIT",  # https://choosealicense.com/
    url="https://github.com/zhmhbest/python-zhmh",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
