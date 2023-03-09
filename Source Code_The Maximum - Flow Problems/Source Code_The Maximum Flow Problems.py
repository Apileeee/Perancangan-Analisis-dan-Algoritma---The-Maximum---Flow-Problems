# Nama  : Arafil Azmi
# NIM   : 21343019
# Prodi : Informatika
# Group : F

# The Maximum - Flow Problems 

def bfs(grafik, sumber, sumbu, induk):
    mengunjungi = [False] * len(grafik)
    baris = []
    baris.append(sumber)
    mengunjungi[sumber] = True

    while baris:
        u = baris.pop(0)
        for ind, val in enumerate(grafik[u]):
            if mengunjungi[ind] == False and val > 0:
                baris.append(ind)
                mengunjungi[ind] = True
                induk[ind] = u

    return True if mengunjungi[sumbu] else False

def ford_fulkerson(grafik, sumber, sumbu):
    induk = [-1] * len(grafik)
    aliran_maksimum = 0

    while bfs(grafik, sumber, sumbu, induk):
        jalur_aliran = float("Inf")
        s = sumbu
        while s != sumber:
            jalur_aliran = min(jalur_aliran, grafik[induk[s]][s])
            s = induk[s]

        aliran_maksimum += jalur_aliran

        v = sumbu
        while v != sumber:
            u = induk[v]
            grafik[u][v] -= jalur_aliran
            grafik[v][u] += jalur_aliran
            v = induk[v]

    return aliran_maksimum

grafik = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

sumber = 0
sumbu = 5

print("Maximum flow ( Aliran maksmum ):", ford_fulkerson(grafik, sumber, sumbu))

