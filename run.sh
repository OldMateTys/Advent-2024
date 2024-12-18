cd 1
start=$(date '+%s%N')
python 1st.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 1b - $(( (end - start) / 1000000))ms"

cd ../2
start=$(date '+%s%N')
python 2nd.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 2b - $(( (end - start) / 1000000))ms"

cd ../3
start=$(date '+%s%N')
bash A_script.sh > /dev/null
end=$(date '+%s%N')
echo "Time: Day 3a - $(( (end - start) / 1000000))ms"

start=$(date '+%s%N')
bash B_script.sh > /dev/null
end=$(date '+%s%N')
echo "Time: Day 3b - $(( (end - start) / 1000000))ms"

cd ../4
start=$(date '+%s%N')
python A.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 4a - $(( (end - start) / 1000000))ms"

start=$(date '+%s%N')
python B.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 4b - $(( (end - start) / 1000000))ms"

cd ../5
start=$(date '+%s%N')
python A.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 5a - $(( (end - start) / 1000000))ms"

start=$(date '+%s%N')
python B.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 5b - $(( (end - start) / 1000000))ms"

cd ../6
start=$(date '+%s%N')
python A.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 6a - $(( (end - start) / 1000000))ms"

cd ../6
start=$(date '+%s%N')
python B.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 6b - $(( (end - start) / 1000000))ms"

cd ../7
start=$(date '+%s%N')
python 7th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 7b - $(( (end - start) / 1000000))ms"

cd ../8
start=$(date '+%s%N')
python 8th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 8b - $(( (end - start) / 1000000))ms"

cd ../9
start=$(date '+%s%N')
python 9th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 9b - $(( (end - start) / 1000000))ms"

cd ../10
start=$(date '+%s%N')
python 10th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 10b - $(( (end - start) / 1000000))ms"

cd ../11
start=$(date '+%s%N')
python 11th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 11b - $(( (end - start) / 1000000))ms"

cd ../12
start=$(date '+%s%N')
python 12th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 12b - $(( (end - start) / 1000000))ms"

cd ../13
start=$(date '+%s%N')
python 13th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 13b - $(( (end - start) / 1000000))ms"


echo "Skipped: Day 14"

cd ../15
start=$(date '+%s%N')
python 15th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 15b - $(( (end - start) / 1000000))ms"

cd ../16
start=$(date '+%s%N')
python 16th.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 16b - $((($end - $start) / 1000000))ms"

cd ../17
start=$(date '+%s%N')
python A.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 17a - $((($end - $start) / 1000000))ms"

start=$(date '+%s%N')
python B.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 17b - $((($end - $start) / 1000000))ms"

cd ../18
start=$(date '+%s%N')
python A.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 18a - $((($end - $start) / 1000000))ms"

start=$(date '+%s%N')
python B.py > /dev/null
end=$(date '+%s%N')
echo "Time: Day 18b - $((($end - $start) / 1000000))ms"