shader_type spatial;

render_mode diffuse_burley, specular_schlick_ggx;

uniform float distortion_size = 0.4;
uniform sampler2D glass;
uniform sampler2D screen_texture : hint_screen_texture,repeat_disable,filter_linear;

float fresnel(float amount, vec3 normal, vec3 view)
{
	return pow((1.0 - clamp(dot(normalize(normal), normalize(view)), 0.0, 1.0 )), amount);
}

void fragment() {
	
	vec2 d = texture(glass, UV).xy - vec2(0.5);
	ALBEDO = textureLod(screen_texture, SCREEN_UV + d * distortion_size,0).rgb;
	//ALBEDO += fresnel(0.1, NORMAL, VIEW);
}