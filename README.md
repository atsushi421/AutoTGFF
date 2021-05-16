# AutoTGFF

## TGFFとは
- DAGをランダムに生成してくれるツール
- パラメータをユーザが指定することが出来る
- 周期的なDAG・非周期的なDAGのどちらも生成可能
- （参考）https://robertdick.org/projects/tgff/index.html


## 使い方

### original
```
bash original_random_generate 生成するDAGの数
```
- `original_change_option.py` 内でパラメータの範囲を指定できる


## TGFFパラメータ

### 共通パラメータ
```
- seed <int>  : 乱数のシード値
- tg_cnt <int>  : 生成するDAGの数
- task_cnt <int><int>  : DAGのタスク数
- prob_periodic <fit>  : DAGが周期的である確率
- prob_multi_start_nodes <fit>  : DAGに複数の開始ノードがある確率
- start_node <int><int>  : 開始ノード数
```

### original algorithm
```
- task_degree <int><int>  : タスクへの最大入力数, タスクからの最大出力数
```

### new algorithm
```
- gen_series_parallel <bool>  : new algorithm を使用
- series_must_rejoin<bool>  : 直列鎖のサブグラフをメイングラフに強制的に結合（エンドノードが1つになる）
- series_len <int><int>  : 直列鎖の長さ
- series_wid <int><int>  : 直列鎖の幅
- series_local_xover <int>  : 直列鎖間でランダムに接続されるエッジの数
- series_global_xover <int>  : series_must_rejoin が true の場合の, 開始ノードからエンドノードに接続されるエッジの数
    - 直列鎖の長さと幅を0に設定した場合, series_global_xover で指定した数のエッジのみを持つランダムなDAGが生成される
```
