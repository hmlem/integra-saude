from setuptools import setup

setup(
    name='commands',
    entry_points='''
        [flask.commands]
        test=app.commands:cli
    ''',
)