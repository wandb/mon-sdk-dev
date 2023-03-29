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
    extras_require={"ecosystem": requirements_ecosystem},
)
