
def calculate_u_ver(u, pix_size=2.5, wall_th=0.25):
    u_vertices = []
    n = len(u)
    curr_x = 0
    for i in range (n):
        curr_y = 0
        for j in range(n):
            # lower
            u_vertices.append((curr_x, curr_y, 0))
            u_vertices.append((curr_x, curr_y, u[i][j]))
            u_vertices.append((curr_x+wall_th, curr_y, 0))
            u_vertices.append((curr_x+wall_th, curr_y, u[i][j]))
            
            # upper
            curr_y += pix_size+2*wall_th
            u_vertices.append((curr_x, curr_y, 0))
            u_vertices.append((curr_x, curr_y, u[i][j]))
            u_vertices.append((curr_x+wall_th, curr_y, 0))
            u_vertices.append((curr_x+wall_th, curr_y, u[i][j]))  
        curr_x += pix_size+wall_th
    return u_vertices


def calculate_v_ver(v, pix_size=2.5, wall_th=0.25):
    v_vertices = []
    n = len(v)
    curr_x = 0+wall_th
    for i in range (n):
        curr_y = 0
        for j in range(n):
            # left
            v_vertices.append((curr_x, curr_y, 0))
            v_vertices.append((curr_x, curr_y, v[i][j]))
            v_vertices.append((curr_x, curr_y+wall_th, 0))
            v_vertices.append((curr_x, curr_y+wall_th, v[i][j]))
            
            # right
            v_vertices.append((curr_x+pix_size, curr_y, 0))
            v_vertices.append((curr_x+pix_size, curr_y, v[i][j]))
            v_vertices.append((curr_x+pix_size, curr_y+wall_th, 0))
            v_vertices.append((curr_x+pix_size, curr_y+wall_th, v[i][j]))  
        curr_x += pix_size+wall_th
    return v_vertices


def calculate_r_ver(r, pix_size=2.5, wall_th=0.25):
    r_vertices = []
    n = len(r)
    curr_x = 0+wall_th
    for i in range (n):
        curr_y = 0+wall_th
        for j in range(n):
            # down left
            r_vertices.append((curr_x, curr_y, r[i][j]))
            # down right
            r_vertices.append((curr_x+pix_size, curr_y, r[i][j]))
            # up left
            r_vertices.append((curr_x, curr_y+pix_size, r[i][j]))
            # up right
            r_vertices.append((curr_x+pix_size, curr_y+pix_size, r[i][j]))
        curr_x += pix_size+wall_th
    return r_vertices


def generate_mesh(r, u, v, pix_size=2.5, wall_th=0.25):
    vertices = []
    faces = []
    r_vertices = calculate_u_ver(r, pix_size, wall_th)
    u_vertices = calculate_u_ver(u, pix_size, wall_th)
    v_vertices = calculate_u_ver(v, pix_size, wall_th)
    return vertices, faces


def test():
    r = []
    u = []
    v = []
    r[0][0] = 1
    u[0][0] = 2
    u[1][0] = 2
    v[0][0] = 3
    v[0][1] = 3
    generate_mesh(r, u, v)  
    
       
if __name__ == '__main__':
    test()
    