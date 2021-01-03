#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = []
        if kwargs.__len__() is not 0:
            for item in kwargs.items():
                self.attributes.append(item)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write("\n")

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes:
            open_tag.append(" {}=\"{}\"".format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Head(Element):
    tag = "head"


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"

class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write("\n")

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag += str(level)
        super().__init__(content, **kwargs)

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = "meta"