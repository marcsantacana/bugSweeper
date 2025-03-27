from setuptools import setup, find_packages

setup(
    name="bugSweeper",
    version="1.0.0",
    author="Marc Santacana",
    description="Herramienta de línea de comandos para simulación y detección de vulnerabilidades.",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "bugSweeper=bugSweeper.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)