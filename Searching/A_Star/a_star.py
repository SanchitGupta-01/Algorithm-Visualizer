from GUI.visualizers.grid import *
from Searching.A_Star.node import Node


class AStarPathfinder(GridGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master,
                         lambda i=0: self.a_star_pathfinder(
                             self.get_grid_nodes().get_start_node(),
                             self.get_grid_nodes().get_goal_node()
                         ), Node, **kwargs)
        self.title = 'A* Pathfinder Algorithm'

    @staticmethod
    def a_star_pathfinder(start: Node, goal: Node) -> tuple:
        open_list = [start]
        closed_list = []

        while len(open_list) is not 0:
            current_node = open_list.pop()

            if current_node is goal:
                break

            yield current_node, current_node.get_color(), 'orange'

            neighbors = current_node.get_neighbors()

            for node in neighbors:
                if node in closed_list:
                    continue

                cost = node.g_cost  # distance b/w node and current node
                new_g = current_node.g_cost + cost
                xc, yc = node.position()
                xg, yg = goal.position()
                new_h = abs(xc - xg) + abs(yc - yg)  # Manhattan distance
                # new_h = math.sqrt((xc - xg)**2 + (yc - yg)**2)        # Euclidean distance
                new_f = new_g + new_h

                if node in open_list and new_f > node.f_cost:
                    continue
                else:
                    node.g_cost, node.h_cost, node.f_cost = new_g, new_h, new_f
                    node.set_parent(current_node)
                    open_list.append(node)
                    open_list = sorted(open_list, key=lambda i=0: i.f_cost, reverse=True)
                    yield node, node.get_color(), 'yellow'

            closed_list.append(current_node)
