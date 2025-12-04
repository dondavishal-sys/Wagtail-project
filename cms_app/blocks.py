from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeadingBlock(blocks.CharBlock):
    class Meta:
        template = "cms_app/blocks/heading_block.html"
        icon = "title"
        label = "Heading"

class ParagraphBlock(blocks.TextBlock):
    class Meta:
        template = "cms_app/blocks/paragraph_block.html"
        icon = "pilcrow"
        label = "Paragraph"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    
    class Meta:
        template = "cms_app/blocks/image_block.html"
        icon = "image"
        label = "Image"

class FeatureBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.TextBlock()
    icon = ImageChooserBlock(required=False)
    
    class Meta:
        template = "cms_app/blocks/feature_block.html"
        icon = "placeholder"
        label = "Feature"

class CtaBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.URLBlock()
    
    class Meta:
        template = "cms_app/blocks/cta_block.html"
        icon = "plus"
        label = "Call to Action"
