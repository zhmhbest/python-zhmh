import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    # 环境依赖（版本、包、文件<包:匹配>）
    # python_requires='>=3',
    # install_requires=[''],
    package_data={'': ['*.txt']},

    # 打包配置
    # scripts=['.py'],
    packages=setuptools.find_packages(exclude=['build.py', 'test.py']),

    # 作者资料
    author="zhmh",
    author_email="zhmhbest@gmail.com",

    # 模块信息
    name="python-zhmh",
    version="0.0.1",
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