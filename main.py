from pathlib import Path
import os
import shutil

def main():
    source = Path(__file__).resolve().parent / 'entry.png'
    destination = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination / 'entry.png')


if __name__ == '__main__':
    main()
