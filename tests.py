from easypil import PILImage
import unittest
import os


class PILImageTest(unittest.TestCase):

  def setUp(self):
    self.base_image = ''
    self.filename = 'test.jpg'
    self.is_save = False

  def tearDown(self):
    if self.is_save:
      os.remove(self.filename)
    self.is_save = False

  def test_draw_text_on_image(self):
    i = PILImage(self.base_image, self.filename)
    i.draw_text("Regular").show()

  def test_draw_positioned_text_on_image(self):
    i = PILImage(self.base_image, self.filename)
    i.draw_text("Positioned", position=(25, 25)).show()

  def test_draw_large_text_on_image(self):
    i = PILImage(self.base_image, self.filename)
    i.draw_text("Large", font_size=36).show()

  def test_draw_rotated_text_on_image(self):
    i = PILImage(self.base_image, self.filename)
    i.draw_text("Rotated Text. Hehehe", rotate=-90, position=(0, 0)).show()

  def test_saving(self):
    i = PILImage(self.base_image, self.filename)
    i.draw_text("Rotated Text. Hehehe", rotate=-90, position=(0, 0))
    i.save()
    self.is_save = True


if __name__ == '__main__':
  unittest.main()
