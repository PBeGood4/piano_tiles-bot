from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["mss","pynput"]

setup(
    name="piano_tiles-bot",
    version="1",
    author="PBeGood4",
    author_email="pbegood.mail@gmail.com",
    description="The fastest piano tiles bot",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="piano tiles python3 bot mss pynput",
    url="https://github.com/PBeGood4/piano_tiles-bot/",
    scripts=["tilesbot.py"],
    packages=[],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
