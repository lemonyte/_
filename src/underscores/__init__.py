"""
`_` allows you to write Python code using only `_`.

Importing this module will register the `_` encoding with the Python interpreter,
which should be done automatically by the `_.pth` file in the `site-packages` directory.
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
__version__ = "0.0.3"
__all__ = ("_",)
