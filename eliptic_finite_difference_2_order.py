import numpy as np

main_matrix = []
len_row_matrix = 5
len_column_matrix = 5
column = 0
batas_atas = 100
batas_bawah = 10
batas_kanan = 50
batas_kiri = 75

# membuat dimensi node matriks beda hingga

for j in range(len_row_matrix):
    row_matrix = []
    for i in range(len_column_matrix):
        row_matrix.append(0)
    #print(row_matrix)
    main_matrix.append(row_matrix)
    column+=1

print( )

# mendefinisikan kondisi batas pada matriks beda hingga

main_matrix[0][0] = (batas_atas + batas_kiri)/2
main_matrix[len_row_matrix-1][0] = (batas_kiri + batas_bawah)/2
main_matrix[0][len_row_matrix-1] = (batas_atas + batas_kanan)/2
main_matrix[len_row_matrix-1][len_column_matrix-1] = (batas_kanan+batas_bawah)/2

for i in range(1,len_column_matrix-1):
    main_matrix[0][i] = batas_atas

for i in range(1,len_column_matrix-1):
    main_matrix[len_row_matrix-1][i] = batas_bawah

for i in range(1,len_row_matrix-1):
    main_matrix[i][len_column_matrix-1] = batas_kanan

for i in range(1,len_row_matrix-1):
    main_matrix[i][0] = batas_kiri

#for i in range(len_row_matrix):
    #print(main_matrix[i])

print( )
# operasi perhitungan tiap node

# membuat matrix penyelesaian
count_matrix = []
len_matrix = (len_row_matrix-2) * (len_column_matrix-2)
#print(len_matrix)
for i in range(len_matrix):
    row_matrix_count = []
    for j in range(len_matrix):
        row_matrix_count.append(0)
    #print(row_matrix_count)
    count_matrix.append(row_matrix_count)
    column+=1

print(" ")

# operasi pada elemen i=j
for i in range(len_matrix):
    for j in range(len_matrix):
        if j == i:
            count_matrix[i][j] = 4


target_matrix = []
for t in range (len_matrix):
    target_matrix.append(0)


# operasi m-1 (bawah)
for m in range(1,len_column_matrix-1):

    for n in range(1,len_row_matrix-1):
        if main_matrix[m-1][n] != 0:
            target_matrix[(((len_column_matrix - 2) * (m-1) + n) - 1)] += main_matrix[m-1][n]
        else:
            jumlah_target_1 = 0
            count_matrix[(((len_column_matrix - 2) * (m-1) + n) - 1)] [(((len_column_matrix - 2) * (m-2)) + n)-1] = -1

#operasi m+1 (atas)
for m in range(1, len_column_matrix - 1):

    for n in range(1, len_row_matrix - 1):
        if main_matrix[m + 1][n] != 0:
            target_matrix[(((len_column_matrix - 2) * (m-1) + n) - 1)] += main_matrix[m + 1][n]
        else:
            jumlah_target_2 = 0
            count_matrix[(((len_column_matrix - 2) * (m-1) + n)-1)] [(((len_column_matrix - 2) * (m)) + n) - 1] = -1

#operasi n-1 (kiri)
for m in range(1,len_column_matrix-1):

    for n in range(1,len_row_matrix-1):
        if main_matrix[m][n-1] != 0:
            target_matrix[(((len_column_matrix - 2) * (m-1) + n) - 1)] += main_matrix[m][n-1]
        else:
            jumlah_target_1 = 0
            count_matrix[(((len_column_matrix - 2) * (m-1) + n)-1)][(((len_column_matrix - 2) * (m-1) + n)) - 2] = -1


#operasi n+1 (kanan)
for m in range(1,len_column_matrix-1):

    for n in range(1,len_row_matrix-1):
        if main_matrix[m][n+1] != 0:
            target_matrix[(((len_column_matrix - 2) * (m-1) + n) - 1)] += main_matrix[m][n+1]
        else:
            jumlah_target_1 = 0
            count_matrix[(((len_column_matrix - 2) * (m-1) + n)-1)][(((len_column_matrix - 2) * (m-1) + n))] = -1

print(" ")
for i in range(len_matrix):
        print(count_matrix[i])

print(" ")
for i in range(len_matrix):
        print(target_matrix[i])