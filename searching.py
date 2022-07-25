# -*- coding:utf-8 -*-


# BFS Search
from collections import deque


def breadth_first_search(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)


def depth_first_search(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.pop()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)


if __name__ == '__main__':
    graph = {
        'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
        'Zerind': ['Oradea', 'Arad'],
        'Oradea': ['Sibiu', 'Zerind'],
        'Timisoara': ['Lugoj', 'Arad'],
        'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Oradea', 'Arad'],
        'Lugoj': ['Mehadia', 'Timisoara'],
        'Rimnicu Vilcea': ['Pitesti', 'Craiova', 'Sibiu'],
        'Mehadia': ['Drobeta', 'Lugoj'],
        'Fagaras': ['Bucharest', 'Sibiu'],
        'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
        'Bucharest': ['Urziceni', 'Giurgiu', 'Fagaras', 'Pitesti'],
        'Craiova': ['Pitesti', 'Rimnicu Vilcea', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Neamt': ['Iasi']
    }
    # print(find_shortest_path(graph, 'Arad', 'Bucharest'))
    print(breadth_first_search(graph, 'Oradea', 'Eforie'))
    print(depth_first_search(graph, 'Oradea', 'Eforie'))
    # print(breadth_first_search(graph, 'Neamt', 'Arad'))
    # print(depth_first_search(graph, 'Neamt', 'Arad'))
