from setuptools import setup

setup(
    name="ESSExplorer",
    version="0.0.0",
    install_requires=[
        "dash",
        "dash-core-components",
        "dash-html-components",
        "dash-table",
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
