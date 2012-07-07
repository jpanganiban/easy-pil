import Image, ImageDraw, ImageFont


class PILImage(object):

  fonts_dir = "/usr/share/fonts/truetype/msttcorefonts/"

  def __init__(self, base_image=None, filename="", dimensions=(100, 100)):
    self.__base_image = self._create_image(base_image) if base_image else self.create_bg(dimensions)
    self.filename = filename or 'untitled.jpg'
    self.dimensions = self.base_image.size or dimensions

  @property
  def base_image(self):
    if not self.__base_image:
      self.__base_image = self._create_image('RGBA', self.dimensions)
    return self.__base_image

  def _font_path(self, filename=""):
    """Returns a msttcorefonts path given a filename."""
    filename = filename or "arial.ttf"
    return "%s%s" % (self.fonts_dir, filename)

  def truetype_font(self, path, size, **kwargs):
    return ImageFont.truetype(path, size, **kwargs)

  def _create_image(self, mode, dimensions, color="#fff"):
    return Image.new(mode, dimensions, color)

  def create_mask(self, dimensions=(0, 0), color="#fff"):
    return self._create_image('L', dimensions or self.dimensions, color)

  def create_bg(self, dimensions=(0, 0), color="#fff"):
    return self._create_image('RGBA', dimensions or self.dimensions, color)

  def draw_image(self, image):
    return ImageDraw.Draw(image)

  def draw_text(self, text, position=(0,0), rotate=0, fill="#222",
                font_size=12, font_name=None, **kwargs):
    font = self.truetype_font(self._font_path(font_name), font_size)
    image_text = self.create_mask(font.getsize(text))
    draw_text = self.draw_image(image_text)
    draw_text.text((0, 0), text, font=font, fill=fill)

    transformed = image_text.rotate(rotate, expand=0)

    self.base_image.paste(transformed, position)
    return self.base_image

  def save(self, filename="", file_format="JPEG", **kwargs):
    self.base_image.save(filename or self.filename, file_format, **kwargs)
