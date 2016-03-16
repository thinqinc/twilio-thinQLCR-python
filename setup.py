from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='twilio_thinQLCR_python',
      version='0.1',
      description='Twilio Wrapper Python Library For thinQ LCR integration.',
      long_description=readme(),
      keywords='twilio thinq wrapper python',
      url='https://github.com/thinqinc/twilio-thinQLCR-python',
      author='thinQ',
      author_email='info@thinq.com',
      license='MIT',
      packages=['twilio_thinQLCR_python'],
      install_requires=[
          'twilio'
      ],
      include_package_data=True,
      zip_safe=False)