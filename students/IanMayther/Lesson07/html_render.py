#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'

    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write('\n')
        for content in self.contents:           
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            out_file.write('\n')
        out_file.write(cur_ind + self._close_tag())    
    
    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" {0}=\"{1}\"".format(key, value))
        open_tag.append(">")
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self):
        return "</{}>".format(self.tag)


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write('<!DOCTYPE html>')
        out_file.write('\n')
        super().render(out_file, cur_ind)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'Head'

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag())
        out_file.write('\n')
        for content in self.contents:           
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write(self._close_tag())
        out_file.write('\n')

class OneLineTag(Element):
    tag = 'OneLineTag'

    def append(self, new_content):
        raise NotImplementedError

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
          
class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    tag = 'SelfClosing'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any contents")
        super().__init__(content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind + tag)          

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "Ul"

class Li(Element):
    tag = "Li"

class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = self.tag + str(level)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"