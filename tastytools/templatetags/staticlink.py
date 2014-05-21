from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()


class StaticLinkNode(template.Node):
    def __init__(self, file_type, file_path):
        print file_type, file_path
        self.file_type = file_type
        if not file_path.endswith(file_type) and file_type != "img":
            file_path = "%s/%s.%s" % (file_type, file_path, file_type)
        else:
            file_path = "%s/%s" % (file_type, file_path)
        self.file_path = file_path

    def render(self, context):
        tag = ''
        if self.file_type == 'js':
            tag = "<script type='text/javascript' src='%s'></script>"
            tag %= (reverse('tastytools_static_url', args=[self.file_path]),)
        if self.file_type == 'css':
            tag = "<link rel='stylesheet' type='text/css' href='%s'>"
            tag %= reverse('tastytools_static_url', kwargs={'path':self.file_path})
        if self.file_type == 'img':
            tag = "<img src='%s'/>"
            tag %= reverse('tastytools_static_url', kwargs={'path':self.file_path})

        return tag


def staticlink_tag(parser, token):
    (staticlink_type, staticlink_file) = tuple(token.split_contents()[1].split(":"))
    return StaticLinkNode(staticlink_type, staticlink_file)


register.tag('staticlink', staticlink_tag)
