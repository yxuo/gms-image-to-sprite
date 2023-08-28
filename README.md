# img2spr

Convert images into sprites for Game Maker Studio

## Requirements

Mandatory:
- Python 3.10.x

Recommended
- conda or pyenv etc

## Running

If you just want to run this program do the following:

1. Install requirements:
   
   ```powershell
   pip install -r requirements.txt
   ```

2. Run the program

    ```powershell
    python -u img2spr/img2spr.py update --images "<path>" --sprite "<path>"
    ```

## Development

1. Create your env and install requirements:

    ```powershell
    conda create -n img2spr python=3.10
    conda activate img2spr
    pip install -r requirements.txt
    ```

2. Activate environment (recommended)

   ```powershell
   conda activate img2spr
   ```

3. Run the program:

   ```powershell
   python -y img2spr/img2spr.py
   ```

4. Run all tests:

   ```powershell
   python -m unittest discover
   ```

   For now it will run [`img2spr/test_img2spr.py`](img2spr/test_img2spr.py)

## TODO

v0.0.1
- [x] Create basic project setup
- [x] Simple CLI interface
- [x] Use existing sprite with existing frames to copy images onto it

v0.0.2
- [ ] App icon
- [ ] Add changelog and releases
- [ ] Unit and e2e tests

v0.0.3
- [ ] Update required frames to match selected image
