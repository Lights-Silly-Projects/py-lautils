#!/usr/bin/env python3

import setuptools  # type:ignore[import]
from pathlib import Path

long_description = Path("README.md").read_text()
install_requires = Path("requirements.txt").read_text()

package_name = "lautils"

exec(Path(f'{package_name}/_metadata.py').read_text(), meta := dict[str, str]())

setuptools.setup(
    name=package_name,
    version=meta['__version__'],
    author=meta['__author_name__'],
    author_email=meta['__author_email__'],
    maintainer=meta['__maintainer_name__'],
    maintainer_email=meta['__maintainer_email__'],
    description=meta['__doc__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        package_name
    ],
    package_data={
        package_name: ['py.typed'],
    },
    install_requires=install_requires,
    project_urls={
        "Source Code": 'https://github.com/Lights-Silly-Projects/py-lautils',
    },
    classifiers=[
        "Natural Language :: English",

        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",

        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires='>=3.11',
)
