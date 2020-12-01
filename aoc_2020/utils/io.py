def stream_lines(day):
    with open(f"../input/day_{day}.txt") as f:
        yield from f.readlines()
