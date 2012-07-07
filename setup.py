from setuptools import setup


setup(name="easy-pil",
      description="PIL made easy",
      author="Jesse Panganiban",
      py_modules=['easypil'],
      install_requires=[
          'PIL'
        ],
      test_suite='tests'
      )
