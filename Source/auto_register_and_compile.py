import os
import sys
import subprocess

# todo: Add a symbol to compile for release mode or debug mode
# and give the ability to escape the auto register pass.
version = '0.1'
assembly_name = 'test'
directory = 'src'

if (len(sys.argv) > 1):
    compile_mode = sys.argv[1]
else:
    compile_mode = 'debug'

# auto register and compile script info
print('\n\n\033[33mGodot Cpp Class auto register and compile script')
print('version:',version,'©Monologist 2023\033[0m\n')
print("Assembly name:" + assembly_name)    
print('compile mode: ' + compile_mode)
compile_mode = 'template_'+compile_mode
count = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
print('Source from: ' + current_dir +'\\' + directory)
files_path = os.path.join(current_dir, directory)
cpp_path = os.path.join(current_dir,directory, 'register_types.cpp')
header_path = os.path.join(current_dir, directory, 'register_types.h')

init_fnc_name = 'initialize_'+assembly_name+'_module'
uninit_fnc_name = 'uninitialize_' + assembly_name + '_module'

# write header file
header_file = open(header_path, 'w')
header_file.write("#pragma once\n")
header_file.write("void "+ init_fnc_name+'();\n')
header_file.write("void "+uninit_fnc_name+'();')
header_file.close()


print("--------------------------------------------")
print("\033[32mBegin register classes")
print("\033[0m--------------------------------------------")
# write register_types.cpp file
file = open(cpp_path, 'w')
file.write('#include "register_types.h"\n')

for filename in os.listdir(files_path):
    if filename.endswith('.h') and filename != 'register_types.h':
        count += 1
        print("register: \033[34m" + filename + '\033[0m')
        file.write('#include "' + filename +'"\n')
 
file.write('\n') 
file.write('using namespace godot;\n\n')   
file.write('void '+init_fnc_name+'(ModuleInitializationLevel p_level)\n{\n')   
file.write('\tif (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) { return; }\n\n')

for filename in os.listdir(files_path):
    if filename.endswith('.h') and filename != 'register_types.h':
        type_name = filename.split(".")[0]
        
        file.write('\tClassDB::register_class<' + type_name +'>();\n')


file.write('}\n') 
file.write('void '+uninit_fnc_name+'(ModuleInitializationLevel p_level)\n{\n')   
file.write('\tif (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) { return; }\n\n}\n')


file.write('extern "C"\n{\n')
file.write('\tGDExtensionBool GDE_EXPORT mn_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address,\n')
file.write('\tconst GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)\n')
file.write('\t{\n'+'\t\tGDExtensionBinding::InitObject initObj(p_get_proc_address, p_library, r_initialization);\n')
file.write('\t\tinitObj.register_initializer('+init_fnc_name+');\n')
file.write('\t\tinitObj.register_terminator('+ uninit_fnc_name +');\n')
file.write('\t\tinitObj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);\n'+'\t\treturn initObj.init();\n\t}\n}')
file.close()

print("\n\033[33mFind and registered", count, 'Classes.\033[0m')
# auto compile
print("--------------------------------------------")
print("\033[32mClass info registered, ready for build")
print("\033[0m--------------------------------------------\nScons Output:")
try:
    result = subprocess.run(['scons','target='+compile_mode], cwd=current_dir)
    print("--------------------------------------------")
    if (result.returncode == 0):
        print("\033[32mCompile succeed\033[0m")
    else:
        print("\033[31mCompile failed\033[0m")
except Exception as e:
    print("Error when calling scons")
print("--------------------------------------------\n")