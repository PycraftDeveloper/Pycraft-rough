import setuptools, os

base = os.path.dirname(__file__)

with open(os.path.join(base, "README.md"), "r") as fh:
    long_description = fh.read()
with open(r"requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(name="python-pycraft",
                 version="0.9.5-1",
                 author="PycraftDev",
                 author_email="thomasjebbo@gmail.com",
                 description="The open-world, OpenGL video game made in Python",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 url="https://github.com/PycraftDeveloper/Pycraft",
                 classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent"],
                 python_requires=">=3.7",
                 install_requires=requirements)
