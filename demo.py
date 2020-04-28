from VRP_P import VRP
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import pandas as pd
import matplotlib.pyplot as plt


def draw():
    for i, row in b_loc.iterrows():
        edgecolor = colors[1] if i in result['starts'] else colors[0]
        plt.scatter(
            row['x'], row['y'], s=750,
            facecolor='white', edgecolor=edgecolor
        )
        plt.text(
            row['x'], row['y'], row['name'],
            fontsize=15, ha='center', va='center'
        )
    for i, route in enumerate(result['routes']):
        for j in range(len(route) - 1):
            loc_start = b_loc.loc[route[j]]
            loc_end = b_loc.loc[route[j + 1]]
            pos_start = loc_start[1:3].values
            pos_end = loc_end[1:3].values
            len_percent = 60 / 100
            arrow_start = pos_start + (pos_end - pos_start) * (1 - len_percent) / 2
            arrow_d = (pos_end - pos_start) * len_percent
            plt.arrow(
                *arrow_start, *arrow_d, head_width=20, head_length=35,
                fc=colors[-i], ec=colors[-i], zorder=0,
                length_includes_head=True
            )

    plt.gca().axis('off')
    plt.savefig('routing.png')


if __name__ == '__main__':
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    b_loc = pd.read_csv('BasicLocations.csv')
    b_dist = squareform(pdist(b_loc.values[:, 1:3])).astype(int)
    '''
    有车子数量以及每辆车的限载的约束时，输入参数为 dep_starts, dep_ends, num_vehicles, vehicle_capacities。
    只给定限载的约束，这时，限制为一个配送中心，输入参数为 depot, vehicle_capacities，其中vehicle_capacities 内元素unique
    只给定车子数量，输入参数为 dep_starts, dep_ends, num_vehicles
    '''
    # Case1:车子限载和数量约束，这时候给出每一辆车的出发点starts和终点ends，以及车子限载b_capa
    # b_capa = [14, 14, 16, 16]
    # depot = 0
    # vrp = VRP(
    #     distance_matrix=b_dist, demands=b_loc['demand'], depot=depot,
    #     num_vehicles=len(b_capa),
    #     vehicle_capacities=b_capa,
    #     travel_time_limit=int(1e9),
    #     vehicle_speed=int(1e9),
    #     max_travel_distance=3000
    # )
    # vrp.solve()
    # result = vrp.result()
    # print(result['routes'])
    # print(result)
    # print('Full Load Rate:', vrp._full_load_rate())
    # draw()
    #
    # # Case2:车子数量的约束，这时候给出每一辆车的出发点starts和终点ends
    # b_capa = [14, 14, 16, 16]
    # depot = 0
    # vrp = VRP(
    #     distance_matrix=b_dist, demands=b_loc['demand'], depot=depot,
    #     num_vehicles=len(b_capa),
    #     # vehicle_capacities=b_capa,
    #     travel_time_limit=int(1e9),
    #     vehicle_speed=int(1e9),
    #     max_travel_distance=3000
    # )
    # vrp.solve()
    # result = vrp.result()
    # print(result['routes'])
    # print(result)
    # draw()
    #
    # Case3:只有限载的约束b_capa，这时，只考虑同一起始点，b_capa为载重列表，列表中数据唯一
    b_capa = [14, 16]
    depot = 0 ## 起始点为0
    vrp = VRP(
        distance_matrix=b_dist, demands=b_loc['demand'], depot=depot,
        # num_vehicles=len(b_capa),
        vehicle_capacities=b_capa,
        travel_time_limit=int(1e9),
        vehicle_speed=int(1e9),
        max_travel_distance=3000
    )
    vrp.solve()
    result = vrp.result()
    print(result['routes'])
    print(result)
    print('Full Load Rate:', vrp._full_load_rate())
    draw()

    # Case4:外卖情形  给定每个外卖员的起点starts以及商家和客户坐标点矩阵pickups_deliveries，第一列为商家地点索引
    #                 第二列为吃外卖客户的位置索引。pick_weights和weight_limits为限制条件，具体见VRP类的 __init__
    #                 当pick_weight和weight_limits同时给出时，就对于外卖员同时运输的外卖的数量或者重量上有限制。
    #                 任一不给出时，就认为外卖员神力，可以同时拿着任意数量及重量的外卖来回穿梭。
    # starts = [1, 6]
    # pickups_deliveries = [
    #     [2, 10],
    #     [4, 3],
    #     [5, 9],
    #     [7, 8],
    #     [15, 11],
    #     [13, 12],
    #     [16, 14],
    # ]
    # # print(b_dist)
    # vrp = VRP(
    #     distance_matrix=b_dist, dep_starts=starts, pickups_deliveries=pickups_deliveries,
    #     num_vehicles=len(starts),
    #     max_travel_distance=3000,
    #     pick_weights=1,
    #     # pick_capacities=[1, 1, 1, 1, 1, 1, 1]
    #     weight_limits=[3, 3]
    # )
    # vrp.solve()
    # result = vrp.result_pd()
    # # print(result['routes'])
    # print(result)
