import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch-yolov4",
    version="0.0.2",
    #author="Example Author",
    #author_email="author@example.com",
    description="Pytorch implementation of YOLOv4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metargus/PyTorch_YOLOv4",
    #project_urls={
    #    "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "numpy==1.17",
        "opencv-python >= 4.1",
        "torch == 1.6",
        "torchvision",
        "matplotlib",
        "pycocotools",
        "tqdm",
        "pillow",
        "tensorboard >= 1.14"
    ]
)