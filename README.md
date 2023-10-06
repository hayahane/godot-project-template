# Godot CPP Template
This is a godot project template using gdextension.
Configure auto type register, compile and debug.

## How to use
Follow the tutorials on godot gdextension page, compile godot-cpp.

Write your C++ code under `Source/src` folder, run
`auto_register_and_compile.py` to generate `register_types.cpp` and the script will automatically run scons to compile your C++ code.
use argument `debug` or `release` to define compile target.

The binaries will be put in fold `Assets/Binaries`. You need to mannually write gdextension file.

## Configure Debug
Open `.vscode/launch.json` and replace the godot editor path with your own one. When debug is launched, it will automatically run debug build.

## Requirements
- *Scons*: build system godot used
- *vscode*: gives you a flexible editor to write GDScript, C# and C++ code in one project.