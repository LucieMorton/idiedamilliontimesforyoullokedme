label idmt_ch3: 
    $ save_name = "Я умерла... Сосложение 'Беги туда, где нет никого'"
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}Сосложение\n\n\n'Беги туда, где нет никого'{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    hide text with dspr 
    show layer master 
    stop ambience 
    $ renpy.pause (2.5, hard=True) 
    window auto 
    "Архидодик Семён Персунов, 'Сны хиккана'." 
    "..."
    "Я ещё не умер, но уже вижу предсмертные галлюцинации." 
    window hide 
    $ renpy.pause (1.5, hard=True)
    $ witchhouse_shake = 3.5  
    scene cg epilogue_mi_8 at idmt_mshake: 
        truecenter 
        zoom 1.04 
    show prologue_dream
    with fade 
    play music idmt_blackearrape
    $ renpy.pause (1.5, hard=True) 
    window auto 
    "Я зашёл в черную комнату, где находился чёрный демон." 
    "Моей задачей было отыскать его." 
    th "Ну да, я же такой храбрый, что можно без опаски поручить что-то подобное кому-то вроде меня." 
    "Будь проклят тот, кто послал меня сюда."
    dreamgirl "Сёёёёмаааа!!!" 
    "Конечно же, меня нашли раньше."
    "Я заметался, как безумный, натыкаясь на стены, но не отдаляясь от демона ни на йоту." 
    "Меня даже преследовать было не надо.{w} Рано или поздно я сам налечу на клинок, отчаявшись." 
    "И вот за мгновение до этого{nw}" 
    window hide
    stop music fadeout 4.5 
    scene idmt_black with Dissolve(3.5) 
    $ renpy.pause (2.5, hard=True)
    scene cg epilogue_un_good: 
        matrixcolor BrightnessMatrix(0) * SaturationMatrix(1.0)
        ease 6.66 matrixcolor BrightnessMatrix(-0.3) * SaturationMatrix(0.1)
    show prologue_dream
    with fade 
    play music idmt_redblack
    $ renpy.pause (2.5, hard=True)
    window auto 
    extend " сцена переменилась." 
    "Я увидел Лену."
    "Она поставила кружку с чаем на столик рядом с креслом."
    "В камине тихо потрескивали дрова, а за окном бушевала метель."
    "Я укутался в плед и посмотрел на Лену." 
    me "Лена?" 
    "..." 
    me "Лена???" 
    window hide 
    $ renpy.pause (6.66, hard=True) 
    scene idmt_sky 
    show idmt_moon zorder 1 
    show idmt_daysky_bg zorder 2: 
        alpha 0.222
        blend "add"
    show layer master at idmt_bxw_filter
    $ renpy.pause (6.66, hard=True) 
    $ witchhouse_shake = 2.22
    scene expression(idmt_darkpict("cg epilogue_un_good")) at idmt_mshake:
        zoom 1.0 align (0.5, 0.5) 
        ease 6.66 zoom 2.22 align (0.5, 0.05)
    $ renpy.pause (6.66, hard=True) 
    scene idmt_sky 
    show idmt_moon zorder 1 
    show idmt_daysky_bg zorder 2: 
        alpha 0.222
        blend "add"
    show layer master: 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1) blur 0
        ease 6.66 matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.15) blur 2
    $ renpy.pause (6.66, hard=True) 
    scene expression(idmt_bloodypict("anim intro_15")) 
    $ renpy.pause (6.66, hard=True) 
    scene idmt_sky 
    show idmt_moon zorder 1 
    show idmt_daysky_bg zorder 2: 
        alpha 0.222
        blend "add"
    show layer master: 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.15) blur 3 
        ease 6.66 matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.2) blur 4 
    $ renpy.pause (6.66, hard=True) 
    python: 
        witchhouse_musicpos = get_pos() 
        witchhouse_startpos = witchhouse_musicpos - 0.1666 
        if witchhouse_startpos < 0: witchhouse_startpos = 0 
        idmt_playingtrack = "<from " + str(witchhouse_startpos) + " to " + str(witchhouse_musicpos) + ">IDMT/music/redblack.mp3" 
        renpy.music.play(idmt_playingtrack, loop=True) 
    scene idmt_cuteye 
    $ renpy.pause (3.5, hard=True) 
    show screen tear(30, 1, 0.1, 0, 40)
    play sound idmt_glitch
    $ renpy.pause (0.3, hard=True)
    stop sound
    hide screen tear 
    call idmt_teardebug
    scene idmt_cuteye_fullscreen 
    show sem eyeless zorder 1 
    show idmt_cuteye1 zorder 2: 
        zoom 0.05 
        xpos 0.46 ypos 0.2 
    show idmt_cuteye1 as ce1 zorder 2: 
        zoom 0.05 
        xpos 0.51 ypos 0.16 
    show idmt_blood zorder 3: 
        zoom 0.33
        pos(934, 236) 
    show idmt_blood as bld zorder 3: 
        zoom 0.33
        pos(1030, 192) 
    $ renpy.pause (2.22, hard=True) 
    window auto 
    "Когда я умру, я расскажу Лене эти сны..." 
    window hide 
    $ renpy.pause (2.22, hard=True) 
    show screen tear(25, 0.1, 1, 0, 40)
    play sound idmt_glitch
    $ renpy.pause (0.3, hard=True)
    stop sound
    hide screen tear 
    call idmt_teardebug
    stop music 
    scene idmt_int_house_of_un_night
    show un serious dress close at center zorder 1
    show idmt_black zorder 2 
    $ renpy.pause (2.5, hard=True)
    window show 
    "Меня пробрал едва слышный удушливый кашель."
    "Какими же реальными казались все эти корчившиеся в конвульсиях образы, сменявшие друг друга, заставлявшие меня корчиться вместе с ними." 
    th "Кто я? Где я? Живой ли я вообще?" 
    "..."
    "Подо мной что-то мягко скрипело.{w} Кровать..." 
    "Я открыл глаза." 
    window hide
    hide idmt_black 
    show unblink zorder 2
    play ambience ambience_int_cabin_night 
    $ renpy.pause (2.5, hard=True) 
    window auto 
    play music idmt_wildlovvers 
    "Реальность показалась продолжением ужасного забытья." 
    th "Снова Лена.{w} Снова её проклятый домик." 
    th "Куда бы я ни шёл, я оказывался здесь.{w} Он засасывал меня в себя, как трясина." 
    "Его хозяйка, возвышаясь надо мной, явно прокачала свои умения и теперь могла внушать страх без ножа, без факела и с обычным выражением лица." 
    th "Или это просто я стал более восприимчив?" 
    "..."
    "Плевать. Страшно мне было или нет, {i}с этим пора было заканчивать{/i}." 
    show un angry2 dress close at center zorder 1 with dspr 
    un "Очухался, я гляжу?" 
    me "Эхехе, представь себе." 
    "Хоть и с обратным знаком, мои чувства прояснились." 
    "Зрение, осязание, слух, память({i}sic!{/i})." 
    "А еще меня переполнял гнев." 
    "Пришло время выбить из неё всё, что было ей известно.{w} Неважно как." 
    me "Ну что, когда мы там из лагеря уезжаем? Завтра? Послезавтра? Через неделю? Уже уехали?" 
    me "Ах да. Там в лесу девку повесили. А тебя я видел как раз неподалеку, ты лыбилась как маньячка. Ничего мне сказать не хочешь?"
    show un rage dress close at center zorder 1 with dspr 
    un "Какой, к чертовой матери, лагерь? Какой лес, какая девка повешенная? Заткни свою пасть, пока я не вышибла все твои пропитые мозги!!!" 
    "Оххохохо, это было сильно, признаю.{w} Я бы посмотрел, как она вышибает мозги."
    "Вот только во второй раз на мне эта ложь не сработает." 
    me "Какой лагерь, спрашиваешь? Совёнок!!! Ни о чём тебе это название не говорит?" 
    me "Знаешь, что еще забавно? {i}Ты{/i} спрашиваешь, какой лагерь, но пропитые мозги почему-то {i}у меня{/i}." 
    me "Уже и не помню, когда последний раз выпивал. В какой жизни, так сказать."
    me "Только голос не повышай, ладно? Я тоже могу кричать, если что." 
    show un cry dress close at center zorder 1 with dspr 
    un "Что ты... мелешь..." 
    un "Вечно, как только сунешься к кибер-{w=1.5}{nw}" 
    show un shocked dress far at center zorder 1 with dspr 
    "Ага!!!" 
    "Поняв, что проговорилась, Лена осеклась и отшатнулась от меня." 
    "Уж что-что, а то, что в лагере существовал кружок кибернетики, я помнил прекрасно." 
    "Полностью завладев моральным преимуществом, я резко встал и продолжил." 
    me "Эх, а так хорошо все начиналось... Что это у меня пропитые мозги... В следующий раз постарайся попрекнуть меня чем-нибудь более правдоподобным, ладно?" 
    me "Конечно, если следующий раз у тебя будет. Потому что сейчас я спрошу с тебя за всё." 
    play sound sfx_table_hit
    me "Ты сама-то кто? КТО ТЫ-ТО, ТВОЮ МАТЬ?" with vpunch 
    play sound sfx_table_hit
    me "И да, мне неинтересно, алкашка ты, наркоманка или потенциальная суицидница. Просто скажи мне - КТО ТЫ И ЧТО ЗА ЧЕРТОВЩИНА ТВОРИТСЯ?" with vpunch
    show un cry dress far at center zorder 1 with dspr 
    play sound sfx_table_hit
    me "ПОЧЕМУ КАЖДЫЙ ГРЁБАНЫЙ РАЗ ВЫХОДЯ ОТСЮДА, Я ВНОВЬ ОКАЗЫВАЮСЬ В ЭТОМ ПРОКЛЯТОМ ДОМИКЕ? КУДА БЫ Я НИ ПОШЁЛ." with vpunch 
    play sound sfx_table_hit
    me "ПОЧЕМУ Я ВИЖУ ТЕБЯ РЯДОМ СО МНОЙ КАЖДЫЙ РАЗ В КАКИХ-ТО КОШМАРАХ?" with vpunch 
    play sound sfx_table_hit 
    me "ПОЧЕМУ? ГДЕ МЫ? КАКОЕ СЕГОДНЯ ЧИСЛО, МЕСЯЦ, ГОД?" with vpunch 
    play sound sfx_table_hit
    me "ПРОСТО СКАЖИ, ПОЧЕМУ? ЗА ЧТО МНЕ ЭТО ВСЁ? СКАЖИ, И Я УЙДУ, УЕДУ, ИСЧЕЗНУ ОТСЮДА РАЗ И НАВСЕГДА...{w} если только разберусь, как..." with vpunch
    hide un with dissolve
    "Вот и всё, на что меня хватило.{w} Перечислив все свои злоключения, я перегорел." 
    "Мой голос осёкся.{w} Я в изнеможении опустился на кровать и обхватил голову руками." 
    "Кулак, которым я от души колотил по столешнице, явно этого не одобрял."
    "Я думал, что мне станет хоть немного легче, но увы.{w} Я был раздавлен своей пустой злобой." 
    "Что-то внутри меня говорило, что ответы на любой из этих вопросов мне бы не понравились совсем." 
    "Тогда зачем же я продолжал упрямствовать и переть как баран?"
    "Подтверждая мои худшие опасения, раздался {i}мертвецки спокойный{/i} голос Лены." 
    show un angry2 dress far at center zorder 1 
    with dissolve 
    un "{i}Как всегда{/i}, ты видишь во всём только себя." 
    show un angry2 dress close at center zorder 1 with dspr 
    un "И мне очень жаль, что ты так ничего и не понял." 
    me "Ну да. Я. Ничего. Не понял. Отлично." 
    me "ОТЛИЧНО, ТВОЮ МАТЬ!!!" with vpunch
    me "МНЕ И НЕ НАДО НИЧЕГО ПОНИМАТЬ!!!" with vpunch
    me "МОЖНО ПОДУМАТЬ, ЭТО ТЫ СЕГОДНЯ ТРЯСЛАСЬ ОТ КАЖДОГО ШОРОХА И МУЧИЛАСЬ КОШМАРАМИ!!!" with vpunch 
    me "ВОТ И ВСЁ, ЧТО Я ДОЛЖЕН ПОНИМАТЬ!!!" with vpunch
    "Меня вновь разобрала злоба." 
    "Сжав кулаки, я накинулся на нее, более не имея за душой ничего, чтобы показать, что прав тут только я...{w=1.5}{nw}" 
    window hide 
    show un angry dress close at center zorder 1 with dspr 
    show layer master:
        subpixel True
        parallel: 
            zoom 1.0 align (0.5, 0.5) 
            ease 1.0 zoom 2.22 align (0.5, 0.2) 
        parallel: 
            1.0 
            blur 0
            ease 2.5 blur 15 
        parallel: 
            1.0 
            idmt_dizzy(2.5, 2.5)
    $ renpy.pause (1.0, hard=True) 
    stop ambience 
    stop music
    play sound sfx_punch_washstand 
    show expression Solid("ff0000") as idmt_redmask onlayer widgetoverlay:
        additive 1.0 
        alpha 0.0 
        ease 2.5 alpha 0.5 
    show expression Solid("ff0000") as idmt_redmask2 onlayer widgetoverlay:
        additive 0.4 
        alpha 0.0 
        ease 2.5 alpha 0.5 
    show idmt_veins onlayer widgetoverlay: 
        additive 0.5
        alpha 0.0 
        ease 2.5 alpha 0.5 
    with vpunch 
    play music idmt_outspace 
    window auto 
    "Однако, даже не увидев замаха, я мигом оказался на полу." 
    "Мир померк.{w} Мою шею что-то сдавило, будто тисками, и сжимало все сильнее, выдавливая из меня душу." 
    window hide 
    stop music 
    hide idmt_redmask onlayer widgetoverlay 
    hide idmt_redmask2 onlayer widgetoverlay 
    hide idmt_veins onlayer widgetoverlay
    scene idmt_white
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}Твой человек\nникогда не будет твоим.{/color}{/size}{/font}") zorder 1 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    stop ambience
    scene idmt_suicide 
    $ renpy.pause (1.0, hard=True) 
    scene idmt_int_house_of_un_night 
    show un eyeless at center zorder 1 
    show layer master: 
        blur 10 
        ease 6.66 blur 0
    show expression Solid("ff0000") as idmt_redmask3 onlayer widgetoverlay:
        additive 1.0 
        alpha 1.0 
        ease 6.66 alpha 0.0 
    show expression Solid("ff0000") as idmt_redmask4 onlayer widgetoverlay:
        additive 0.4 
        alpha 1.0 
        ease 6.66 alpha 0.0 
    show idmt_veins onlayer widgetoverlay: 
        additive 0.5
        alpha 1.0 
        ease 6.66 alpha 0.0 
    play ambience ambience_int_cabin_night 
    $ renpy.pause (6.66, hard=True) 
    hide idmt_redmask3 onlayer widgetoverlay 
    hide idmt_redmask4 onlayer widgetoverlay 
    hide idmt_veins onlayer widgetoverlay
    play music idmt_myjoyptpf 
    window auto 
    "Я хрипел.{w} Просто чудо, что Лена не добила меня." 
    "В одном она была права - я не понял ничего.{w} Но мне было вовсе не до этого." 
    "Я оглянулся.{w} Лена с отрешённым видом привалилась к стене, уставившись перед собой стеклянными глазами."
    "Душевное состояние этой ненормальной меня мало волновало.{w} Зато изрядно волновало то, как бы оказаться от неё и от всего вокруг как можно дальше." 
    th "Настолько, насколько здесь это вообще возможно." 
    "Я рванулся" with vpunch
    extend " и медленно, словно во сне, выбежал из домика," 
    play ambience ambience_camp_center_night
    window hide
    scene idmt_ext_house_of_un_night 
    show layer master: 
        zoom 1.10 anchor (48, 27)
        ease 0.30 pos (0,0)
        ease 0.30 pos (25, 25)
        ease 0.30 pos (0, 0)
        ease 0.30 pos (-25, 25)
        repeat 
    with dissolve 
    $ renpy.pause (3.5, hard=True) 
    play ambience ambience_forest_night
    show bg ext_path_night zorder 1 with dissolve 
    $ renpy.pause (3.5, hard=True) 
    show bg ext_path2_night zorder 2 with dissolve 
    $ renpy.pause (1.5, hard=True)
    window auto 
    extend " из последних сил прокладывая себе путь сквозь вязкий, как кисель, воздух в сторону леса." 
    "Мне вдогонку неслись мольбы и проклятия, перемалывая мои перепонки в кашу." 
    "Не всё еще было кончено.{w} Наверное, лишь чудо помогло бы мне пережить эту злую ночь." 
    th "Ну, думаю, {i}это все еще была одна и та же ночь{/i}."
    th "Только не оглядываться... и как бы ненароком не оказаться опять на той проклятой поляне..."
    play sound sfx_owl_far
    dreamgirl "Кы-ысь... кы-ысь..." 
    show idmt_eyes zorder 3: 
        additive 0.5
    "Бесконечное множество раз мне виделись во тьме зеленоватые отблески, похожие на чьи-то всевидящие глаза." 
    "И вот, когда я почувствовал, что ногам не сделать больше ни одного шага, ветви передо мной расступились"  
    scene bg ext_old_building_night_moonlight with dissolve 
    extend " и показалось широкое открытое пространство." 
    "Залитый светом мёртвой луны ведьмин круг." 
    "Я тяжко выдохнул и рухнул на колени напротив старого лагеря." 
    th "Это и было максимально возможное отдаление?"
    "Могло показаться странным, но..." 
    "Самое внушающее ужас здание во всём Совёнке выглядело гораздо более приветливым, чем его обжитые улочки." 
    "Я с усилием поднялся.{w} Остался последний рывок." 
    "Убежать с этого проклятого открытого пространства." 
    "Оставить все свои страхи и всё остальное далеко позади." 
    "Забиться в подвал и...{w=1.5} уж лучше гнить там." 
    th "Весь свет во мне и так погас. А снаружи его никогда и не было." 
    "Я пересёк ведьмин круг, оглянулся и открыл входную дверь полусгнившего здания." 
    play sound idmt_squeakwithecho
    "Она заскрипела на весь лес так, что я сразу понял: все мои петляния по лесу были лишь пустой тратой сил, времени и эмоций." 
    stop ambience
    scene bg int_old_building_night 
    with dissolve
    "Впрочем, сюда еще надо было осмелиться зайти." 
    th "Как будто {i}она{/i} не осмеливалась."
    window hide 
    scene idmt_white
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}Двери закрыты,\nокна забиты,\nмы в могиле зарыты.{/color}{/size}{/font}") zorder 1 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    show layer master at idmt_oldcinema
    show cg d4_catac_un zorder 2: 
        blur 3.5 
    $ renpy.pause (6.5, hard=True) 
    window auto 
    stop ambience
    scene bg int_old_building_night 
    window auto
    th "Да-да, спасибо за напоминание." 
    "Может, это Лена и насылала все эти видения? Я бы не удивился." 
    "И кто знает, если бы я не был таким пугливым и всматривался в них как следует..." 
    th "Делать мне больше нечего." 
    "Я засомневался в следующем шаге."
    "Почему-то очень захотелось найти Лену.{w} Плевать, если бы убила, значит, этого я и заслуживал." 
    "Но пока глаза боялись одного, а мысли думали о другом, ноги делали третье и вели моё тело к железному люку в углу." 
    play sound sfx_open_metal_hatch 
    "Мои руки открывали его..." 
    scene idmt_black with fade 
    "Я падал в темноту и пустоту, бесконечно устав от всего и желая, чтобы приземление было настолько жестким, что куски разлетелись бы по всей сети подземных тоннелей." 
    "..." 
    window hide 
    play sound sfx_jump_into_hole_2
    scene bg int_catacombs_entrance_red
    with Dissolve(3.5)
    play ambience ambience_catacombs fadein 3 
    $ renpy.pause (1.5, hard=True)
    window show
    "Кажется, я {i}всего лишь{/i} слегка ушибся." 
    "Тут было... темно, тихо и влажно." 
    "Не так темно и тихо, как я ожидал, но это были мелочи.{w} Главное - я был здесь {i}один{/i}." 
    th "Именно этого я и добивался." 
    "Держась за стену, я поднялся на ноги и поплёлся наугад, не имея перед собой четкой цели." 
    "Пожалуй, уже неважно, догадается Лена или нет, что я спрыгнул сюда.{w} А она догадается, в этом я был уверен." 
    "Так что рано или поздно я добегаюсь." 
    "Меня поразили те спокойствие и равнодушие, с которыми я об этом думал." 
    th "Да... вот оно, то, что я искал всю ночь, и то, от чего я всё остальное время почему-то убегал." 
    th "Спокойствие.{w} Хоть и ненадолго." 
    "Темнота, которой я раньше боялся до дрожи, теперь несла своеобразное умиротворение."
    th "Мне никуда не деться с подводной лодки.{w} Нечего узнавать, кроме ламп, проводов, средств связи, кнопочек, рычагов..." 
    scene idmt_int_catacombs_door_red 
    with fade 
    "Подземный коридор окончился. Мой дальнейший путь преграждала массивная железная дверь со значком радиационной опасности." 
    "Один вид этого значка заставил меня исступленно расхохотаться." 
    th "А если бы на моём месте был этот значок и он увидел бы на двери меня, он испугался бы или нет?" 
    "Продолжая безумно хохотать, я просто дёрнул дверь на себя, и она, к моему удивлению, скрипнула и открылась." 
    play sound sfx_open_door_mines_metal 
    scene idmt_black with fade
    "Тут не было заперто." 
    "Я влетел в открывшийся проход, зажмурился от неожиданно яркого света и почему-то тут же заткнулся." 
    "Какой бы прилив мрачного умиротворения я до этого ни испытывал..."
    "Захотелось закрыться, за что я тут же и принялся, нашарив дверной вентиль." 
    dreamgirl "Не туда крутишь." 
    scene idmt_int_catacombs_living: 
        matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0)
        linear 111 matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    show uv normal far at center zorder 1 
    with fade 
    "От осознания того факта, что я тут не один, кхм, пережидал радиационную опасность, я вздрогнул." with vpunch
    "Это была не Лена, нет.{w} Это было что-то... Хуже? Лучше? А откуда мне знать?" 
    "О существовании в этом лагере кого-то ещё, кроме Лены и всех тех, чьи имена, повадки и роли улетучились из памяти, я и не подозревал." 
    "Вероятно, так всегда и было?{w} Ведь кто-то же должен был поддерживать видимость отдыха в летнем лагере..?" 
    "Так почему бы этому кому-то не быть этим существом?" 
    "Девушкоподобное, неопрятное, с кошачьими ушками на голове, с длинным хвостом и когтями, существо сильно смахивало на..." 
    me "Ты чёрт." 
    me "А я в аду, наверное..." 
    show uv upset at center zorder 1 with dspr 
    uv "Думай, как знаешь. Только закрой дверь. Нам надо поговорить. Серьезно поговорить." 
    hide uv with dissolve
    th "Думаю, черти дважды не будут так умолительно просить." 
    "Я завернул дверной вентиль до упора и на всякий случай вставил в распорку какую-то прочную на вид железяку." 
    me "Пойдёт?" 
    show uv normal at center zorder 1 with dissolve
    uv "Должно." 
    "Меня слегка задело то, что этот суккуб не удосужился элементарно проверить надёжность моих трудов." 
    "Я опёрся о стену убежища." 
    show uv normal close at center zorder 1 with dspr 
    "Демоница встала напротив, затравленно глядя на меня." 
    uv "Помоги мне. Это в твоих же интересах." 
    "Обычно если кто-то говорил мне, что что-то там в моих интересах, я сразу понимал, что моих интересов в этом совершенно нет." 
    "Но если здесь существовал кто-то ещё, кроме меня и Лены, понимавший, что происходило то, чего не должно было происходить, то это существо явно сейчас находилось передо мной." 
    me "И чем же я могу быть полезен? Душу тебе не продать? Сейчас, погоди, тут где-то гвоздь лежал..." 
    show uv rage close at center zorder 1 with dspr 
    "Существо посмотрело на меня так оскорблённо, словно оно само продавало души оптом." 
    th "Оставь мне за гаражами три грамма душ, они мне еще пригодятся." 
    th "Такие барыги нужны в любом городе, хехе."
    "Я заметил у дальней стены осциллографы, доисторический монитор и прочие приборы, назначение которых я понимал очень смутно." 
    "На мониторе то и дело вспыхивали красные окна со скрученной в мучениях рожицей и знаком ОК." 
    "Курсор сам по себе метался по экрану туда-сюда и приканчивал одну рожицу за другой."
    "Чёрт проследил за моим взглядом и наконец-то приступил к сути дела."
    show uv guilty close at center zorder 1 with dspr 
    uv "Когда-то это была система управления лагерем..." 
    uv "Больше от неё ничего не осталось." 
    show blink zorder 2
    th "Когда-то... Система управления лагерем..." 
    "Вот теперь я точно знал ответ хотя бы на один вопрос." 
    th "На тот, который меня уже не волновал, но лучше поздно, чем никогда." 
    "..."
    "Сложнейшая система управления целым лагерем или же слабенький нетбук школьника, с трудом тянущий видео, - проблемы обычно одни и те же." 
    "Похоже, это от меня и требовалось.{w} Разобраться с этой проблемой.{w} И ведь пронюхала как-то, нечисть." 
    "Единственное, чего она не учла, - того, что любые навыки, если ими не пользоваться, притупляются."
    "Да и похоже, что помочь было уже не в моих силах.{w} Остатки системы умирали." 
    th "Интересно, а как она отреагирует на предложение переустановить оную?" 
    "..."
    th "Хм, а могла ли речь вообще идти об {i}операционках и файлах{/i}?{w} Хотя...{w} если уж она {i}меня{/i} просила, то, скорее всего, могла." 
    th "А вдруг там содержалась и {i}моя память{/i} о более светлых деньках?" 
    "Я потрогал затылок, проверяя, не торчал ли оттуда какой-нибудь {i}чип{/i}."
    "Не торчал.{w} Но меня это не убедило." 
    th "Очень интересно, а память восстановится или перепишется с нуля..?" 
    th "...ладно.{w} Не попробуешь - не узнаешь."
    "Я повернул голову{w=1}{nw}" 
    window hide 
    $ renpy.pause (0.5, hard=True)
    stop music  
    play sound idmt_knife 
    scene idmt_int_catacombs_living_nodoor at idmt_bxw_filter: 
        blur 7
    show idmt_lenacatkiller zorder 1 
    show idmt_blood zorder 2: 
        pos (794, 281) 
    show layer master: 
        truecenter
        zoom 2.5 ypos 0.0 
        ease 10 ypos 1.0 
    with fade 
    $ renpy.pause (10.0, hard=True) 
    window auto 
    extend " и тупо уставился на чертика, из глазницы которого торчало острие ножа.{w} Бедолага даже сказать {i}мяу{/i} не успела." 
    "Стена напротив щерилась пустым дверным проемом, будто ведьма на кострище беззубым ртом.{w} Дверь лежала на полу, но {i}никто из нас вовремя ничего не услышал и не увидел.{/i}"
    "Тело существа оседало на пол, как в замедленной съёмке, а за ним стояла Лена и демонстрировала страшной улыбкой, кто тут настоящая нечистая сила." 
    un "Что же, пора домой. Прости, что торопилась и не успела собрать твои вещи..." 
    "{cps=10}Не подходи.{/cps}" 
    "{cps=10}Не подходи.{/cps}" 
    "{cps=10}Не подхо-{/cps}{nw}" 
    stop ambience
    window hide 
    play sound idmt_glitch2
    scene bg int_catacombs_door at idmt_bxw_filter  
    $ renpy.pause (0.05, hard=True) 
    scene bg int_catacombs_entrance at idmt_bxw_filter
    $ renpy.pause (0.05, hard=True) 
    scene bg int_old_building_night at idmt_bxw_filter 
    $ renpy.pause (0.05, hard=True) 
    scene bg ext_old_building_night_moonlight at idmt_bxw_filter 
    $ renpy.pause (0.05, hard=True) 
    scene bg ext_path2_night at idmt_bxw_filter 
    $ renpy.pause (0.05, hard=True) 
    scene bg ext_path_night at idmt_bxw_filter 
    $ renpy.pause (0.05, hard=True) 
    scene idmt_ext_house_of_un_night at idmt_bxw_filter  
    $ renpy.pause (0.05, hard=True) 
    scene bg ext_camp_entrance_night at idmt_bxw_filter  
    $ renpy.pause (0.05, hard=True) 
    scene bg int_liaz at idmt_dvplicate: 
        matrixcolor SaturationMatrix(0.1) * BrightnessMatrix(-0.1)
    play sound sfx_bus_interior_moving 
    $ renpy.pause (10.0, hard=True) 
    stop sound 
    scene bg semen_room at idmt_bxw_filter 
    $ prolog_time()
    show layer master: 
        blur 10 
        ease 6.66 blur 0
    $ renpy.pause (6.66, hard=True) 
    window auto 
    "Я..." 
    "Я дома?" 
    window hide 
    scene idmt_black
    jump idmt_ch4