grep -oE "mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)" text.txt > B_mults.txt

python B.py