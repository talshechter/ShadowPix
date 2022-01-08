def calculate_u_vertices_and_faces(u, vertices, faces, ver_ctr, pix_size=2.5, wall_th=0.25):
    n = len(u)
    curr_x = 0
    for i in range (n):
        curr_y = 0
        for j in range(n):
            # lower
            vertices.append((curr_x, curr_y, 0))               # ver_ctr+1          
            vertices.append((curr_x, curr_y, u[i][j]))         # ver_ctr+2
            vertices.append((curr_x+wall_th, curr_y, 0))       # ver_ctr+3
            vertices.append((curr_x+wall_th, curr_y, u[i][j])) # ver_ctr+4
            
            # upper
            curr_y += pix_size+2*wall_th
            vertices.append((curr_x, curr_y, 0))               # ver_ctr+5
            vertices.append((curr_x, curr_y, u[i][j]))         # ver_ctr+6
            vertices.append((curr_x+wall_th, curr_y, 0))       # ver_ctr+7
            vertices.append((curr_x+wall_th, curr_y, u[i][j])) # ver_ctr+8  
            
            # add 5 faces
            faces.append((ver_ctr+1, ver_ctr+2, ver_ctr+5, ver_ctr+6)) # outer face
            faces.append((ver_ctr+3, ver_ctr+4, ver_ctr+7, ver_ctr+8)) # inner face
            faces.append((ver_ctr+2, ver_ctr+4, ver_ctr+6, ver_ctr+8)) # upper face
            faces.append((ver_ctr+1, ver_ctr+2, ver_ctr+3, ver_ctr+4)) # side face
            faces.append((ver_ctr+5, ver_ctr+6, ver_ctr+7, ver_ctr+8)) # side face
            ver_ctr +=8
        curr_x += pix_size+wall_th
    return vertices, faces, ver_ctr


def calculate_v_vertices_and_faces(v, vertices, faces, ver_ctr, pix_size=2.5, wall_th=0.25):
    n = len(v)
    curr_x = 0+wall_th
    for i in range (n):
        curr_y = 0
        for j in range(n):
            # left
            vertices.append((curr_x, curr_y, 0))               # ver_ctr+1
            vertices.append((curr_x, curr_y, v[i][j]))         # ver_ctr+2
            vertices.append((curr_x, curr_y+wall_th, 0))       # ver_ctr+3
            vertices.append((curr_x, curr_y+wall_th, v[i][j])) # ver_ctr+4
            
            # right
            vertices.append((curr_x+pix_size, curr_y, 0))               # ver_ctr+5
            vertices.append((curr_x+pix_size, curr_y, v[i][j]))         # ver_ctr+6
            vertices.append((curr_x+pix_size, curr_y+wall_th, 0))       # ver_ctr+7
            vertices.append((curr_x+pix_size, curr_y+wall_th, v[i][j])) # ver_ctr+8
            
            # add 5 faces
            faces.append((ver_ctr+1, ver_ctr+2, ver_ctr+5, ver_ctr+6))
            faces.append((ver_ctr+3, ver_ctr+4, ver_ctr+7, ver_ctr+8))
            faces.append((ver_ctr+2, ver_ctr+4, ver_ctr+6, ver_ctr+8)) # upper face
            faces.append((ver_ctr+1, ver_ctr+2, ver_ctr+3, ver_ctr+4)) # side face
            faces.append((ver_ctr+5, ver_ctr+6, ver_ctr+7, ver_ctr+8)) # side face
            ver_ctr +=8
              
        curr_x += pix_size+wall_th
    return vertices, faces, ver_ctr


def calculate_r_vertices_and_faces(r, vertices, faces, ver_ctr, pix_size=2.5, wall_th=0.25):
    n = len(r)
    curr_x = 0+wall_th
    for i in range (n):
        curr_y = 0+wall_th
        for j in range(n):
            # down left
            vertices.append((curr_x, curr_y, r[i][j]))
            # down right
            vertices.append((curr_x+pix_size, curr_y, r[i][j]))
            # up left
            vertices.append((curr_x, curr_y+pix_size, r[i][j]))
            # up right
            vertices.append((curr_x+pix_size, curr_y+pix_size, r[i][j]))
            faces.append((ver_ctr+1, ver_ctr+2, ver_ctr+3, ver_ctr+4))
            ver_ctr+=4
        curr_x += pix_size+wall_th
    return vertices, faces, ver_ctr


def generate_mesh(r, u, v, pix_size=2.5, wall_th=0.25):
    vertices = []
    faces = []
    vertices_counter = 0
    vertices, faces, vertices_counter = calculate_r_vertices_and_faces(r, vertices, faces, vertices_counter, pix_size, wall_th)
    vertices, faces, vertices_counter = calculate_u_vertices_and_faces(u, vertices, faces, vertices_counter, pix_size, wall_th)
    vertices, faces, vertices_counter = calculate_v_vertices_and_faces(v, vertices, faces, vertices_counter, pix_size, wall_th)
    return vertices, faces


def test():
    r = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
    u = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
    v = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
    generate_mesh(r, u, v)  
    
       
if __name__ == '__main__':
    test()
    