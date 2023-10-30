# `_`

`_` allows you to write Python code using only `_`.

## Installation

To install the latest in-development version:

```shell
python -m pip install git+https://github.com/lemonyte/_
```

Or, to install a specific commit or tag:

```shell
python -m pip install git+https://github.com/lemonyte/_@{commit-or-tag}
```

[Python 3.8](https://www.python.org/downloads/) or a newer version is required.

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

## Troubleshooting

If you get `SyntaxError: invalid syntax`, make sure the line `# coding: _` is present at the top of your script.

If you get `SyntaxError: encoding problem: _`, follow the steps below to make sure the `_` encoding is registered on startup:

1. Run `SITE_PACKAGES=$(python -c 'import sysconfig; print(sysconfig.get_path("purelib"))')` to get the path to the Python site-packages directory.
2. Run `echo "import underscores" > "$SITE_PACKAGES/_.pth"` to register the `_` encoding on startup.

> Note: if using PowerShell, use `$SITE_PACKAGES` instead of `SITE_PACKAGES` to assign the variable.

This issue is commonly encountered when installing `_` into the user site-packages.

## Credits

`_` is a port of [`_`](https://github.com/mame/_) from Ruby to Python.
Please check out the original creator [mame](https://github.com/mame).

Big thanks to [shailist](https://github.com/shailist) for [this](https://shailist.github.io/posts/python-source-preprocessor-custom-encoding/) awesome post on custom encodings.

## License

[MIT License](LICENSE.txt)
