import time

start = time.process_time()

routes = []


def find_paths(node, cities, path, distance):
    path.append(node)

    if len(path) > 1:
        distance += cities[path[-2]][node]

    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print(path, distance)
        routes.append([distance, path])
        return

    for city in cities:
        if (city not in path) and (node in cities[city]):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'Cilacap': {'Purwokerto': 2, 'Kroya': 1},
        'Purwokerto': {'Cilacap': 2, 'Slawi': 4, 'Kebumen': 4, 'Kroya': 1},
        'Kroya': {'Cilacap': 1, 'Purwokerto': 1, 'Kebumen': 3},
        'Slawi': {'Purwokerto': 4, 'Brebes': 2, 'Tegal': 1},
        'Tegal': {'Slawi': 1, 'Brebes': 2, 'Pemalang': 3},
        'Brebes': {'Slawi': 2, 'Tegal': 2},
        'Kebumen': {'Purwokerto': 4, 'Kroya': 3, 'Purworejo': 3},
        'Pemalang': {'Tegal': 3, 'Pekalongan': 2},
        'Pekalongan': {'Pemalang': 2, 'Kendal': 1},
        'Kendal': {'Temanggung': 3, 'Pekalongan': 1, 'Semarang': 3},
        'Purworejo': {'Kebumen': 3, 'Magelang': 2},
        'Magelang': {'Purworejo': 2, 'Wonosobo': 3, 'Temanggung': 3, 'Boyolali': 3},
        'Wonosobo': {'Magelang': 3, 'Temanggung': 1},
        'Temanggung': {'Magelang': 3, 'Wonosobo': 1, 'Kendal': 3, 'Salatiga': 1},
        'Boyolali': {'Magelang': 3, 'Salatiga': 2, 'Solo': 2},
        'Salatiga': {'Boyolali': 2, 'Temanggung': 1, 'Semarang': 2},
        'Semarang': {'Salatiga': 2, 'Kendal': 3, 'Demak': 1},
        'Demak': {'Purwodadi': 2, 'Semarang': 1, 'Kudus': 1},
        'Solo': {'Boyolali': 2, 'Purwodadi': 3, 'Sragen': 1},
        'Purwodadi': {'Solo': 3, 'Demak': 2, 'Kudus': 2, 'Blora': 4},
        'Kudus': {'Purwodadi': 2, 'Demak': 1, 'Rembang': 3},
        'Rembang': {'Kudus': 3, 'Blora': 2},
        'Blora': {'Sragen': 4, 'Purwodadi': 4, 'Rembang': 2},
        'Sragen': {'Solo': 1, 'Blora': 4}
    }

    print("Titik Mulai: CILACAP")
    find_paths('Cilacap', cities, [], 0)
    print("\n")
    routes.sort()
    if len(routes) != 0:
        print("Rute Terpendek: %s" % routes[0])
    else:
        print("Gagal!")

    print("Time: ", time.process_time() - start)
