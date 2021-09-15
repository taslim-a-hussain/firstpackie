from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="firstpackie",
    version="0.0.2",
    description="Say hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taslim-a-hussain/helloworld",
    author="Taslim A Hussain",
    author_email="taslim@outlook.co.nz",
    py_modules=["firstpackie"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
        ]
)
