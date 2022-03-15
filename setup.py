from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

project_slug = "mcman-index"
module_name = project_slug.replace('-', "_")

setup(
    name=project_slug,
    use_scm_version=True,
    url=f"https://github.com/Senth/{project_slug}",
    license="MIT",
    author="Matteus Magnusson",
    author_email="senth.wallace@gmail.com",
    description="Helps with indexing minecraft mods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha","Topic :: Software Development :: Libraries","License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
