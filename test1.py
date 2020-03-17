from VRP_P import VRP
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import pandas as pd
import matplotlib.pyplot as plt

b_loc = pd.read_csv('BasicLocations.csv')
# b_loc = pd.read_csv('new_testdata.csv')
b_dist = squareform(pdist(b_loc.values[:, 1:3])).astype(int)
print(b_dist)
b_car = pd.read_csv('BasicVehicles.csv')
# b_car = pd.read_csv('new_testdata_v.csv')
b_capa = []
starts = [0, 0, 1, 1]
ends = starts
for i, row in b_car.iterrows():
    b_capa.extend([row['capacity']] * row['number'])

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
result = {}


def test_solve_both_multiple_depots():
    vrp = VRP(
        distance_matrix=b_dist, demands=b_loc['demand'], dep_starts=starts, dep_ends=ends,
        num_vehicles=len(b_capa),
        vehicle_capacities=b_capa,
        travel_time_limit=int(1e9),
        vehicle_speed=int(1e9),
        max_travel_distance=3000
    )
    vrp.solve()
    global result
    result = vrp.result()
    print(result['routes'])

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
        for j in range(len(route)-1):
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

test_solve_both_multiple_depots()
print(result)
draw()