from quiz.models import Text, Image, Slide

class BaseSlide:
    def __init__(self, slide):
        self.slide = slide

    def info(self):
        return {
            'type': self.slide.type
        }
    
    @staticmethod
    def create(type, fk):
        return Slide.objects.create(type=type, fk=fk)

    def delete(self):
        self.slide.delete()

class TextSlide(BaseSlide):
    def __init__(self, slide):
        assert slide.type = 'Text'

        super().__init__(slide)

        from quiz.models import Text
        self.text = Text.objects.get(pk=slide.fk)
    
    def info(self):
        base_info = super().info()
        base_info['text'] = self.text.text
        return base_info

    @staticmethod
    def create(text):
        text_field = Text.objects.create(text=text)
        return BaseSlide.create('Text', text_field.id)

    def delete(self):
        super().delete()
        self.text.delete()

class ImageSlide(BaseSlide):
    def __init__(self, slide):
        assert slide.type = 'Image'

        super().__init__(slide)

        from quiz.models import Image
        self.image = Image.objects.get(pk=slide.fk)
    
    def info(self):
        base_info = super().info()
        base_info['image'] = self.image.image
        return base_info

    @staticmethod
    def create(image):
        image_field = Image.objects.create(image=image)
        return BaseSlide.create('Image', image_field.id)

    def delete(self):
        super().delete()
        self.image.delete()

slides = {
    'Text': TextSlide,
    'Image': ImageSlide
}

def get_slide(slide):
    return slides[slide.type](slide)

def create_slide(slide_info):
    return slides[slide_info.type].create(slide_info.info)
