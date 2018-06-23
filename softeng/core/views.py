from django.views.generic import TemplateView
from .models import SoftwareEngineering


class HomePageView(TemplateView):
    """
    Page to show information about software engineering.
    """

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        """
        Insert software engineering data into template
        """

        software = SoftwareEngineering()

        context = super(HomePageView, self).get_context_data(**kwargs)

        context['software'] = software

        return context
