# WordLister

WordLister is a Python CLI tool for generating custom wordlists from text or files.

## Features

- Generate wordlists from text or input files

- Uppercase, lowercase, and mixed modes (Mixed mode generates uppercase, lowercase, and words with mixed capitalization.)

- Custom word limit

- Uses low RAM

- Output to `.txt` file

## Clone

```bash
git clone https://github.com/arch-Fddr3/WordLister.git

```

## Usage

```bash
python3 wordlister.py -i "Lucas 1990 ! @ #" -n 10000 -m -o output.txt

```

-> see Lucas.txt for result file

## Tips

For easier access to the tool:

- Make this tool executable

```bash
chmod +x wordlister.py

```

Then you can either rename the file or create a link:

- Renaming

```bash
mv wordlister.py wordlister

```

- Linking

```bash
sudo ln -s /path/of/wordlister.py /usr/local/bin/wordlister

```

