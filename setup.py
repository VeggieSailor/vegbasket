from setuptools import setup

setup(name='veggiesailor',
      version='0.1',
      description="Veggie Sailor",
      long_description="",
      author='Rafal Zawadzki',
      author_email='bluszcz@bluszcz.net',
      license='TODO',
      packages=['vegbasketapp'],
      zip_safe=False,
      install_requires=[
          'Django',
          # 'Sphinx',
          # ^^^ Not sure if this is needed on readthedocs.org
          # 'something else?',
          ],
      )
