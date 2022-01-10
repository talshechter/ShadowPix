# from global_method import *
from global_method_mesh_generator import *
from obj_file_creator import *

def run():
    heightfield = main()
    vertices, faces = generate_mesh(heightfield)
    output_file = 'output_global_method.obj'
    # print("v : ", vertices)
    # print("f : ", faces)

    create_obj_file_from_mesh(output_file, vertices, faces)
    
if __name__ == '__main__':
    run()