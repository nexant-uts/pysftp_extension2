"""setup for package"""

from setuptools import setup

# with open('README.rst') as h_rst:
#     LONG_DESCRIPTION = h_rst.read()
#
# with open('docs/changes.rst') as h_rst:
#     BUF = h_rst.read()
#     BUF = BUF.replace('``', '$')        # protect existing code markers
#     for xref in [':meth:', ':attr:', ':class:', ':func:']:
#         BUF = BUF.replace(xref, '')     # remove xrefs
#     BUF = BUF.replace('`', '``')        # replace refs with code markers
#     BUF = BUF.replace('$', '``')        # restore existing code markers
# LONG_DESCRIPTION += BUF
with open("README.rst", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# LONG_DESCRIPTION = "pysftp_extension"

DESCRIPTION = "A friendly face on SFTP"

setup(
    name="pysftp_extension2",
    version="0.2.14",
    packages=[
        "pysftp_extension2",
    ],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["paramiko>=2.9.2"],
    # metadata for upload to PyPI
    author="Resource Innovations",
    author_email="",
    description=DESCRIPTION,
    license="BSD",
    keywords="sftp ssh ftp internet",
    url="https://github.com/nexant-uts/pysftp_extension2",  # project home page
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    platforms=["any"],
    download_url="",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
