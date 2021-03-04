from os.path import join, dirname, abspath
from setuptools.config import read_configuration
from setuptools import setup


def write_version_py(version, filename=join('src', 'ampardiso', 'version.py')):
    text = """
# THIS FILE IS GENERATED FROM AMPARDISO SETUP.PY
version = '{}'
""".format(version)

    with open(filename, 'w') as fp:
        fp.write(text)


if __name__ == '__main__':
    here = abspath(dirname(__file__))
    metadata = read_configuration(join(here, 'setup.cfg'))['metadata']
    write_version_py(metadata['version'])
    setup()
