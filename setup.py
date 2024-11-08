import setuptools

setuptools.setup(
  name="webots",
  version="2.0.0",
  author="James Hu",
  author_email="jameshu@live.com",
  description="Webots API Wrapper R2024a",
  long_description="Webots API Wrapper",
  long_description_content_type="text/markdown",
  url="https://github.com/statsmind/webots-python",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  package_data={
    "webots": ["lib/*"]
  }
)