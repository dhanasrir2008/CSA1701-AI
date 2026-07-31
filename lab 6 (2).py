def vacuum(world, pos):
    for i in range(len(world)):
        if world[pos] == 1:
            print("Cleaning position", pos)
            world[pos] = 0
        pos = (pos + 1) % len(world)
    print("Final State:", world)

world = [1,0]
vacuum(world, 0)
