# py-lightarrowsexe-utils

A collection of generic utilities I use in different packages.
These are typically going to be functions
that don't necessarily have a place
in the package it was originally needed for.

Full information on each function/wrapper/etc. can be found in the accompanying docstrings.

For further support, leave an issue or contact me on _Discord_ (@lightarrowsexe).

## How to install

Install `lautils` with the following command:

```sh
$ pip3 install lautils
```

Or if you want the latest git version, install it with this command:

```sh
$ pip3 install git+https://github.com/Lights-Silly-Projects/la-utils.git
```

## Usage

After installation, functions can be loaded and used as follows:

```py
import lautils as la

la.FilesizeUnits.MEGABYTES.from_bytes(...)
...
```

## Disclaimer

Anything **MAY** change at any time.
The public API **SHOULD NOT** be considered stable.
If you use lvsfunc in any of your projects,
consider hardcoding a version requirement.
