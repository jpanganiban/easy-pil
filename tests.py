from easypil import EasyImage
import unittest
import os


class PILImageTest(unittest.TestCase):

  def setUp(self):
    self.base_image = 'coupon.png'
    self.filename = 'test.png'
    self.is_save = False

  def tearDown(self):
    if self.is_save:
      os.remove(self.filename)
    self.is_save = False

  def test_me(self):

    image = EasyImage(self.filename, self.base_image,
        font='/usr/share/fonts/truetype/msttcorefonts/arial.ttf')
    image.draw_text('test', rotation=90, position=(10, 10), font_size=30)
    image.show()

  def test_without_base(self):
    image = EasyImage(self.filename,
        font='/usr/share/fonts/truetype/msttcorefonts/arial.ttf')
    image.draw_text('test', rotation=90, position=(10, 10), font_size=30)
    image.show()


if __name__ == '__main__':
  unittest.main()
