import numpy as np
import os

def generate_mesh(heightfield, file_name):
    vertices = create_vertices(heightfield)
    faces = create_faces(heightfield)
    create_obj_file_from_mesh(file_name, vertices, faces)
    return vertices, faces

def create_vertices(heightfield):
    # init
    n, m = heightfield.shape # n = rows number, m = cols number
    vertices = np.zeros([n, m, 4, 3])
    indexes = np.arange(0, m, dtype=np.uint32)
    
    # assign x values
    vertices[:, :, 0, 0] =  indexes[np.newaxis, :]
    vertices[:, :, 1, 0] = vertices[:, :, 0, 0]
    vertices[:, :, 2, 0] = vertices[:, :, 0, 0] + 1
    vertices[:, :, 3, 0] = vertices[:, :, 2, 0]

    # assign y values
    vertices[:, :, 0, 2] = indexes[:, np.newaxis]
    vertices[:, :, 3, 2] = vertices[:, :, 0, 2]
    vertices[:, :, 1, 2] = vertices[:, :, 0, 2] + 1
    vertices[:, :, 2, 2] = vertices[:, :, 1, 2]
    
    # assign z values from heightfield
    vertices[:, :, :, 1] = heightfield[:, :, np.newaxis]
    
    vertices = convert_to_triangles(vertices)
    return vertices

def create_faces(heightfield):
    # init
    n, m = heightfield.shape # n = rows number, m = cols number
    faces = np.zeros([n, m, 2, 3], dtype=np.uint32)
    indexes = np.arange(0, m, dtype=np.uint32)
    
    # calculate faces
    vertices_of_faces_type1 = [indexes * 4, indexes * 4 + 1, indexes * 4 + 2]
    vertices_of_faces_type1 = np.array(vertices_of_faces_type1)
    faces[:, :, 0, :] = np.transpose(vertices_of_faces_type1)[np.newaxis, :, :]
    
    vertices_of_faces_type2 = [indexes * 4, indexes * 4 + 2, indexes * 4 + 3]
    vertices_of_faces_type2 = np.array(vertices_of_faces_type2)
    faces[:, :, 1, :] = np.transpose(vertices_of_faces_type2)[np.newaxis, :, :]
    
    faces += (indexes * m * 4)[:, np.newaxis, np.newaxis, np.newaxis]
    faces = convert_to_triangles(faces)
    faces += 1
    
    return faces

def convert_to_triangles(np_array):
    np_array.shape = (np_array.size // 3, 3)
    return np_array

def create_obj_file_from_mesh(file, vertices, faces):
    with open(file, 'w+') as f:
        for v in vertices:
            f.write("v %f %f %f\n" % (v[0], v[1], v[2]))
        for face in faces:
            f.write("f %d %d %d\n" % (face[0], face[1], face[2]))
    print("Created", file)


def test():
    heightfield = [[1, 2], [3, 4]]
    heightfield = np.array(heightfield)
    vertices, faces = generate_mesh(heightfield, "test.obj")  
    print("v: ", vertices)
    print("f: ", faces)
         
if __name__ == '__main__':
    test()