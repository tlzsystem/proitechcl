from django.views.generic import TemplateView


class DahsboardView(TemplateView):
    template_name = "dashboard/dashboard.html"
