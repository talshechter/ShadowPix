def generate_mesh(heightfield, element_size=0.5):
    vertices = calculate_vertices(heightfield, element_size=0.5)
    faces = []
    n = len(heightfield)
    faces = calculate_vertical_faces(faces, n)
    faces = calculate_horizontal_faces(faces, n)
    return vertices, faces

def calculate_vertices(heightfield, element_size=0.5):
    n = len(heightfield)
    vertices = []
    curr_x = 0
    curr_y = 0
    for i in range (n):
        for j in range(n):
            curr_z = heightfield[i][j]
            # add 4 points of curr element
            vertices.append((curr_x, curr_y, curr_z))                           # 1 top left
            vertices.append((curr_x+element_size, curr_y, curr_z))              # 2 top right
            vertices.append((curr_x, curr_y+element_size, curr_z))              # 3 bottom left
            vertices.append((curr_x+element_size, curr_y+element_size, curr_z)) # 4 bottom right
            curr_y += element_size
        curr_x += element_size
        curr_y = 0
    return vertices

def calculate_horizontal_faces(faces, n):
    # vertices indices
    curr_top = 2
    curr_bottom = 4
    next_top = curr_top + (4*n-1)
    next_bottom = curr_bottom + (4*n-1)
    for i in range (n-1):
        for j in range(n):
            faces.append((curr_top, curr_bottom, next_top, next_bottom))
            curr_top, curr_bottom, next_top, next_bottom = move_to_next_vertical_element(curr_top, curr_bottom, next_top, next_bottom)
        curr_top, curr_bottom, next_top, next_bottom = move_to_next_vertical_element(curr_top, curr_bottom, next_top, next_bottom)
    return faces

def calculate_vertical_faces(faces, n):
    # vertices indices
    curr_left = 3
    curr_right = 4
    next_left = 5
    next_right = 6
    for i in range (n):
        for j in range(n-1):
            faces.append((curr_left, curr_right, next_left, next_right))
            curr_left, curr_right, next_left, next_right = move_to_next_vertical_element(curr_left, curr_right, next_left, next_right)
        curr_left, curr_right, next_left, next_right = move_to_next_vertical_element(curr_left, curr_right, next_left, next_right)           
    return faces

# helper method
def move_to_next_vertical_element(a, b, c, d):
    a+=4
    b+=4
    c+=4
    d+=4
    return a, b, c, d

def test():
    heightfield = [[1, 2], [3, 4]]
    vertices, faces = generate_mesh(heightfield)  
    print("v: ", vertices)
    print("f: ", faces)

    print("Vertices should be: [(0, 0, 1), (0.5, 0, 1), (0, 0.5, 1), (0.5, 0.5, 1), (0, 0.5, 2), (0.5, 0.5, 2), (0, 1.0, 2), (0.5, 1.0, 2), (0.5, 0, 3), (1.0, 0, 3), (0.5, 0.5, 3), (1.0, 0.5, 3), (0.5, 0.5, 4), (1.0, 0.5, 4), (0.5, 1.0, 4), (1.0, 1.0, 4)]")  
    print("Faces should be: [(3, 4, 5, 6), (11, 12, 13, 14), (2, 4, 9, 11), (6, 8, 13, 15)]")  
         
if __name__ == '__main__':
    test()