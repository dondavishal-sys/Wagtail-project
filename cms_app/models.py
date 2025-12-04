from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel  # ONLY FieldPanel is needed now
from .blocks import HeadingBlock, ParagraphBlock, ImageBlock, FeatureBlock, CtaBlock

class CMSHomePage(Page):
    template = "cms_app/cms_home_page.html"

    main_content = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', ParagraphBlock()),
        ('image', ImageBlock()),
        ('feature', FeatureBlock()),
        ('cta', CtaBlock()),
    ], blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('main_content'),  # just use FieldPanel
    ]
