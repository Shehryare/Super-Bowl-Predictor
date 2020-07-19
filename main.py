#!/usr/bin/python3
from pathlib import Path
data_dir_path = Path('data')
file_names = [x.name for x in data_dir_path.glob('*') if x.is_file()]