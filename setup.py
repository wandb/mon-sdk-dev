from setuptools import setup
import pkg_resources

with open("requirements.txt") as requirements_file:
    requirements = pkg_resources.parse_requirements(requirements_file) 

setup(
    name="mon-sdk-deve",
    version="0.0.1.dev1",
    description="W&B dev package for monitoring sdk.",
    author="Weights & Biases",
    author_email="support@wandb.com",
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
