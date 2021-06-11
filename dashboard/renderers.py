from django.core.exceptions import ImproperlyConfigured
from django.templatetags.static import static
from django.conf import settings
from react.render import render_component
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import status
import json
from django.core.cache import cache
from react.exceptions import ReactRenderingError
from django.template.context_processors import csrf


class ReactTemplateHTMLRenderer(TemplateHTMLRenderer):
    """
    An HTML renderer which uses python-react to render react components.

    The `rendered_react_template_variable_name` attribute specifies the name
    of the Django template variable to contain the rendered React code. This
    should be included in the Django template using the `safe` template filter.

    The view needs to have `component_path` attribute, or `get_component_path()` method.
    Either should return location of JSX component file relative to static files path.
    """

    rendered_react_template_variable_name = 'rendered_react'
    component_path = None

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        if response.status_code in [status.HTTP_404_NOT_FOUND]:
            return super(ReactTemplateHTMLRenderer, self).render(data,
                                                                 accepted_media_type=accepted_media_type,
                                                                 renderer_context=renderer_context)

        renderer_context = renderer_context or {}
        data = data or {}

        if 'django_template_context' in data:
            django_template_context = data['django_template_context']
        else:
            django_template_context = {}

        if isinstance(data, list):
            data = {'dataList': data}
        view = renderer_context['view']
        request = renderer_context['request']
        component_path = self.get_component_path(view)

        

        data['global'] = {}
        data['global']['csrf'] = str(csrf(request)['csrf_token'])
        import os

        rendered = render_component(os.path.join(settings.BASE_DIR,component_path), props=data)
        template_context = dict((
            ('jsx_component', component_path),
            ('jsonified_props', data),
            (self.rendered_react_template_variable_name, rendered)
        ))

        template_context.update(django_template_context)
        return super(ReactTemplateHTMLRenderer, self).render(template_context,
                                                             accepted_media_type=accepted_media_type,
                                                             renderer_context=renderer_context)

    def get_component_path(self, view):
        if hasattr(view, 'get_component_path'):
            return view.get_component_path()
        elif hasattr(view, 'component_path'):
            return view.component_path
        raise ImproperlyConfigured(
            'Returned a template response with no `component_path` attribute set on either the view or response'
        )

