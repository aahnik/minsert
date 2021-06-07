# minsert

Insert dynamic content in markdown, without using a separate template file.

[![Tests](https://github.com/aahnik/minsert/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/minsert/actions/workflows/test.yml)
[![Code Quality](https://github.com/aahnik/minsert/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/minsert/actions/workflows/quality.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/minsert)
[![codecov](https://codecov.io/gh/aahnik/minsert/branch/main/graph/badge.svg?token=Q1XROUHDRM)](https://codecov.io/gh/aahnik/minsert)

## Motivation

Inspired by jinja.

Your actual markdown file is the template file itself.
Just make a block of content just by using comments, which indicate the start and
end of the block.

This is really great for making a dynamic GitHub README.
No hassle of creating a separate template file.
Using a simple python script and GitHub Actions,
you can automatically update the contents of the markdown file.

## Installation

```shell
pip install minsert
```

## Syntax

Using minsert is easy. Just write normal markdown.
The start and end of named blocks are marked by special comments.

Start a block named `my_block`

```markdown
<!-- start my_block -->
```

End a block

```markdown
<!-- end -->
```

You must end the current block before starting a new one.

## Usage

For example you have a markdown file `test.md` like this.

```markdown
hello
<!-- start thing1 -->
<!-- end -->
what is happening
<!-- start thing2 -->
<!-- end -->
Bye!
```

Create a simple script `update.py` for updating the markdown file.

```python
# update.py

from minsert import MarkdownFile

file = MarkdownFile("test.md")
things = {
    "thing1": "hi hello",
    "thing2": "ping pong",
}
file.insert(things)

```

The markdown file gets updated with the value of the blocks.

```markdown
hello
<!-- start thing1 -->
hi hello
<!-- end -->
what is happening
<!-- start thing2 -->
ping pong
<!-- end -->
Bye!
```

Now try running `update.py` after changing the values in the `things` dictionary.
You will see that minsert will neatly update the `test.md` without fail.
