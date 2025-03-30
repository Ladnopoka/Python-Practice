from collections import deque


def dfs(graph):
    start_node = 'A'
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        current_node = queue.popleft()

        print(current_node, end= ' ')

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print(dfs(graph))

if __name__ == "__main__":
    main()