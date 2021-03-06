import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UiL Django Core",
    version="2.0.0",
    author="UiL OTS Labs",
    author_email="labbeheer.gw@uu.nl",
    description="A shared code library for UiL OTS Django projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UiL-OTS-labs/django-shared-core",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=2.0',
        'pyscss',
        'lesscpy',
        'closure',
        'vbuild',
        'requests',
        'PyJWT',
        'djangorestframework',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 2.2",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)

