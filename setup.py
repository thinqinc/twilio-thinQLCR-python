from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='twilio_thinQLCR',
      version='2.0.0',
      description='Twilio 6.x Wrapper Python Library For thinQ LCR integration.',
      long_description=readme(),
      keywords='twilio thinq wrapper python',
      url='https://github.com/thinqinc/twilio-thinQLCR-python',
      author='thinQ',
      author_email='info@thinq.com',
      license='MIT',
      packages=['twilio_thinQLCR'],
      install_requires=[
          'twilio>=6.0'
      ],
      include_package_data=True,
      zip_safe=False)