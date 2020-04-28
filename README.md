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
- depot:整数，配送中心起始点。
- time_limit:整数（秒）启发式算法计算的时间，默认为2秒。
- travel_time_limit:货车一趟最多行驶时间
- discharge_time:货车在送货点卸货时间
- vehicle_speed:货车行驶速度
- max_travel_distance:货车一趟最多行驶路程
- strategy:字符串，设置使用的启发式算法，默认为AUTOMATIC
    - AUTOMATIC：让求解器选择元启发式方法
    - GREEDY_DESCENT：接受改善（降低成本）的本地搜索邻居，直到达到本地最小值。
    - GUIDED_LOCAL_SEARCH：使用引导式本地搜索来逃避本地最小值（请参阅http://en.wikipedia.org/wiki/Guided_Local_Search）；这通常是车辆路线选择中最有效的元启发式方法。
    - SIMULATED_ANNEALING：使用模拟退火来逃避局部最小值（请参阅http://en.wikipedia.org/wiki/Simulated_annealing）。
    - TABU_SEARCH：使用禁忌搜索来逃避局部最小值（请参阅http://en.wikipedia.org/wiki/Tabu_search）。
    - OBJECTIVE_TABU_SEARCH：对结果的目标值使用禁忌搜索以逃避局部最小值

## demo.py
变量与其他文件中的一致，文件中考虑了四种情况，在注释中写明。
变量说明
- b_loc:读取csv文件中的坐标
- b_dist:将b_loc中的坐标转化为距离邻接矩阵
- b_car:读取csv文件中车辆数量信息以及车载容量信息
- depot:唯一配送中心
- starts:列表，设定每一辆外卖车子的出发点
- ends:列表，设定每一辆外卖车子的行驶终点

此demo目前考虑的情况为给定车辆数量，和车载重量，以及配送中心点，根据路程最短原则来规划最佳路线。  

