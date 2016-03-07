# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
from django.views.generic.base import TemplateView




__all__ = (
        'HomeView', )


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['comments'] = range(1,5)
        return context

    def get(self, request, *args, **kwargs):
        #aca se hacen las cosas
        return super(HomeView, self).get(request, *args, **kwargs)


