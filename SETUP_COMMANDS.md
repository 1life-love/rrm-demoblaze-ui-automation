# VS Code Setup and Test Run Guide

This guide is for setting up and running the Demoblaze UI automation project from GitHub using VS Code.

Repository:

```text
https://github.com/1life-love/rrm-demoblaze-ui-automation
```

## 1. Clone the Repository

### macOS

Open Terminal and run:

```bash
cd ~/Documents/GitHub
git clone https://github.com/1life-love/rrm-demoblaze-ui-automation.git
cd rrm-demoblaze-ui-automation
```

### Windows PowerShell

Open PowerShell and run:

```powershell
cd $HOME\Documents\GitHub
git clone https://github.com/1life-love/rrm-demoblaze-ui-automation.git
cd rrm-demoblaze-ui-automation
```

## 2. Open the Project in VS Code

Open VS Code.

Go to:

```text
File > Open Folder
```

Select the cloned folder:

```text
rrm-demoblaze-ui-automation
```

The folder should contain:

```text
requirements.txt
pytest.ini
components
pages
test_data
tests
```

## 3. Create a Virtual Environment

Open the VS Code terminal:

```text
Terminal > New Terminal
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

## 4. Select the Python Interpreter in VS Code

Press:

```text
Cmd + Shift + P
```

On Windows:

```text
Ctrl + Shift + P
```

Search for:

```text
Python: Select Interpreter
```

Choose the interpreter inside `.venv`.

macOS path usually looks like:

```text
.venv/bin/python
```

Windows path usually looks like:

```text
.venv\Scripts\python.exe
```

## 5. Install Dependencies

Run this in the VS Code terminal after activating `.venv`:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. Install Playwright Browser

```bash
python -m playwright install chromium
```

## 7. Run Tests from VS Code Terminal

Run all tests:

```bash
python -m pytest
```

Run smoke tests:

```bash
python -m pytest -m smoke
```

Run navigation tests:

```bash
python -m pytest -m navigation
```

Run checkout tests:

```bash
python -m pytest -m checkout
```

Run one file:

```bash
python -m pytest tests/ui/test_navigation.py
```

Run headed browser mode:

```bash
python -m pytest tests/ui/test_cart.py --headed
```

## 8. Run Tests Using VS Code Test Runner

Install these VS Code extensions:

```text
Python
Pylance
```

Then:

1. Open the Testing panel from the left sidebar.
2. If VS Code asks to configure tests, choose `pytest`.
3. Select the `tests` folder.
4. VS Code should discover the test cases.
5. Click the play button beside a test, file, or folder.

If tests are not discovered:

1. Confirm the selected interpreter is `.venv`.
2. Confirm dependencies are installed.
3. Run this from the terminal:

```bash
python -m pytest --collect-only
```

If collection works in terminal but not in VS Code:

1. Press `Cmd + Shift + P` on macOS or `Ctrl + Shift + P` on Windows.
2. Run `Python: Configure Tests`.
3. Choose `pytest`.
4. Choose the `tests` directory.

## 9. Expected Result

The full suite should run 11 UI tests in Chromium.

Expected summary:

```text
11 passed
```

## 10. Common Problems

### Problem: No such file or directory: requirements.txt

You are in the wrong folder.

Run:

```bash
pwd
ls
```

Make sure you are inside the folder that contains `requirements.txt`.

### Problem: No module named playwright

The virtual environment is not active or dependencies were not installed.

Run:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Problem: pytest command not found

Use:

```bash
python -m pytest
```

This is safer because it uses pytest from the active Python environment.

### Problem: Browser not installed

Run:

```bash
python -m playwright install chromium
```

## 11. Quick Command Checklist

### macOS

```bash
git clone https://github.com/1life-love/rrm-demoblaze-ui-automation.git
cd rrm-demoblaze-ui-automation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest
```

### Windows PowerShell

```powershell
git clone https://github.com/1life-love/rrm-demoblaze-ui-automation.git
cd rrm-demoblaze-ui-automation
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest
```

