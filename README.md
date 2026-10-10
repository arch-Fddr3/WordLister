# WordLister
[![Downloads](https://img.shields.io/github/downloads/arch-Fddr3/WordLister/latest/total?label=Downloads&style=plastic&color=A85316)](https://github.com/arch-Fddr3/WordLister/total)
[![Latest Release](https://img.shields.io/github/v/release/arch-Fddr3/WordLister?label=Version&style=plastic&color=2ea44f)](https://github.com/arch-Fddr3/WordLister/releases/latest)
[![Top Language](https://img.shields.io/github/languages/top/arch-Fddr3/WordLister?label=Python&style=plastic&color=3776AB)](https://github.com/arch-Fddr3/WordLister)
[![Repo Size](https://img.shields.io/github/repo-size/arch-Fddr3/WordLister?label=Size&style=plastic&color=8A2BE2)](https://github.com/arch-Fddr3/WordLister)

WordLister is a lightweight Python CLI tool for generating custom wordlists from text or files.

## Features

- Generate wordlists from text 

- Uppercase, lowercase, and mixed modes (Mixed mode generates uppercase, lowercase, and words with mixed capitalization.)

- Custom word limit

- Uses low RAM

- Output to `.txt` file

- Configuration save option for better customization

## Requirements

- Python: `3.8 or newer`

## Installation

### File .zip

- extract the .zip file in the desired folder 

### From terminal

```bash
git clone https://github.com/arch-Fddr3/WordLister.git

```

## Usage

### Windows usage example

```bash
py wordlister.py -i "Lucas 1990 ! @ #" -n 10000 -m -o output.txt

```

### Linux usage example

```bash
python3 wordlister.py -i "Lucas 1990 ! @ #" -n 10000 -m -o output.txt

```

> see Lucas.txt for example result file
