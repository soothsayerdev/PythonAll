def towers_of_hanoi(n, source , auxiliary, target):
    # N = numero de discos
    # source = origem, qual torre os discos estao posicionados
    # auxiliary = torre auxiliar 
    # target = destino, onde desejamos mover os discos
    if n == 1:
        print(f"Mover disco 1 da torre {source} para a torre {target}")
        return 
    
    towers_of_hanoi(n-1, source, target, auxiliary)
    print(f"Mover disco {n} da torre {source} para a torre {target}")
    towers_of_hanoi(n-1, auxiliary, source, target)


n_disks = 3
towers_of_hanoi(n_disks, "A", "B", "C")        