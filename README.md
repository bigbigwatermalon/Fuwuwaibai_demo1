# Fuwuwaibai_demo1
## 环境配置
pip install -r requirements.txt

## VRP_P.py
VRP模型类
参数说明
- distance_matrix:距离矩阵
- demands:列表，各配送点需求
- dep_starts:列表，货车出发点
- dep_ends:列表，货车行驶终点
- depot:整数，起始点唯一时的起始点，它的默认值为-1，当它不为-1时，dep_starts和dep_ends参数失效。
- time_limit:整数（秒） 超过这个时间则叫停算法，返回结果
- travel_time_limit:货车一趟最多行驶时间
- discharge_time:货车在送货点卸货时间
- vehicle_speed:货车行驶速度
- max_travel_distance:货车一趟最多行驶路程

## demo.py
变量与其他文件中的一致，文件中考虑了四种情况，在注释中写明。
变量说明
- b_loc:读取csv文件中的坐标
- b_dist:将b_loc中的坐标转化为距离邻接矩阵
- b_car:读取csv文件中车辆数量信息以及车载容量信息
- starts:列表，设定每一辆车子的出发点
- ends:列表，设定每一辆车子的行驶终点，这里设置其与start相同，以表示出发后回到原点。

此demo目前考虑的情况为给定车辆数量，和车载重量，以及配送中心点，根据路程最短原则来规划最佳路线。  

