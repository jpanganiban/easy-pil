import Image, ImageDraw, ImageFont, ImageChops, ImageOps
from functools import partial


class EasyImage(object):

  def __init__(self, filename, base_image=None, dimensions=None, font=None):
    self.filename = filename
    self.base_image = self.__create_base_image(base_image)
    self.__dimensions = dimensions
    self.__font = font

  def __repr__(self):
    return "<EasyImage %{filename}>" % {'filename': self.filename}

  @property
  def dimensions(self):
    return self.__dimensions or self.base_image.size

  def __create_base_image(self, base_image, mode='RGBA', size=(100, 100),
                          color=(255, 255, 255, 0)):
    if base_image:
      return Image.open(base_image)
    return Image.new(mode, size, color)

  def font(self, size=None):
    if not self.__font:
      return ImageFont.load_default()
    return ImageFont.truetype(self.__font, size)

  def draw_text(self, text, position=(0, 0), color='black', font=None,
                font_size=12, rotation=0, **kwargs):
    """Draws a text on the base image."""
    font = self.font(font_size)

    text_image = Image.new('L', self.dimensions, 'black')
    draw_text_image = ImageDraw.Draw(text_image)
    draw_text_image.text(position, text, font=font, fill='white')

    alpha = Image.new('L', self.dimensions)
    alpha = ImageChops.lighter(alpha, text_image)

    solidcolor = Image.new('RGBA', self.dimensions, color)
    image_mask = Image.eval(text_image, lambda p: 255 * (int(p != 0)))
    self.base_image = Image.composite(solidcolor, self.base_image, image_mask)
    self.base_image.putalpha(alpha)

  def save(self, filename=None, file_format="PNG", **kwargs):
    """Saves this EasyImage."""
    self.base_image.save(filename or self.filename, file_format, **kwargs)

  def show(self):
    self.base_image.show()
