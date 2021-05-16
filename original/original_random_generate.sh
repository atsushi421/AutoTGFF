#!/usr/bin/bash


for ((i=0 ; i<30 ; i++))
do
python3 original_change_option.py
python3 original_get_parameter.py
./tgff3_1.exe original

wait

rm original.vcg
mv original_generate_parameter.txt original_random_${i}.txt
mv original_random_${i}.txt ./original_random_dag/
mv original.eps original_random_${i}.eps
mv original_random_${i}.eps ./original_random_dag/
mv original.tgff original_random_${i}.tgff
mv original_random_${i}.tgff ./original_random_dag/

wait
done

python3 change_dag_name.py