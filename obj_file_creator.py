
def create_obj_file_from_mesh(file, vertices, faces):
    with open(file, 'w+') as f:
        for v in vertices:
            f.write("v %f %f %f\n" % (v[0], v[1], v[2]))
        for face in faces:
            f.write("f %d %d %d %d\n" % (face[0], face[1], face[2], face[3]))
    