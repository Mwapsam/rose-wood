from home.models import HomePage
from wagtail.models import Site


def home_page(request):
    wagtail_site = Site.find_for_request(request)
    context = {"home_page": HomePage.objects.in_site(wagtail_site).first()}
    return context
