#pragma once

#include <godot_cpp/classes/node3d.hpp>

using namespace godot;

class ExampleNode : public Node3D
{
    GDCLASS(ExampleNode, Node3D)
protected:
    static void _bind_methods();

public:

    ExampleNode();
    ~ExampleNode();
};