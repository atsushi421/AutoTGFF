# AutoTGFF

## TGFFとは
- DAGをランダムに生成してくれるツール
- パラメータをユーザが指定することが出来る
- 周期的なDAG・非周期的なDAGのどちらも生成可能
- （参考）https://robertdick.org/projects/tgff/index.html

## TGFFパラメータ

### 共通パラメータ
- seed <int> : 乱数のシード値
- tg_cnt <int> : 生成するDAGの数
- task_cnt <int（基準値）><int（ばらつき）> : DAGのタスク数
- prob_periodic <fit> : DAGが周期的である確率
- prob_multi_start_nodes　<fit> : DAGに複数の開始ノードがある確率
- start_node <int（基準値）><int（ばらつき）> : 開始ノード数
- 


### original algorithm


### new algorithm
