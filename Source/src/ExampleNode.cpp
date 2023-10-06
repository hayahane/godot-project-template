#include "ExampleNode.h"
#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/variant/utility_functions.hpp>

using namespace godot;

ExampleNode::ExampleNode() 
{
    UtilityFunctions::print("Example node constructed");
}

ExampleNode::~ExampleNode()
{
    
}

void ExampleNode::_bind_methods()
{

}