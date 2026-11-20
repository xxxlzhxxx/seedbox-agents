"""Find a shortest walking route through a SeedBox world."""
import argparse
from collections import deque
import json
from pathlib import Path


def route(world, start, goal):
    if world["version"] != 1:
        raise ValueError("Unsupported world version")
    neighbors = {place: [] for place in world["places"]}
    for left, right in world["paths"]:
        neighbors[left].append(right)
        neighbors[right].append(left)
    if start not in neighbors or goal not in neighbors:
        raise ValueError("Unknown starting place or destination")

    previous = {start: None}
    queue = deque([start])
    while queue:
        place = queue.popleft()
        if place == goal:
            steps = []
            while place is not None:
                steps.append(world["places"][place])
                place = previous[place]
            return steps[::-1]
        for neighbor in neighbors[place]:
            if neighbor not in previous:
                previous[neighbor] = place
                queue.append(neighbor)
    raise ValueError("Destination is unreachable")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("world", type=Path)
    parser.add_argument("start")
    parser.add_argument("goal")
    args = parser.parse_args()
    try:
        world = json.loads(args.world.read_text(encoding="utf-8"))
        print(" → ".join(route(world, args.start, args.goal)))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"World error: {error}\n")
