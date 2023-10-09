shader_type spatial;

render_mode skip_vertex_transform;

uniform vec4 color = vec4(0.5,0.2,0.2,1);
uniform float thickness = 0.1f;

void vertex()
{
	mat4 projection_mat = PROJECTION_MATRIX;
	//PROJECTION_MATRIX = mat4(1.0);
	vec4 positionVS = MODELVIEW_MATRIX * vec4(VERTEX, 1);
	vec4 positionCS = projection_mat * positionVS;
	
	//VERTEX = positionVS.xyz;
	VERTEX = positionCS.xyz;
	POSITION = positionCS;
}


void fragment()
{
	ALBEDO = color.xyz;
}