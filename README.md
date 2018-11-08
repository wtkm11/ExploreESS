# ExploreESS
Explore some data in the European Social Survey

## Data
The European Social Survey data for year 2016 is available here: https://www.europeansocialsurvey.org/download.html?file=ESS8e02&y=2016 .

### Accessing the survey data

1. To obtain the data, sign in with your email address.
2. Download the SPSS ZIP file and extract `ESS8e02.sav` from the ZIP file.

```
$ unzip ESS8e02.spss.zip
```

3. The data can be converted to CSV format with `pspp`.

```
$ pspp-convert ESS8e02.sav ESS8e02.csv
```

4. Ensure that `ESS8e02.csv` is in the `essexplorer/data` directory. While ESS
   data is freely available, I am not permitted to distribute it.

## How to run

1. Create and activate a Python3 virtual environment in which to install
   dependencies.

  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```

2. Navigate to the project root directory (the directory with the `setup.py`)
   and install the dependencies.

   ```
   $ pip install -e .
   ```

3. Start the HTTP server.

   ```
   $ ess-explorer
   ```
