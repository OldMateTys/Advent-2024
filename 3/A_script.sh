grep -oE "mul\([0-9]+,[0-9]+\)" text.txt | cut -c4- > A_mults.txt

python A.py