shader_type spatial;
// set render modes
render_mode unshaded;
render_mode cull_front;
render_mode skip_vertex_transform;

uniform vec4 color = vec4(0,0.5,0.5,1);
uniform float thickness = 0.05;

void vertex() 
{
  	vec3 positionCS = (MODELVIEW_MATRIX * vec4(VERTEX,1)).xyz;
	vec3 normalCS = normalize(MODELVIEW_MATRIX * vec4(NORMAL,0)).xyz;
	VERTEX = positionCS + normalCS * (thickness * abs(positionCS.z));
}

void fragment() {
  //NORMAL_MAP = texture(normalmap, tex_position).xyz;
	ALBEDO = color.xyz;
}