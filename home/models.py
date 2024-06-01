import uuid
from django.db import models
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from wagtail.models import Page, Orderable, ClusterableModel
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtailmetadata.models import MetadataPageMixin

from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)


@register_setting
class NavigationSettings(BaseGenericSetting):
    # id = models.AutoField(primary_key=True)
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    facebooks_url = models.URLField(verbose_name="Facebook URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    tiktok_url = models.URLField(verbose_name="Tiktok URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("facebooks_url"),
                FieldPanel("instagram_url"),
                FieldPanel("tiktok_url"),
            ],
            "Social settings",
        )
    ]


class HomePage(MetadataPageMixin, RoutablePageMixin, Page):
    content_panels = Page.content_panels + [
        InlinePanel("projects"),
        InlinePanel("slides"),
    ]

    @path("project/<uuid:id>/")
    def project_detail(self, request, id):
        try:
            project = Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise Http404("Project does not exist")

        return render(
            request,
            "home/project_detail.html",
            context={"project": project},
        )

    def get_sitemap_urls(self, request=None):
        urls = []

        # Add the HomePage URL
        urls.append({
            'location': self.full_url,
            'lastmod': timezone.now(),
            'priority': 0.8,
        })

        # Add URLs for each project
        for project in self.projects.all():
            project_url = self.reverse_subpage('project_detail', args=[str(project.id)])
            urls.append({
                'location': self.full_url + project_url,
                'lastmod':  timezone.now(),
                'priority': 0.5,
            })

        return urls


class ProjectImages(Orderable):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = ParentalKey(
        "Project", related_name="project_images", on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="project_images",
    )


class Project(ClusterableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="projects", null=True
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        InlinePanel("project_images", label="Project Images"),
    ]


class SlideImages(Orderable):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slide = ParentalKey("Slide", related_name="slide_images", on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="slide_images",
    )


class Slide(ClusterableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="slides", null=True
    )

    panels = [
        FieldPanel("title"),
        InlinePanel("slide_images", label="Slide Images"),
    ]
