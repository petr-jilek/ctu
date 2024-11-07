# Setup Python with virtual environment

## Requirements

- Python 3.12.5
- pip 21.2

## Step 1 - Setup virtual environment

```sh
python -m venv env
```

## Step 2 - Activate virtual environment

On linux/macOS:

```sh
source env/bin/activate
```

On Windows:

```sh
.\env\Scripts\activate
```

## Step 3 - Check python path

On linux/macOS:

```sh
which python
```

On Windows:

```sh
where python
```

The output should be the path to the python executable in the virtual environment. The path should contain the `env/bin/python` or `env/Scripts/python` directory.

## Step 4 - Install dependencies

```sh
pip install -r requirements.txt
```

## Step 5 - Install the package

```sh
pip install <package-name>
```

Or outside the virtual environment:

```sh
python -m pip install <package-name>
```

## Step 6 - Run

Run the python file:

```sh
python <file-name>.py
```

Run jupyter notebook:

```sh
python -m notebook
```

## Step 7 - Deactivate virtual environment

```sh
deactivate
```
