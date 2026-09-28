name: Build Simple Tally Feeder

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: windows-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install PyInstaller
      run: pip install pyinstaller

    - name: Create EXE file (With Core Windows DLLs)
      run: |
        pyinstaller --onefile --noconsole --paths="C:\Windows\System32" app.py

    - name: Upload EXE Artifact
      uses: actions/upload-artifact@v4
      with:
        name: TallyFeeder-Single-EXE
        path: dist/app.exe
