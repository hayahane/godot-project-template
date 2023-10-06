import os
import sys
import subprocess

#todo: Add a symbol to compile for release mode or debug mode
# and give the ability to escape the auto register pass.

if (len(sys.argv) > 1):
    compile_mode = sys.argv[1]
else:
    compile_mode = 'debug'
    
print('compile mode: ' + compile_mode)

module_name = 'test'
directory = 'src'
count = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
files_path = os.path.join(current_dir, directory)
cpp_path = os.path.join(current_dir,directory, 'register_types.cpp')
file = open(cpp_path, 'w')
file.write('#include "register_types.h"\n')

for filename in os.listdir(files_path):
    if filename.endswith('.h'):
        count += 1
        
        file.write('#include "' + filename +'"\n')
 
file.write('\n') 
file.write('using namespace godot;\n\n')   
init_fnc_name = 'initialize_'+module_name+'module'
file.write('void '+init_fnc_name+'(ModuleInitializationLevel p_level)\n{\n')   
file.write('\tif (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) { return; }\n\n')

for filename in os.listdir(files_path):
    if filename.endswith('.h') and filename != 'register_types.h':
        count += 1
        type_name = filename.split(".")[0]
        
        file.write('\tClassDB::register_class<' + type_name +'>();\n')


file.write('}\n') 
uninit_fnc_name = 'uninitialize' + module_name + '_module'
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

# auto compile
subprocess.run(['scons','target='+compile_mode], cwd=current_dir)