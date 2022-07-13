init python:
    renpy.register_shader("witchhouse.mask", variables="""
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 color0 = texture2D(tex0, v_tex_coord.st, u_lod_bias);
        vec4 color1 = texture2D(tex1, v_tex_coord.st, u_lod_bias);

        gl_FragColor = mix(vec4(0.0), color1, color0.r);
    """) 



    renpy.register_shader("witchhouse.swirl", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_time;
        uniform vec2 u_resolution;
        uniform float u_whirl_angle;
        uniform float u_whirl_radius;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_250="""
        float effectRadius = u_whirl_radius;
        float effectAngle = u_whirl_angle * 3.14;
        
        vec2 center = vec2(.5, .5);
        
        vec2 uv = v_tex_coord - center;
        
        float len = length(uv * vec2(u_resolution.x / u_resolution.y, 1.));
        float angle = atan(uv.y, uv.x) + effectAngle * smoothstep(effectRadius, 0.0, len);
        float radius = length(uv);

        gl_FragColor = texture2D(tex0, vec2(radius * cos(angle), radius * sin(angle)) + center);
    """)



    renpy.register_shader("witchhouse.duplicate", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform float u_time;
        uniform float u_speed;
    """, vertex_300 = """
        v_tex_coord = a_tex_coord;
    """, fragment_300 = """
        vec2 coord = vec2(v_tex_coord.x, fract(v_tex_coord.y + fract(u_time * u_speed)));
        gl_FragColor = texture2D(tex0, coord);
    """) 


    
    renpy.register_shader("witchhouse.matrix", variables="""
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_resolution; 
        uniform vec2 u_mouse;
        uniform float u_time;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        const int ITERATIONS = 40;   //use less value if you need more performance
        const float SPEED = 1.;

        const float STRIP_CHARS_MIN =  7.;
        const float STRIP_CHARS_MAX = 40.;
        const float STRIP_CHAR_HEIGHT = 0.15;
        const float STRIP_CHAR_WIDTH = 0.10;
        const float ZCELL_SIZE = 1. * (STRIP_CHAR_HEIGHT * STRIP_CHARS_MAX);  //the multiplier can't be less than 1.
        const float XYCELL_SIZE = 12. * STRIP_CHAR_WIDTH;  //the multiplier can't be less than 1.

        const int BLOCK_SIZE = 10;  //in cells
        const int BLOCK_GAP = 2;    //in cells

        const float WALK_SPEED = 1. * XYCELL_SIZE;
        const float BLOCKS_BEFORE_TURN = 3.;


        const float PI = 3.14159265359;


        //        ----  random  ----

        float hash(float v) {
            return fract(sin(v)*43758.5453123);
        }

        float hash(vec2 v) {
            return hash(dot(v, vec2(5.3983, 5.4427)));
        }

        vec2 hash2(vec2 v)
        {
            v = vec2(v * mat2(127.1, 311.7,  269.5, 183.3));
	        return fract(sin(v)*43758.5453123);
        }

        vec4 hash4(vec2 v)
        {
            vec4 p = vec4(v * mat4x2( 127.1, 311.7,
                                      269.5, 183.3,
                                      113.5, 271.9,
                                      246.1, 124.6 ));
            return fract(sin(p)*43758.5453123);
        }

        vec4 hash4(vec3 v)
        {
            vec4 p = vec4(v * mat4x3( 127.1, 311.7, 74.7,
                                      269.5, 183.3, 246.1,
                                      113.5, 271.9, 124.6,
                                      271.9, 269.5, 311.7 ) );
            return fract(sin(p)*43758.5453123);
        }


        //        ----  symbols  ----
        //  Slightly modified version of "runes" by FabriceNeyret2 -  https://www.shadertoy.com/view/4ltyDM
        //  Which is based on "runes" by otaviogood -  https://shadertoy.com/view/MsXSRn

        float rune_line(vec2 p, vec2 a, vec2 b) {   // from https://www.shadertoy.com/view/4dcfW8
            p -= a, b -= a;
	        float h = clamp(dot(p, b) / dot(b, b), 0., 1.);   // proj coord on line
	        return length(p - b * h);                         // dist to segment
        }

        float rune(vec2 U, vec2 seed, float highlight)
        {
	        float d = 1e5;
	        for (int i = 0; i < 4; i++)	// number of strokes
	        {
                vec4 pos = hash4(seed);
		        seed += 1.;

		        // each rune touches the edge of its box on all 4 sides
		        if (i == 0) pos.y = .0;
		        if (i == 1) pos.x = .999;
		        if (i == 2) pos.x = .0;
		        if (i == 3) pos.y = .999;
		        // snap the random line endpoints to a grid 2x3
		        vec4 snaps = vec4(2, 3, 2, 3);
		        pos = ( floor(pos * snaps) + .5) / snaps;

		        if (pos.xy != pos.zw)  //filter out single points (when start and end are the same)
		            d = min(d, rune_line(U, pos.xy, pos.zw + .001) ); // closest line
	        }
	    return smoothstep(0.1, 0., d) + highlight*smoothstep(0.4, 0., d);
        }

        float random_char(vec2 outer, vec2 inner, float highlight) {
            vec2 seed = vec2(dot(outer, vec2(269.5, 183.3)), dot(outer, vec2(113.5, 271.9)));
            return rune(inner, seed, highlight);
        }


        //        ----  digital rain  ----

        // xy - horizontal, z - vertical
        vec3 rain(vec3 ro3, vec3 rd3, float time) {
            vec4 result = vec4(0.);

            // normalized 2d projection
            vec2 ro2 = vec2(ro3);
            vec2 rd2 = normalize(vec2(rd3));

            // we use formulas `ro3 + rd3 * t3` and `ro2 + rd2 * t2`, `t3_to_t2` is a multiplier to convert t3 to t2
            bool prefer_dx = abs(rd2.x) > abs(rd2.y);
            float t3_to_t2 = prefer_dx ? rd3.x / rd2.x : rd3.y / rd2.y;

            // at first, horizontal space (xy) is divided into cells (which are columns in 3D)
            // then each xy-cell is divided into vertical cells (along z) - each of these cells contains one raindrop

            ivec3 cell_side = ivec3(step(0., rd3));      //for positive rd.x use cell side with higher x (1) as the next side, for negative - with lower x (0), the same for y and z
            ivec3 cell_shift = ivec3(sign(rd3));         //shift to move to the next cell

            //  move through xy-cells in the ray direction
            float t2 = 0.;  // the ray formula is: ro2 + rd2 * t2, where t2 is positive as the ray has a direction.
            ivec2 next_cell = ivec2(floor(ro2/XYCELL_SIZE));  //first cell index where ray origin is located
            for (int i=0; i<ITERATIONS; i++) {
                ivec2 cell = next_cell;  //save cell value before changing
                float t2s = t2;          //and t

                //  find the intersection with the nearest side of the current xy-cell (since we know the direction, we only need to check one vertical side and one horizontal side)
                vec2 side = vec2(next_cell + cell_side.xy) * XYCELL_SIZE;  //side.x is x coord of the y-axis side, side.y - y of the x-axis side
                vec2 t2_side = (side - ro2) / rd2;  // t2_side.x and t2_side.y are two candidates for the next value of t2, we need the nearest
                if (t2_side.x < t2_side.y) {
                    t2 = t2_side.x;
                    next_cell.x += cell_shift.x;  //cross through the y-axis side
                } else {
                    t2 = t2_side.y;
                    next_cell.y += cell_shift.y;  //cross through the x-axis side
                }
                //now t2 is the value of the end point in the current cell (and the same point is the start value in the next cell)

                //  gap cells
                vec2 cell_in_block = fract(vec2(cell) / float(BLOCK_SIZE));
                float gap = float(BLOCK_GAP) / float(BLOCK_SIZE);
                if (cell_in_block.x < gap || cell_in_block.y < gap || (cell_in_block.x < (gap+0.1) && cell_in_block.y < (gap+0.1))) {
                    continue;
                }

                //  return to 3d - we have start and end points of the ray segment inside the column (t3s and t3e)
                float t3s = t2s / t3_to_t2;

                //  move through z-cells of the current column in the ray direction (don't need much to check, two nearest cells are enough)
                float pos_z = ro3.z + rd3.z * t3s;
                float xycell_hash = hash(vec2(cell));
                float z_shift = xycell_hash*11. - time * (0.5 + xycell_hash * 1.0 + xycell_hash * xycell_hash * 1.0 + pow(xycell_hash, 16.) * 3.0);  //a different z shift for each xy column
                float char_z_shift = floor(z_shift / STRIP_CHAR_HEIGHT);
                z_shift = char_z_shift * STRIP_CHAR_HEIGHT;
                int zcell = int(floor((pos_z - z_shift)/ZCELL_SIZE));  //z-cell index
                for (int j=0; j<2; j++) {  //2 iterations is enough if camera doesn't look much up or down
                    //  calcaulate coordinates of the target (raindrop)
                    vec4 cell_hash = hash4(vec3(ivec3(cell, zcell)));
                    vec4 cell_hash2 = fract(cell_hash * vec4(127.1, 311.7, 271.9, 124.6));

                    float chars_count = cell_hash.w * (STRIP_CHARS_MAX - STRIP_CHARS_MIN) + STRIP_CHARS_MIN;
                    float target_length = chars_count * STRIP_CHAR_HEIGHT;
                    float target_rad = STRIP_CHAR_WIDTH / 2.;
                    float target_z = (float(zcell)*ZCELL_SIZE + z_shift) + cell_hash.z * (ZCELL_SIZE - target_length);
                    vec2 target = vec2(cell) * XYCELL_SIZE + target_rad + cell_hash.xy * (XYCELL_SIZE - target_rad*2.);

                    //  We have a line segment (t0,t). Now calculate the distance between line segment and cell target (it's easier in 2d)
                    vec2 s = target - ro2;
                    float tmin = dot(s, rd2);  //tmin - point with minimal distance to target
                    if (tmin >= t2s && tmin <= t2) {
                        float u = s.x * rd2.y - s.y * rd2.x;  //horizontal coord in the matrix strip
                        if (abs(u) < target_rad) {
                            u = (u/target_rad + 1.) / 2.;
                            float z = ro3.z + rd3.z * tmin/t3_to_t2;
                            float v = (z - target_z) / target_length;  //vertical coord in the matrix strip
                            if (v >= 0.0 && v < 1.0) {
                                float c = floor(v * chars_count);  //symbol index relative to the start of the strip, with addition of char_z_shift it becomes an index relative to the whole cell
                                float q = fract(v * chars_count);
                                vec2 char_hash = hash2(vec2(c+char_z_shift, cell_hash2.x));
                                if (char_hash.x >= 0.1 || c == 0.) {  //10% of missed symbols
                                    float time_factor = floor(c == 0. ? time*5.0 :  //first symbol is changed fast
                                        time*(1.0*cell_hash2.z +   //strips are changed sometime with different speed
                                            cell_hash2.w*cell_hash2.w*4.*pow(char_hash.y, 4.)));  //some symbols in some strips are changed relatively often
                                    float a = random_char(vec2(char_hash.x, time_factor), vec2(u,q), max(1., 3. - c/2.)*0.2);  //alpha
                                    a *= clamp((chars_count - 0.5 - c) / 2., 0., 1.);  //tail fade
                                    if (a > 0.) {
                                        float attenuation = 1. + pow(0.06*tmin/t3_to_t2, 2.);
                                        vec3 col = (c == 0. ? vec3(0.67, 1.0, 0.82) : vec3(0.25, 0.80, 0.40)) / attenuation;
                                        float a1 = result.a;
                                        result.a = a1 + (1. - a1) * a;
                                        result.xyz = (result.xyz * a1 + col * (1. - a1) * a) / result.a;
                                        if (result.a > 0.98)  return result.xyz;
                                    }
                                }
                            }
                        }
                    }
                    // not found in this cell - go to next vertical cell
                    zcell += cell_shift.z;
                }
                // go to next horizontal cell
            }

            return result.xyz * result.a;
        }


        //        ----  main, camera  ----

        vec2 rotate(vec2 v, float a) {
            float s = sin(a);
	        float c = cos(a);
            mat2 m = mat2(c, -s, s, c);
            return m * v;
        }

        vec3 rotateX(vec3 v, float a) {
            float s = sin(a);
            float c = cos(a);
            return mat3(1.,0.,0.,0.,c,-s,0.,s,c) * v;
        }

        vec3 rotateY(vec3 v, float a) {
            float s = sin(a);
            float c = cos(a);
            return mat3(c,0.,-s,0.,1.,0.,s,0.,c) * v;
        }

        vec3 rotateZ(vec3 v, float a) {
            float s = sin(a);
            float c = cos(a);
            return mat3(c,-s,0.,s,c,0.,0.,0.,1.) * v;
        }

        float smoothstep1(float x) {
            return smoothstep(0., 1., x);
        }
    """, fragment_300="""
        if (STRIP_CHAR_WIDTH > XYCELL_SIZE || STRIP_CHAR_HEIGHT * STRIP_CHARS_MAX > ZCELL_SIZE) {
            // error
            gl_FragColor = vec4(1., 0., 0., 1.);
            return;
        }

	    vec2 uv = v_tex_coord * 2. - u_resolution.xy / u_resolution.y;

        float time = u_time * SPEED;

        const float turn_rad = 0.25 / BLOCKS_BEFORE_TURN;   //0 .. 0.5
        const float turn_abs_time = (PI/2.*turn_rad) * 1.5;  //multiplier different than 1 means a slow down on turns
        const float turn_time = turn_abs_time / (1. - 2.*turn_rad + turn_abs_time);  //0..1, but should be <= 0.5

        float level1_size = float(BLOCK_SIZE) * BLOCKS_BEFORE_TURN * XYCELL_SIZE;
        float level2_size = 4. * level1_size;
        float gap_size = float(BLOCK_GAP) * XYCELL_SIZE;

        vec3 ro = vec3(gap_size/2., gap_size/2., 0.);
        vec3 rd = vec3(uv.x, 2.0, uv.y);

        float tq = fract(time / (level2_size*4.) * WALK_SPEED);  //the whole cycle time counter
        float t8 = fract(tq*4.);  //time counter while walking on one of the four big sides
        float t1 = fract(t8*8.);  //time counter while walking on one of the eight sides of the big side

        vec2 prev;
        vec2 dir;
        if (tq < 0.25) {
            prev = vec2(0.,0.);
            dir = vec2(0.,1.);
        } else if (tq < 0.5) {
            prev = vec2(0.,1.);
            dir = vec2(1.,0.);
        } else if (tq < 0.75) {
            prev = vec2(1.,1.);
            dir = vec2(0.,-1.);
        } else {
            prev = vec2(1.,0.);
            dir = vec2(-1.,0.);
        }
        float angle = floor(tq * 4.);  //0..4 wich means 0..2*PI

        prev *= 4.;

        const float first_turn_look_angle = 0.4;
        const float second_turn_drift_angle = 0.5;
        const float fifth_turn_drift_angle = 0.25;

        vec2 turn;
        float turn_sign = 0.;
        vec2 dirL = rotate(dir, -PI/2.);
        vec2 dirR = -dirL;
        float up_down = 0.;
        float rotate_on_turns = 1.;
        float roll_on_turns = 1.;
        float add_angel = 0.;
        if (t8 < 0.125) {
            turn = dirL;
            //dir = dir;
            turn_sign = -1.;
            angle -= first_turn_look_angle * (max(0., t1 - (1. - turn_time*2.)) / turn_time - max(0., t1 - (1. - turn_time)) / turn_time * 2.5);
            roll_on_turns = 0.;
        } else if (t8 < 0.250) {
            prev += dir;
            turn = dir;
            dir = dirL;
            angle -= 1.;
            turn_sign = 1.;
            add_angel += first_turn_look_angle*0.5 + (-first_turn_look_angle*0.5+1.0+second_turn_drift_angle)*t1;
            rotate_on_turns = 0.;
            roll_on_turns = 0.;
        } else if (t8 < 0.375) {
            prev += dir + dirL;
            turn = dirR;
            //dir = dir;
            turn_sign = 1.;
            add_angel += second_turn_drift_angle*sqrt(1.-t1);
            //roll_on_turns = 0.;
        } else if (t8 < 0.5) {
            prev += dir + dir + dirL;
            turn = dirR;
            dir = dirR;
            angle += 1.;
            turn_sign = 0.;
            up_down = sin(t1*PI) * 0.37;
        } else if (t8 < 0.625) {
            prev += dir + dir;
            turn = dir;
            dir = dirR;
            angle += 1.;
            turn_sign = -1.;
            up_down = sin(-min(1., t1/(1.-turn_time))*PI) * 0.37;
        } else if (t8 < 0.750) {
            prev += dir + dir + dirR;
            turn = dirL;
            //dir = dir;
            turn_sign = -1.;
            add_angel -= (fifth_turn_drift_angle + 1.) * smoothstep1(t1);
            rotate_on_turns = 0.;
            roll_on_turns = 0.;
        } else if (t8 < 0.875) {
            prev += dir + dir + dir + dirR;
            turn = dir;
            dir = dirL;
            angle -= 1.;
            turn_sign = 1.;
            add_angel -= fifth_turn_drift_angle - smoothstep1(t1) * (fifth_turn_drift_angle * 2. + 1.);
            rotate_on_turns = 0.;
            roll_on_turns = 0.;
        } else {
            prev += dir + dir + dir;
            turn = dirR;
            //dir = dir;
            turn_sign = 1.;
            angle += fifth_turn_drift_angle * (1.5*min(1., (1.-t1)/turn_time) - 0.5*smoothstep1(1. - min(1.,t1/(1.-turn_time))));
        }

        if (u_mouse.x > 10. || u_mouse.y > 10.) {
            vec2 mouse = u_mouse.xy / u_resolution.xy * 2. - 1.;
            up_down = -0.7 * mouse.y;
            angle += mouse.x;
            rotate_on_turns = 1.;
            roll_on_turns = 0.;
        } else {
            angle += add_angel;
        }

        rd = rotateX(rd, up_down);

        vec2 p;
        if (turn_sign == 0.) {
            //  move forward
            p = prev + dir * (turn_rad + 1. * t1);
        }
        else if (t1 > (1. - turn_time)) {
            //  turn
            float tr = (t1 - (1. - turn_time)) / turn_time;
            vec2 c = prev + dir * (1. - turn_rad) + turn * turn_rad;
            p = c + turn_rad * rotate(dir, (tr - 1.) * turn_sign * PI/2.);
            angle += tr * turn_sign * rotate_on_turns;
            rd = rotateY(rd, sin(tr*turn_sign*PI) * 0.2 * roll_on_turns);  //roll
        }  else  {
            //  move forward
            t1 /= (1. - turn_time);
            p = prev + dir * (turn_rad + (1. - turn_rad*2.) * t1);
        }

        rd = rotateZ(rd, angle * PI/2.);
        ro.xy += level1_size * p;

        ro += rd * 0.2;
        rd = normalize(rd);

        vec3 col = rain(ro, rd, time);

        gl_FragColor = vec4(col, 1.);
    """) 



    renpy.register_shader("witchhouse.oldcinema", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_time;
        uniform vec2 u_resolution; 
        uniform vec3 u_mouse;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        
        float rand(vec2 co){
            return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
        }

        float rand(float c){
	        return rand(vec2(c,1.0));
        }

        float randomLine(float seed, vec2 uv){
	        float b = 0.01 * rand(seed);
	        float a = rand(seed+1.0);
	        float c = rand(seed+2.0) - 0.5;
	        float mu = rand(seed+3.0);
	
	        float l = 1.0;
	
	        if ( mu > 0.2)
		        l = pow(  abs(a * uv.x + b * uv.y + c ), 1.0/8.0 );
	        else
		        l = 2.0 - pow( abs(a * uv.x + b * uv.y + c), 1.0/8.0 );				
	
	        return mix(0.5, 1.0, l);
        }

        // Generate some blotches.
        float randomBlotch(float seed, vec2 uv, vec2 u_resolution){
	        float x = rand(seed);
	        float y = rand(seed+1.0);
	        float s = 0.01 * rand(seed+2.0);
	
	        vec2 p = vec2(x,y) - uv;
	        p.x *= u_resolution.x / u_resolution.y;
	        float a = atan(p.y,p.x);
	        float v = 1.0;
	        float ss = s*s * (sin(6.2831*a*x)*0.1 + 1.0);
	
	        if ( dot(p,p) < ss ) v = 0.2;
	        else
		        v = pow(dot(p,p) - ss, 1.0/16.0);
	
	        return mix(0.3 + 0.2 * (1.0 - (s / 0.02)), 1.0, v);
        }

    
    """, fragment_250="""
        
        #define BLACK_AND_WHITE
        #define LINES_AND_FLICKER
        #define BLOTCHES
        #define GRAIN

        #define FREQUENCY 15.0 

        vec2 uv = v_tex_coord;
	
	    if ( u_mouse.z < 0.9 ){		
		    // Set frequency of global effect to 15 variations per second
		    float t = float(int(u_time * FREQUENCY));
		
		    // Get some image movement
		    vec2 suv = uv + 0.002 * vec2( rand(t), rand(t + 23.0));
		
		    // Get the image
		    vec3 image = texture2D(tex0, vec2(suv.x, suv.y) ).xyz;
		
		    #ifdef BLACK_AND_WHITE
		    // Convert it to B/W
		    float luma = dot( vec3(0.2126, 0.7152, 0.0722), image );
		    vec3 oldImage = luma * vec3(0.7, 0.7, 0.7);
		    #else
		    vec3 oldImage = image;
		    #endif
		
		    // Create a time-varying vignetting effect
		    float vI = 16.0 * (uv.x * (1.0-uv.x) * uv.y * (1.0-uv.y));
		    vI *= mix( 0.7, 1.0, rand(t + 0.5));
		
		    // Add additive flicker
		    vI += 1.0 + 0.4 * rand(t+8.);
		
		    // Add a fixed vignetting (independent of the flicker)
		    vI *= pow(16.0 * uv.x * (1.0-uv.x) * uv.y * (1.0-uv.y), 0.4);
		
		    // Add some random lines (and some multiplicative flicker. Oh well.)
		    #ifdef LINES_AND_FLICKER
		    int l = int(8.0 * rand(t+7.0));
		
		    if ( 0 < l ) vI *= randomLine( t+6.0+17.* float(0), uv);
		    if ( 1 < l ) vI *= randomLine( t+6.0+17.* float(1), uv);
		    if ( 2 < l ) vI *= randomLine( t+6.0+17.* float(2), uv);		
		    if ( 3 < l ) vI *= randomLine( t+6.0+17.* float(3), uv);
		    if ( 4 < l ) vI *= randomLine( t+6.0+17.* float(4), uv);
		    if ( 5 < l ) vI *= randomLine( t+6.0+17.* float(5), uv);
		    if ( 6 < l ) vI *= randomLine( t+6.0+17.* float(6), uv);
		    if ( 7 < l ) vI *= randomLine( t+6.0+17.* float(7), uv);
		
		    #endif
		
		    // Add some random blotches.
		    #ifdef BLOTCHES
		    int s = int( max(8.0 * rand(t+18.0) -2.0, 0.0 ));

		    if ( 0 < s ) vI *= randomBlotch( t+6.0+19.* float(0), uv, u_resolution);
		    if ( 1 < s ) vI *= randomBlotch( t+6.0+19.* float(1), uv, u_resolution);
		    if ( 2 < s ) vI *= randomBlotch( t+6.0+19.* float(2), uv, u_resolution);
		    if ( 3 < s ) vI *= randomBlotch( t+6.0+19.* float(3), uv, u_resolution);
		    if ( 4 < s ) vI *= randomBlotch( t+6.0+19.* float(4), uv, u_resolution);
		    if ( 5 < s ) vI *= randomBlotch( t+6.0+19.* float(5), uv, u_resolution);
	
		    #endif
	
		    // Show the image modulated by the defects
            gl_FragColor.xyz = oldImage * vI;
		
		    // Add some grain (thanks, Jose!)
		    #ifdef GRAIN
            gl_FragColor.xyz *= (1.0+(rand(uv+t*.01)-.2)*.15);		
            #endif		
		
	    }
	    else
	    {
		    gl_FragColor = texture2D( tex0, uv ); 
        }

    """) 



    renpy.register_shader("witchhouse.bloodlake", variables=""" 
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord; 
        uniform float u_time; 
        uniform float u_bloodlevel;
    """, vertex_200="""
        v_tex_coord = a_tex_coord; 
    """, fragment_250=""" 

        vec2 uv = v_tex_coord;
    
        vec4 waterColor = vec4(1.0);
        float reflactionY = u_bloodlevel;
        if(uv.y <= reflactionY)
        {        
            float oy = uv.y;
            uv.y = 2.0*reflactionY - uv.y;
            //uv.x = uv.x - ((uv.x-0.5)*0.2) * (1.0-oy/reflactionY);
            uv.y = uv.y + sin(1./(oy-reflactionY)+u_time*10.0)*0.05;
            waterColor = vec4(0.5,0.0, 0.0,1.0);
        }
    
        gl_FragColor = texture2D(tex0, uv) * waterColor;

    """) 



    renpy.register_shader("witchhouse.blurred", variables=""" 
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_resolution; 
        uniform vec2 u_mouse;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300=""" 

        const int nsamples = 10;
        vec2 center = u_mouse.xy /u_resolution.xy;
	    float blurStart = 1.0;
        float blurWidth = 0.1;

    
	    vec2 uv = v_tex_coord;
    
        uv -= center;
        float precompute = blurWidth * (1.0 / float(nsamples - 1));
    
        vec4 color = vec4(0.0);
        for(int i = 0; i < nsamples; i++)
        {
            float scale = blurStart + (float(i)* precompute);
            color += texture2D(tex0, uv * scale + center);
        }
    
    
        color /= float(nsamples);
    
	    gl_FragColor = color;                              

    """) 