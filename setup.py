from setuptools import setup, find_packages

setup(
    name="biological-age",
    version="0.1.0",
    packages=find_packages(where="src"),   # 🔥 key change
    package_dir={"": "src"},               # 🔥 key change
)
