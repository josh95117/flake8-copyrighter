flake8-copyrighter
==================

`flake8-copyrighter` is a Flake8 extension to check that non-empty files checked by Flake8 contain a copyright statement and that the year of the file's modification date is listed within the copyright statement. `flake8-copyrighter`'s default settings attempt to identify a line containing a copyright string, using the following regular expression pattern (_case insensitive_).

``` python
r'copyright .+ [0-9][0-9][0-9][0-9]'
```

Once a line containing a copyright statement is identified, `flake8-copyrighter` searches within the line for all copyright years using the following regular expression:

``` python
r'\d{4}'  # 4-digit years
```

`flake8-copyrighter` then checks the file's modification date and compares to the highest year found. Violations will be raised if the file's modification year is not listed in the copyright string, or if no copyright string is found in a file (except for completely empty files).

&nbsp;

The following table shows some example strings and the year that would be identified with the default settings:

| Copyright string                         | Year | Notes                                           |
|------------------------------------------|------|-------------------------------------------------|
| Copyright © 2012 BigCo, Inc.             | 2012 |                                                 |
| copyright (c) 2011, 2015-2018 Mega Corp. | 2018 |                                                 |
| Copyright 1999 Partytime, Inc            | 1999 |                                                 |
| Copyright (c) 2017-18                    | 2017 | Default pattern searches for 4-digit years      |
| \<no copyright string in file\>          | n/a  | "Copyright string not found" message raised     |

&nbsp;

Checker results
---------------

`flake8-copyrighter` uses the following message codes to report problems found:

| Code    | Message                                                  |
|---------|----------------------------------------------------------|
| CRC0000 | Copyright string does not contain file modification year |
| CRC0001 | Copyright string not found                               |

&nbsp;

Options
-------

- To override the default pattern for a **line** containing a copyright string, use `--crc-line-pattern=[YOUR_PATTERN]` as an option for either flake8 CLI or config file.
  - To override the default **year** identifier pattern, use the `--crc-year-pattern=[YOUR_PATTERN]` option.
  - `flake8-copyrighter` uses a default message code base (and plugin entry point) of 'CRC000', per the [Flake8 plugin authoring guidelines](http://flake8.pycqa.org/en/latest/plugin-development/registering-plugins.html). Individual messages add one digit to this base ('CRC0000', 'CRC0001'). `flake8-copyrighter` provides the `--crc-code-base` option to work around a shortcoming of the current Visual Studio Code implementation of Flake8 linting, which only recognizes Flake8 message codes that begin with a single character followed by any number of digits. Thus `flake8-copyrighter`'s defaults will not show in VSCode's **PROBLEMS** panel when Flake8 linting is enabled. To get around this, you can use this option in your VSCode `python.linting.flake8Args` setting, for example:
    ``` json
    "python.linting.flake8Args": ["--crc-code-base=W9999"],
    ```

&nbsp;

Installation and usage
----------------------

To install, execute `python setup.py install` or `pip install .` in the directory containing `setup.py`. When you next run Flake8, the extension will be active and checks will be performed.