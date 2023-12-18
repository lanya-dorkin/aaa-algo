import csv
from collections import deque
from heapq import heappop, heappush


class Node:
    def __init__(self, title: str, id: int) -> None:
        self.title = title
        self.id = id
        self.links = set()

    def __hash__(self) -> int:
        return self.id

    def __len__(self) -> int:
        return len(self.title)

    def __repr__(self) -> str:
        return f'{self.title}({len(self)})'

    def __lt__(self, other) -> bool:
        return self.id < other.id

    def add_links(self, *pages) -> None:
        self.links.update(pages)


def read_pages(path: str = 'simple_english_wiki_pages.csv') -> dict:
    with open(path, 'r', encoding='UTF-8') as file:
        pages = {}
        title_id_map = {}
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['page_id'])
            title = row['page_title']
            pages[id] = Node(title, id)
            title_id_map[title] = id

    return pages, title_id_map


def update_with_page_links(
        pages: dict,
        path: str = 'simple_english_wiki_pagelinks.csv'
        ) -> None:
    with open(path, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pl_from, pl_to = int(row['pl_from']), int(row['pl_to'])
            pages[pl_from].add_links(pages[pl_to])


def bfs(pages: list, start: int, finish: int) -> list:
    routes = deque([[pages[start]]])
    visited = set()
    while routes:
        cur_route = routes.popleft()
        cur_node = cur_route[-1]

        if cur_node.id == finish:
            return cur_route

        if cur_node in visited:
            continue
        visited.add(cur_node)

        routes.extend(
            [cur_route + [new_node] for new_node in cur_node.links]
        )

    raise ValueError('not found')


def route_len(route: list) -> int:
    return sum([len(node) for node in route[1:]])


def dijikstra(pages: dict, start: int, end: int) -> list:
    paths = {start: (0, None)}
    heap_queue = []
    heappush(heap_queue, (0, pages[start]))
    while heap_queue:
        cur_cost, cur_node = heappop(heap_queue)

        for node in cur_node.links:
            new_cost = cur_cost + len(node)
            prev_cost = paths.get(node.id, (None,))[0]
            if prev_cost is None or prev_cost > new_cost:
                paths[node.id] = (new_cost, cur_node)
                heappush(heap_queue, (new_cost, node))

    if end in paths:
        path = [pages[end]]
        cur_node = paths[path[-1].id][1]
        while cur_node is not None:
            path.append(cur_node)
            cur_node = paths[path[-1].id][1]

        return paths[end][0], path[::-1]

    raise ValueError('not found')


if __name__ == '__main__':
    print('loading data... wait a bit, please')
    pages, title_id_map = read_pages()
    update_with_page_links(pages)

    while True:
        start = title_id_map[input('page name where to start: ')]
        finish = title_id_map[input('page name where to finish: ')]

        # route = bfs(pages, start, finish)
        # print(' -> '.join([x.title for x in route]))

        total_cost, path = dijikstra(pages, start, finish)
        print(total_cost, ' -> '.join(map(str, path)))
