from setuptools import setup, find_packages
from tail_slack import __version__


class About(object):
    NAME = 'tail_slack'
    AUTHOR = 'sagnikrayc'
    VERSION = __version__
    EMAIL = "sagnikrayc@gmail.com"
    URL = "https://www.github.com/sagnik/tail_slack"


def main():
    setup(
        name=About.NAME,
        version=About.VERSION,
        description='tail a file and send the content to a slack webhook',
        author=About.AUTHOR,
        author_email=About.EMAIL,
        license='Apache 2.0',
        url=About.URL,
        packages=find_packages(),
        install_requires=[
            'watchdog',
            'slack_sdk'
        ],
        entry_points={
            'console_scripts': [
                'tail_slack = tail_slack.cli:main'
            ],
        },
        extras_require={}
    )


if __name__ == "__main__":
    main()