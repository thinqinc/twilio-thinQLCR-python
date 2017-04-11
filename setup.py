from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='twilio_thinQLCR',
      version='1.0',
      description='Twilio 5.x Wrapper Python Library For thinQ LCR integration.',
      long_description=readme(),
      keywords='twilio thinq wrapper python',
      url='https://github.com/thinqinc/twilio-thinQLCR-python',
      author='thinQ',
      author_email='info@thinq.com',
      license='MIT',
      packages=['twilio_thinQLCR'],
      install_requires=[
          'twilio>=5.0'
      ],
      include_package_data=True,
      zip_safe=False)