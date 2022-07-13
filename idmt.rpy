label i_died_million_times: 
    window hide 
    stop music fadeout 1
    stop sound fadeout 1                                                                                                                  
    stop sound2 fadeout 1
    stop sound3 fadeout 1
    stop sound_loop fadeout 1
    stop sound_loop2 fadeout 1
    stop sound_loop3 fadeout 1
    stop voice fadeout 1
    stop ambience fadeout 1
    scene idmt_black with fade
    $ renpy.pause (2.0, hard=True) 
    $ night_time() 
    $ persistent.sprite_time = 'night' 
    menu: 
        "Я прочитал описание в Стиме и готов к любой дичи." 
        "Да":
            jump idmt_ch1 
        "Нет": 
            return 

#upd from 02.05.2022: bug fix 
label idmt_teardebug: 
    $ number = None 
    $ offtimeMult = None 
    $ ontimeMult = None 
    $ offsetMin = None 
    $ offsetMax = None 
    $ srf = None 
    return