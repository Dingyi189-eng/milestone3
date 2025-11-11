from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

def test_replace_b_with_blockquote():
    html = "<p>Hello <b>world</b></p>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "<blockquote>world</blockquote>" in str(soup)

def test_no_change_for_other_tags():
    html = "<p>Hello <i>world</i></p>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "<i>world</i>" in str(soup)
