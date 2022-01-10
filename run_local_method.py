
from local_method import *
from local_method_mesh_generator import *
from obj_file_creator import *

def run():
    r, u, v = main()
    vertices, faces = generate_mesh(r, u, v)
    output_file = 'output_local_method.obj'
    # print("v : ", vertices)
    # print("f : ", faces)

    create_obj_file_from_mesh(output_file, vertices, faces)
    
if __name__ == '__main__':
    run()