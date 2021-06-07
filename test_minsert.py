#!/usr/bin/env python

# pylint: skip-file

from minsert.minsert import MarkdownFile, is_comment, is_ender, is_starter


def test_is_comment():
    assert is_comment("<!--  -->")
    assert is_comment("<!-- hello how are you -->")
    assert is_comment("<!-- -->")
    assert not is_comment("< !--  -->")
    assert not is_comment("<!-- -- >")


def test_is_starter():
    assert not is_starter("<!-- start -->")
    assert is_starter("<!-- start block -->") == "block"
    assert not is_starter("Normal Sentence")


def test_is_ender():
    assert is_ender("<!-- end -->")
    assert is_ender("<!-- end blah blah-->")
    assert is_ender("<!-- blah end blah-->")
    assert not is_ender("end")
    assert not is_ender("<!-- blend -->")


def test_minsert():
    with open("test.md", "w") as file:
        file.write("Hello\n<!-- start block-->\n<!-- end -->\nOk bye")
    mfile = MarkdownFile("test.md")
    mfile.insert({"block": "what"})
    with open("test.md") as file:
        content = file.read()
        assert content == "Hello\n<!-- start block-->\nwhat\n<!-- end -->\nOk bye"
