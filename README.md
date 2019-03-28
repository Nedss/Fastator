# Fastator
Generate your own random fasta for test !
**Version 1.1.0** (last update : 28/03/19)

## Why am I needed this script ? 

If you don't want to search by yourself your datas on famous databasse and only want to have some nucleotides to do your test.     
During my Master's degree, I developped several parsing script for DNA. Each time I need a sequence to test, but an internet connection is not always available. **That's why Fastator exists !**


## How it works ? 

### Default mode

You can use the script with default options (*Sequence length = 500, number of sequences = 1, characters by line = 60, output path = current directory*) by this way : 

```
python3 fastator.py
```

### Options 

- **-l | --length** : Set length of your sequence (should be an *integer*)
- **-n | --number** : Set number of sequences in generated fasta file (should be an *integer*)
- **-c | --character** : Set characters by line (insert *'\n'* after, should be an *integer*)
- **-o | --output** : Set output's path (you should create *target directory before*)

**Example :** 

```
python3 fastator.py -l 1000 -n 5 -c 70 -o fasta/
```

**ENJOY !**


