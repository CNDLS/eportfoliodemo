from django import template
from django.template.defaultfilters import stringfilter
from django.template import loader_tags, Template
from django.conf import settings
from django.template.loader import find_template
from django.template.loader_tags import BaseIncludeNode
from django.template.base import TemplateSyntaxError, TemplateDoesNotExist

register = template.Library()

@register.filter(name='is_composition')

@stringfilter
def is_composition(path):
    return path.find('compose') > 0
    
@register.simple_tag
def editable_state(path):
	if is_composition(path):
		return "editable"
	else:
		return ""
        
# including compiled templates (for eventual uploadable templates)


class CustomIncludeNode(BaseIncludeNode):
	def __init__(self, template_name, template_dir, *args, **kwargs):
		super(CustomIncludeNode, self).__init__(*args, **kwargs)
		self.template_name = template_name
		self.template_dir = template_dir

	def render(self, context):
		try:
			template = self.get_template(context)
			return self.render_template(template, context)
		except:
			if settings.TEMPLATE_DEBUG:
				raise
		return ''
		
	def get_template(self, context):
		template, origin = find_template( self.template_name.resolve(context), [self.template_dir.resolve(context)] )
		if not hasattr(template, 'render'):
			# template needs to be compiled
			template = get_template_from_string(template, origin, self.template_name)
		return template
            
# slight change to default template tag which allows including a template we put in a different place.
def do_custom_include(parser, token):
    """
    Loads a template and renders it with the current context. You can pass
    additional context using keyword arguments.

    Example::

        {% include "foo/some_include" %}
        {% include "foo/some_include" with bar="BAZZ!" baz="BING!" %}

    Use the ``only`` argument to exclude the current context when rendering
    the included template::

        {% include "foo/some_include" only %}
        {% include "foo/some_include" with bar="1" only %}
    """
    bits = token.split_contents()
    if len(bits) < 3:
        raise TemplateSyntaxError("%r tag takes at least two arguments: the name of the template to be included, and the directory in which to find it." % bits[0])
    options = {}
    remaining_bits = bits[3:]
    while remaining_bits:
        option = remaining_bits.pop(0)
        if option in options:
            raise TemplateSyntaxError('The %r option was specified more '
                                      'than once.' % option)
        if option == 'with':
            value = token_kwargs(remaining_bits, parser, support_legacy=False)
            if not value:
                raise TemplateSyntaxError('"with" in %r tag needs at least '
                                          'one keyword argument.' % bits[0])
        elif option == 'only':
            value = True
        else:
			value = False
            # raise TemplateSyntaxError('Unknown argument for %r tag: %r.' %
            #                           (bits[0], option))
        options[option] = value
    isolated_context = options.get('only', False)
    namemap = options.get('with', {})
    return CustomIncludeNode(parser.compile_filter(bits[1]), parser.compile_filter(bits[2]), extra_context=namemap,
                       isolated_context=isolated_context)

register.tag('custom_include', do_custom_include)