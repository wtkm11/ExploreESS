from setuptools import setup

setup(
    name="ESSExplorer",
    version="0.0.0",
    install_requires=[
        "dash==0.29.0",
        "dash-core-components==0.36.0",
        "dash-html-components==0.13.2",
        "dash-table==3.1.3",
        "matplotlib",
        "numpy",
        "pandas",
        "plotly"
    ],
    entry_points={
        'console_scripts': [
            'ess-explorer = essexplorer.app:app.run_server',
        ],
    }
)
