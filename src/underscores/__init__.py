"""
`_` allows you to write Python code using only `_`.

You shouldn't need to import this module unless the .pth file fails to install.
See the [README](https://github.com/lemonyte/_) for more information.

## Usage

The following script is a "Hello, world!" program which can be executed by the Python interpreter:

```python
# coding: _
_ ____ _ _____ _ ____ __ _ _ ___ ______ ____ _ ____ _ ___ _ ____ __ ___ _ __ _
_____ _ _ ______ _____ _ ___ _ _ _ ___ _____ ______ _ ____ _ _ _ ____ _ _ _ ____
_ ____ _ __ __ ___ _ _ ______ ___ _ ____ __ ______ _ ____ _ ____ _ ____ __ _ _
____ _ _ _ ___ _____ _____ _ _ ______ ____ _ _ ______ _____ _ __ _ ______
```

You can generate a script with `_`:

```python
print('print("Hello, world!")'.encode("_").decode("utf-8"))
```
"""

from underscores._ import _

__name__ = "_"
__version__ = "0.0.1"
__all__ = ("_",)
