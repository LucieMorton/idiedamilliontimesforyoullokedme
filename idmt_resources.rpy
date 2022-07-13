#colors
init: 
    image idmt_white = "#aaaaaa" 
    image idmt_black = "#000000" 
    image idmt_red = "#ff2400" 

#bgs and cgs
init: 
    image idmt_bathdoor:
        "IDMT/images/bathdoor.png" 
        matrixcolor SaturationMatrix(0.1) 
    image idmt_blood:
        size (1, 1)
        truecenter
        idmt_Blood("IDMT/images/blood_drop.png").sm
    image idmt_bus_stop: 
        "bg bus_stop" 
        yzoom -1 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    image idmt_ext_410: 
        "IDMT/images/ext_410.jpg" 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    image idmt_ext_emptytown:
        "IDMT/images/ext_emptytown.jpg" 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    image idmt_ext_emptytown2: 
        "idmt_ext_emptytown" 
        yzoom -1
    image idmt_ext_gates_lastact = "IDMT/images/ext_gates_lastact.png" 
    image idmt_ext_house_of_dv_lastact = "IDMT/images/ext_house_of_dv_lastact.png"
    image idmt_ext_house_of_un_day_lastact = "IDMT/images/ext_house_of_un_day_lastact.png"
    image idmt_ext_house_of_un_night = "IDMT/images/ext_house_of_un_night.jpg" 
    image idmt_ext_house_of_un_night_without_doors = "IDMT/images/ext_house_of_un_night_without_doors.png"
    image idmt_ext_square_lastact = "IDMT/images/ext_square_lastact.png"
    image idmt_eyes: 
        "IDMT/images/eyes1.png" with Dissolve (1.5)
        3.0 
        "IDMT/images/eyes2.png" with Dissolve (1.5) 
        3.0 
        repeat 
    image idmt_flashlight: 
        "IDMT/images/flashlight.png" 
        alpha 1.0 
        block: 
            ease 1.5 alpha 0.9 
            ease 1.5 alpha 1.0 
            repeat
    image idmt_int_bus_lastact = "IDMT/images/int_bus_lastact.png" 
    image idmt_int_catacombs_door_red = im.MatrixColor( im.Composite((1920,1080), (0,0), "images/bg/int_catacombs_door.jpg"), im.matrix.tint(1, 0.1, 0.1) ) 
    image idmt_int_catacombs_living = LiveComposite((1920, 1080), (0, 0), "images/bg/int_catacombs_living.jpg", (620, 475), "idmt_virus") 
    image idmt_int_catacombs_living_nodoor = LiveComposite((1920, 1080), (0, 0), "images/bg/int_catacombs_living_nodoor.jpg", (620, 475), "idmt_virus")
    image idmt_int_entrance:
        "IDMT/images/int_entrance.png" 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    image idmt_int_etage:
        "IDMT/images/int_etage.png" 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(0) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.05) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.15) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.2) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.25) 
        choice: 
            matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.3)
        pass 
        choice: 
            0.1 
        choice: 
            0.2 
        choice: 
            0.3 
        choice: 
            0.4 
        choice: 
            0.5 
        repeat
    image idmt_int_firstetage:
        "IDMT/images/int_firstetage.jpg" 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1) * TintMatrix((85, 105, 185)) 
        yzoom -1 
    image idmt_int_house_of_mt_night = "IDMT/images/int_house_of_mt_night.jpg" 
    image idmt_int_house_of_mt_night2 = "IDMT/images/int_house_of_mt_night2.jpg" 
    image idmt_int_house_of_un_night = "IDMT/images/int_house_of_un_night.jpg" 
    image idmt_lenacatkiller = im.MatrixColor( im.Composite((1920,1080), (0,0), "IDMT/images/lena_catkiller.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image idmt_moon: 
        "IDMT/images/moon.png" 
        choice: 
            alpha 1.0 
        choice: 
            alpha 0.95 
        choice: 
            alpha 0.96 
        choice: 
            alpha 0.97 
        choice:
            alpha 0.98 
        choice: 
            alpha 0.99 
        pass
        choice:
            0.01 
        choice: 
            0.02 
        choice: 
            0.03 
        choice: 
            0.04 
        choice: 
            0.05
        repeat 
    image idmt_mysticforest = "IDMT/images/mysticforest.jpg" 
    image idmt_sky = "IDMT/images/sky.png"  
    image idmt_un_suicide: 
        "cg d7_un_suicide" 
        crop (0, 0, 1920, 1080) 
    image idmt_virus: 
        idmt_RectCluster(Solid("#fa0000"), 4, 15, 5).sm
        size (50, 45)

#videos 

init: 
    image idmt_cuteye = Movie(size = (1920, 1080), play="IDMT/video/cuteye.webm", loop=False) 
    image idmt_cuteye1 = Movie(size = (1920, 1080), play="IDMT/video/cuteye.webm", loop=True)
    image idmt_cuteye_fullscreen: 
        contains: 
            "idmt_cuteye1" 
            zoom 0.5 
            xpos 0 ypos 0 
        contains: 
            "idmt_cuteye1" 
            zoom 0.5 
            xpos 0.5 ypos 0 
            matrixcolor BrightnessMatrix(0.4) * ContrastMatrix(3.5) * ColorizeMatrix("#ff0000", "#000000") 
        contains: 
            "idmt_cuteye1" 
            zoom 0.5 
            xpos 0 ypos 0.5 
            matrixcolor BrightnessMatrix(0.2) * ContrastMatrix(3.5) * ColorizeMatrix("#000000", "#ff0000") 
        contains: 
            "idmt_cuteye1" 
            zoom 0.5 
            xpos 0.5 ypos 0.5 
            matrixcolor BrightnessMatrix(0) * ContrastMatrix(3.5) * ColorizeMatrix("#aaaaaa", "#0000ff")
    image idmt_mask = Movie(size = (1920, 1080), play="IDMT/video/mask.webm", loop=True)
    image idmt_suicide = Movie(size = (1920, 1080), play="IDMT/video/suicide.webm", loop=False) 


#slideshow 
init: 
    image idmt_slideshow: 
        contains: 
            "cg epilogue_dv_3" 
        contains: 
            alpha 0.0 
            "cg epilogue_sl_2" 
            5.0
            ease 2.0 alpha 1.0 
        contains: 
            alpha 0.0 
            10.0
            "cg epilogue_mi_9" 
            ease 2.0 alpha 1.0 
        contains: 
            alpha 0.0 
            "cg epilogue_us_3_a" 
            15.0
            ease 2.0 alpha 1.0 
        contains: 
            alpha 0.0 
            "cg epilogue_un_good" 
            20.0 
            ease 2.0 alpha 1.0 
        contains: 
            alpha 0.0 
            "cg epilogue_dv_3"
            25.0 
            ease 2.0 alpha 1.0
        27.0 
        repeat


#flashbacks 
init: 
    image idmt_flashbacks_slide: 
        idmt_LumaMask("idmt_slideshow", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_all: 
        idmt_LumaMask("cg final_all_2", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_deadlena: 
        idmt_LumaMask("idmt_un_suicide", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5
    image idmt_flashback_lena1: 
        idmt_LumaMask("cg d5_un_island", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_lena2: 
        idmt_LumaMask("cg d6_un_evening_2", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_lena3: 
        idmt_LumaMask("cg d3_un_dance", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_lena4: 
        idmt_LumaMask("cg d7_un_hentai_3", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    image idmt_flashback_final: 
        idmt_LumaMask("cg epilogue_un_bad", "idmt_mask")
        alpha 0.0
        easein 3.0 alpha 0.5 
    
     
#masks 
init: 
    image idmt_daysky: 
        "IDMT/images/sky_mask/daysky.png" 
    image idmt_eveningsky: 
        "IDMT/images/sky_mask/eveningsky.png" 
    image idmt_lightningsky: 
        xsize 4604
        contains: 
            "IDMT/images/sky_mask/greysky.png" 
        contains: 
            "IDMT/images/sky_mask/lightningsky1.png" 
            choice: 
                alpha 0.75 
            choice: 
                alpha 0.5 
            choice: 
                alpha 0.25 
            choice: 
                alpha 0 
            pass 
            choice:
                0.05 
            choice: 
                0.1 
            choice: 
                0.15 
            choice: 
                0.2 
            repeat 
        contains: 
            "IDMT/images/sky_mask/lightningsky2.png" 
            choice: 
                alpha 0.75 
            choice: 
                alpha 0.5 
            choice: 
                alpha 0.25 
            choice: 
                alpha 0 
            pass 
            choice:
                0.05 
            choice: 
                0.1 
            choice: 
                0.15 
            choice: 
                0.2 
            repeat 
        contains: 
            "IDMT/images/sky_mask/lightningsky3.png" 
            choice: 
                alpha 0.75 
            choice: 
                alpha 0.5 
            choice: 
                alpha 0.25 
            choice: 
                alpha 0 
            pass 
            choice:
                0.05 
            choice: 
                0.1 
            choice: 
                0.15 
            choice: 
                0.2 
            repeat 
    image idmt_dsky_bg: 
        idmt_randomStart("idmt_daysky", 4604) 
        xtile 2 subpixel True 
        xoffset 0
        linear 400 xoffset -4604
        repeat 
    image idmt_evsky_bg: 
        idmt_randomStart("idmt_eveningsky", 4604) 
        xtile 2 subpixel True 
        xoffset 0
        linear 400 xoffset -4604
        repeat 
    image idmt_lsky_bg: 
        "idmt_lightningsky" 
        xtile 2 subpixel True 
        xoffset 0
        linear 400 xoffset -4604
        repeat 
    image idmt_daysky_bg = LiveComposite((1920, 1080), (0, 0), "idmt_dsky_bg") 
    image idmt_eveningsky_bg = LiveComposite((1920, 1080), (0, 0), "idmt_evsky_bg") 
    image idmt_lightningsky_bg = LiveComposite((1920, 1080), (0, 0), "idmt_lsky_bg") 
    image idmt_veins: 
        idmt_AnimatedMask("IDMT/images/veinmask/veins.png", "IDMT/images/veinmask/veins.png", "IDMT/images/veinmask/veinsvign.png", 0.15, 16, moving=False, speed=10.0, frequency=0.25, amount=0.1)
        xanchor 0.05 zoom 1.10
        xpos -5
        subpixel True
        parallel:
            ease 2.0 xpos 5
            ease 1.0 xpos 0
            ease 1.0 xpos 5
            ease 2.0 xpos -5
            ease 1.0 xpos 0
            ease 1.0 xpos -5
            repeat
        parallel:
            choice:
                0.6
            choice:
                0.2
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            pass
            choice:
                xoffset 0
            choice:
                xoffset 1
            choice:
                xoffset 2
            choice:
                xoffset -1
            choice:
                xoffset -2
            repeat 


#sprites 
init: 
    
    image dv_faceless1 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/dv_faceless/1.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image dv_faceless2 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/dv_faceless/2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image dv_faceless3 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/dv_faceless/3.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image dv_faceless4 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/dv_faceless/4.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
    image dv_faceless: 
        "dv_faceless1" 
        0.0001 
        "dv_faceless2" 
        0.0001 
        "dv_faceless3" 
        0.0001 
        "dv_faceless4" 
        0.0001 
        repeat 

    image dv faceless: 
        "dv_faceless" 

        mesh True shader "witchhouse.swirl"

        u_resolution (1920,1080)
        u_whirl_radius .5
        block:

            linear 1000 u_whirl_angle 3.1415 * 10
            repeat


     
    image mi_faceless1 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mi_faceless/1.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mi_faceless2 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mi_faceless/2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mi_faceless3 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mi_faceless/3.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mi_faceless4 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mi_faceless/4.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

    image mi_faceless:
        "mi_faceless1" 
        0.0001 
        "mi_faceless2" 
        0.0001 
        "mi_faceless3" 
        0.0001 
        "mi_faceless4" 
        0.0001 
        repeat 

    image mi faceless: 
        "mi_faceless" 

        mesh True shader "witchhouse.swirl"

        u_resolution (1920,1080)
        u_whirl_radius .5
        block:

            linear 1000 u_whirl_angle 3.1415 * 10
            repeat 



    image mz_faceless1 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mz_faceless/1.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mz_faceless2 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mz_faceless/2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mz_faceless3 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mz_faceless/3.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image mz_faceless4 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/mz_faceless/4.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
    image mz_faceless: 
        "mz_faceless1" 
        0.0001 
        "mz_faceless2" 
        0.0001 
        "mz_faceless3" 
        0.0001 
        "mz_faceless4" 
        0.0001 
        repeat 

    image mz faceless: 
        "mz_faceless" 

        mesh True shader "witchhouse.swirl"

        u_resolution (1920,1080)
        u_whirl_radius .5
        block:

            linear 1000 u_whirl_angle 3.1415 * 10
            repeat 



    image sl_faceless1 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/sl_faceless/1.png"), im.matrix.tint(0.63, 0.78, 0.82) )  
    image sl_faceless2 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/sl_faceless/2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image sl_faceless3 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/sl_faceless/3.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image sl_faceless4 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/sl_faceless/4.png"), im.matrix.tint(0.63, 0.78, 0.82) )
        
    image sl_faceless:    
        "sl_faceless1" 
        0.0001 
        "sl_faceless2" 
        0.0001 
        "sl_faceless3" 
        0.0001 
        "sl_faceless4" 
        0.0001 
        repeat 

    image sl faceless: 
        "sl_faceless" 

        mesh True shader "witchhouse.swirl"

        u_resolution (1920,1080)
        u_whirl_radius .5
        block:

            linear 1000 u_whirl_angle 3.1415 * 10
            repeat 



    image us_faceless1 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/us_faceless/1.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image us_faceless2 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/us_faceless/2.png"), im.matrix.tint(0.63, 0.78, 0.82) )  
    image us_faceless3 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/us_faceless/3.png"), im.matrix.tint(0.63, 0.78, 0.82) )  
    image us_faceless4 = im.MatrixColor( im.Composite((463,1080), (0,0), "IDMT/sprites/us_faceless/4.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

    image us_faceless:
        "us_faceless1" 
        0.0001 
        "us_faceless2" 
        0.0001 
        "us_faceless3" 
        0.0001 
        "us_faceless4" 
        0.0001 
        repeat 

    image us faceless: 
        "us_faceless" 

        mesh True shader "witchhouse.swirl"

        u_resolution (1920,1080)
        u_whirl_radius .5
        block:

            linear 1000 u_whirl_angle 3.1415 * 10
            repeat 

    image sem eyeless = im.MatrixColor( im.Composite((1125,1080), (0,0), "IDMT/sprites/sem_eyeless.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
    image un eyeless = im.MatrixColor( im.Composite((675,1080), (0,0), "IDMT/sprites/un_eyeless.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

    image un angry coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un evil smile coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un normal coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un shy coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un smile coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un smile2 coat1 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "IDMT/sprites/un_coat/un_1_winter.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

    image un cry coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un cry smile coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un sad coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un scared coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un shocked coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un surprise coat2 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "IDMT/sprites/un_coat/un_2_winter.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

    image un angry coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un grin coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un laugh coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un rage coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un serious coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 
    image un smile coat3 = im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "IDMT/sprites/un_coat/un_3_winter.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ) 

#music     
init: 
    $ idmt_blackearrape = "IDMT/music/black earrape.mp3"
    $ idmt_devil = "IDMT/music/d3v1l.mp3"
    $ idmt_deadpatients = "IDMT/music/dead patients.mp3" 
    $ idmt_deathvinyl = "IDMT/music/deathvinyl.mp3" 
    $ idmt_doolb = "IDMT/music/doolb.mp3" 
    $ idmt_help = "IDMT/music/help.mp3"
    $ idmt_htaednaissur = "IDMT/music/htaed naissur.mp3" 
    $ idmt_idiedamilliontimes = "IDMT/music/i died a million times.mp3" 
    $ idmt_lwo = "IDMT/music/lwo.mp3" 
    $ idmt_mantra = "IDMT/music/mantra.mp3"
    $ idmt_meetmethere = "IDMT/music/meet me there.mp3" 
    $ idmt_myjoyptpf = "IDMT/music/myjoyptpf.mp3" 
    $ idmt_night = "IDMT/music/night.mp3" 
    $ idmt_outspace = "IDMT/music/outspace.mp3" 
    $ idmt_redblack = "IDMT/music/redblack.mp3"
    $ idmt_reganeet = "IDMT/music/reganeet.mp3"
    $ idmt_sdneirfebstel = "IDMT/music/sdneirf eb stel.mp3" 
    $ idmt_sicksociety = "IDMT/music/sick society.mp3"
    $ idmt_skcabhsalf = "IDMT/music/skcabhsalf.mp3" 
    $ idmt_skin = "IDMT/music/skin.mp3" 
    $ idmt_suicidalgirl = "IDMT/music/suicidal girl.mp3" 
    $ idmt_wildlovvers = "IDMT/music/wild lovvers.mp3" 


#sounds
init: 
    $ idmt_bell = "IDMT/sounds/bell.mp3" 
    $ idmt_curtains = "IDMT/sounds/curtains.mp3"
    $ idmt_glitch = "IDMT/sounds/glitch.ogg" 
    $ idmt_glitch2 = "IDMT/sounds/glitch2.ogg"
    $ idmt_knife = "IDMT/sounds/knife.mp3"
    $ idmt_int_cabin_night_reverb = "IDMT/sounds/int_cabin_night_reverb.mp3" 
    $ idmt_short_watersplash = "IDMT/sounds/short_watersplash.wav"
    $ idmt_squeakwithecho = "IDMT/sounds/squeakwithecho.mp3"
    $ idmt_vinyl = "IDMT/sounds/vinyl.mp3" 
    $ idmt_wakeup = "IDMT/sounds/wakeup.mp3" 
    $ idmt_waterdrops = "IDMT/sounds/waterdrops.mp3"