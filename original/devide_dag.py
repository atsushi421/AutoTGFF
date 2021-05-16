# -*- coding: utf-8 -*-


import os
import sys


args = sys.argv
num_of_dag = int(args[1])  # DAGの数を受け取る

num_fifty = 0
num_one_hundred = 0
num_two_hundred = 0


for i in range(num_of_dag):

	dag_path = './original_random_dag/original_random_' + str(i) + '.tgff'
	eps_path = './original_random_dag/original_random_' + str(i) + '.eps'
	txt_path = './original_random_dag/original_random_' + str(i) + '.txt'

	tgff_file = open(dag_path, "r")  # ファイルを開く

	num_of_node = 0

	for line in tgff_file:  # 1行ずつ読み込む

		# 空行はスキップ
		if(line == '\n'):
			continue
		
		line_list = line.split()  # 文字列の半角スペース・タブ区切りで区切ったリストを取得

		# TASKの情報の取得
		if(line_list[0] == 'TASK'):
			num_of_node += 1

	tgff_file.close()  # ファイルを閉じる


	if(num_of_node < 60):
		dag_rename_path = './original_random_dag/50/original_50_' + str(num_fifty) + '.tgff'
		eps_rename_path = './original_random_dag/50/original_50_' + str(num_fifty) + '.eps'
		txt_rename_path = './original_random_dag/50/original_50_' + str(num_fifty) + '.txt'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		os.rename(txt_path, txt_rename_path)

		num_fifty += 1


	elif(num_of_node < 110):
		dag_rename_path = './original_random_dag/100/original_100_' + str(num_one_hundred) + '.tgff'
		eps_rename_path = './original_random_dag/100/original_100_' + str(num_one_hundred) + '.eps'
		txt_rename_path = './original_random_dag/100/original_100_' + str(num_one_hundred) + '.txt'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		os.rename(txt_path, txt_rename_path)

		num_one_hundred += 1


	else:
		dag_rename_path = './original_random_dag/200/original_200_' + str(num_two_hundred) + '.tgff'
		eps_rename_path = './original_random_dag/200/original_200_' + str(num_two_hundred) + '.eps'
		txt_rename_path = './original_random_dag/200/original_200_' + str(num_two_hundred) + '.txt'
		os.rename(dag_path, dag_rename_path)
		os.rename(eps_path, eps_rename_path)
		os.rename(txt_path, txt_rename_path)

		num_two_hundred += 1