def sort_actors():
    with open('top_actors.txt', 'r') as f:
        actors_count = []
        lines = f.readlines()
        for line in lines:
            parts = line.split(':')
            actors_count.append((parts[0].strip(), int(parts[1])))
        sorted_actors_count = sorted(actors_count, key=lambda x: x[1], reverse=True)
        return sorted_actors_count

