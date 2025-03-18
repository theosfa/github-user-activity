# Python CLI app to see user activity
[Link to the task](https://roadmap.sh/projects/github-user-activity)

## Installation

*This project works with Python 3.12+ on macOS and Linux.*

### Step 0: (Optional) Install via script file

To install app just with a few clicks and skip Step 1 - 5

Open terminal and in project folder run:
```bash
source install-app.sh -i
```

To see all possibilities of script run :
```bash
source install-app.sh -h
```


### Step 1: (Optional) Set up a Virtual Environment

To keep the project dependencies isolated from your global Python environment,
it is recommended to create a Python virtual environment.

1. Create a virtual environment (replace `<path to virtualenv>` with the desired path):
    ```bash
    python3 -m venv <path to virtualenv>
    ```

2. Activate the virtual environment:
    ```bash
    source <path to virtualenv>/bin/activate
    ```

---

### Step 2: Install Required Dependencies

Install the necessary dependencies:
```bash
python3 -m pip install -r requirements.txt
```

---

### Step 3: Install the Project

- To install the project, run the following command:
    ```bash
    python3 -m pip install .
    ```

---

### Step 4: (For Developers) Editable Install

If you're a developer and want to make changes to the project while testing them
immediately, you can install the project in "editable" mode. This allows you to
make changes without needing to reinstall each time.

- Run the following command:
    ```bash
    python3 -m pip install -e .
    ```

This links the project directory directly into the environment, so changes are
reflected in real time.

---

## Usage

To see help menu run:
```bash
gua -h
```

To fetch last activity run:
```bash
gua <username> -a
```
[My solution on roadmap.sh](https://roadmap.sh/projects/github-user-activity/solutions?u=67c894f5fe4b7df03b736ad6)
