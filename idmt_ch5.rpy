label idmt_ch5: 
    $ save_name = "Я умерла... Решение 'Мертвые пациенты'"
    $ day_time() 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}Решение\n\n\n'Мертвые пациенты'{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    hide text with dspr 
    show layer master 
    $ renpy.pause (2.5) 
    play sound_loop sfx_bus_interior_moving fadein 1.5
    scene idmt_int_bus_lastact with fade: 
        zoom 1.10 anchor (48, 27)
        linear 0.1 pos (0,2)
        linear 0.1 pos (0,0)
        linear 0.1 pos (2,0)
        linear 0.1 pos (0,0) 
        repeat 
    $ renpy.pause (2.5, hard=True) 
    window show 
    "Я полусидел-полулежал в салоне автобуса и преисполнялся отчаянием." 
    "Оно лишь усиливалось, вытесняя из сознания всё, что когда-то делало меня человеком." 
    window hide
    stop sound_loop 
    scene idmt_int_bus_lastact with vpunch
    play sound sfx_bus_stop 
    $ renpy.pause (4.5, hard=True)
    play sound sfx_ikarus_open_doors 
    window show 
    "Двери распахнулись.{w} Споткнувшись на ступеньках, я вывалился из автобуса и упал на колени перед воротами проклятого лагеря." 
    scene idmt_ext_gates_lastact with dissolve 
    "Ждать тут было нечего и некого.{w} Незапертые ржавые ворота молча приглашали меня внутрь моей камеры пыток." 
    "Никаких возражений придумать мне было не под силу." 
    "Животный ужас погнал меня вперёд..."
    scene idmt_ext_square_lastact 
    show layer master:
        zoom 1.10 anchor (48, 27)
        ease 0.10 pos (0,0)
        ease 0.10 pos (25, 25)
        ease 0.10 pos (0, 0)
        ease 0.10 pos (-25, 25)
        repeat 
    with dissolve
    "На полной скорости мимо пустой, поросшей не иначе как асфоделями площади и печально повисших флагов..." 
    th "Здесь пушкина некому было оборонять, вот и повалился." 
    th "Больше не осталось никаких следов этой борьбы, останков неизвестных солдат - местных жителей - и памяти о них." 
    show idmt_ext_house_of_dv_lastact zorder 1 with dissolve 
    "Оставлен позади домик с недобро сверкавшим пустыми глазницами Весёлым Роджером на дверях." 
    th "Как будто тут им было от чего сверкать." 
    th "Любая отражающая поверхность без излучения лишена смысла." 
    th "Еще чуть-чуть - и где-то там, в домике на окраине лагеря, окончательно пропадёт {i}мой собственный{/i} смысл." 
    "Я уже знал, что мне предстояло там увидеть." 
    "Я помнил от начала и до конца нашу с ней короткую историю." 
    "Я..."
    scene idmt_ext_house_of_un_day_lastact with dissolve 
    "Вот и он. Домик Лены.{w} Двери на месте, хотя и не закрыты." 
    show blink 
    "Закрыв глаза, я шагнул внутрь." 
    th "А того, чего ты не видишь, попросту не существует." 
    un "Ну, вот мы и встретились. На том же месте, в тот же час, да?" 
    window hide
    scene cg d7_un_suicide:
        pos (0,-360)
        linear 10.0 pos (0,0) 
    show unblink  
    $ renpy.pause (10.0, hard=True) 
    window show 
    "Голос Лены был совершенно безразличен и в то же время нёс в себе долю какой-то насмешки." 
    "На ее руке, свисавшей с кровати, почти не осталось целых участков." 
    "Я топтался на месте.{w} Перебивая душевные терзания, мой мозг настойчиво сверлила жгучая боль ниже локтя." 
    "Да так, что мне было бы куда легче, попадись я прямо сейчас Джеффри Дамеру."
    un "Только, прошу тебя, хотя бы сейчас заткнись. Я не знаю, сколько мне осталось." 
    "Это было явно излишне.{w} Тяжело вздохнув, покачнувшись в кровати и скривившись, Лена продолжила." 
    un "Вот и всё... Странно, что я надеялась на что-то другое. Ты-то, я смотрю, не надеялся вообще ни на что." 
    un "Этот лагерь..." 
    un "Для тебя он создавал одни иллюзии, не дававшие тебе покоя, а для меня - другие. Ведь так?" 
    un "Только не думай, что это тебя может как-то оправдать."
    un "Мне казалось, что я потеряла тебя навсегда... Вернее, даже не тебя." 
    un "В один прекрасный момент я помрачилась рассудком и начала... нет, убить хотя бы какую-то частичку этого кошмара невозможно. Но я пыталась." 
    un "Однако всё всегда кончалось для меня одинаково." 
    "Разрезанная рука девушки дрогнула."
    un "Не получая никаких ответов на свои вопросы, я вновь и вновь избавлялась от этих поисков как умела... но всё лишь начиналось заново." 
    un "Пока однажды я не повстречала жалкую пародию на прежнего тебя." 
    un "Ты тыкался куда угодно, только меня обходил стороной. Ты был потерян и ничтожен." 
    un "Может, поэтому мне и хотелось придушить и тебя заодно? Но я не сумела."
    un "Это я сломала систему лагеря." 
    un "В очередной раз оказавшись {i}с той стороны{/i}, я как-то умудрилась... удалить всего одну букву из её узора." 
    un "Я так надеялась, что хоть какие-нибудь сдвиги это за собой повлечёт; на остальное мне было плевать." 
    un "Не особо-то это и помогло." 
    un "Думала, что ты поймёшь хоть что-то, оказавшись там, поэтому и дала тебе {i}яблочный сок{/i}." 
    un "Я так хотела, чтобы ты {i}это{/i} увидел..."
    un "Я вот думаю, может быть, тебе все же стоило попытаться спасти эту дохлую кошку? Тогда хотя бы ты смог бы двинуться дальше, учтя свои прошлые ошибки..." 
    un "Но куда там, ты и сам себя спасти был неспособен. А мне...{w} мне не привыкать." 
    un "Ты просто нереально слаб и туп; я даже не знаю, понял ли ты хотя бы слово из того, что я сказала." 
    un "Что с тобой, что без тебя, это проклятый замкнутый круг." 
    un "И всё равно, я всегда буду тянуться к тебе. А ты всегда будешь избегать меня." 
    un "Грёбаные тайминги..." #rip Sea of members </3
    "Я бы сказал, что я понял слишком много, ещё находясь в автобусе. И все же..." 
    "Как бы грубо это ни было, мне ли жаловаться. У Лены, в отличие от меня, {i}были все основания на грубость{/i}." 
    th "Больше у неё ничего не осталось.{w} Как и у меня." 
    me "Ты просто больная... ты больная." 
    me "Хранить яблочный сок в аптечке..."
    un "Это {i}ты{/i} больной." 
    "..." 
    "Будь иначе, вряд ли бы её голос был так спокоен.{w} Так кто все же тут больной, она или я?" 
    th "И кто тут вообще кто?" 
    "Всё, как она и говорила. Я всегда буду более виноват, более труслив, более... Мне от этого {i}уже не деться никуда{/i}."
    un "В аду никогда не встретить ни родных, ни близких." 
    un "Я все же встретила тебя. Но ты совсем не тот." 
    un "Почему именно ты? Что и кому я сделала, чтобы заслужить такую участь?" with vpunch
    "Белое лицо Лены, казалось, светилось от святой ненависти в комнатке, где больше не было и не могло быть никакого света.{w} А в уголках её глаз скопились слезы." 
    "Голос девушки то становился едва слышным, то истерически возвышался и гремел, как адский колокол." 
    "Как светлая и тёмная сторона Луны.{w} Преданность и одержимость."
    un "И всё равно я бы вырезала весь мир... ради твоей любви..." 
    "А вот это было уже чересчур." 
    "И без разницы, насколько сильна была моя вина перед нею."
    me "ТЫ ПОЕХАВШАЯ!!! ТЫ ЭТО ПОНИМАЕШЬ?" with vpunch
    me "ТЫ И БЫЛА МОИМ МИРОМ!!! ОТ НАЧАЛА И ДО КОНЦА!!! ЧЁРТ ПОБЕРИ, ПРОСТО ЗАЧЕМ, СКАЖИ!!!" with vpunch 
    me "Я ведь тоже теперь..." 
    "Мой голос поник.{w} Я уже и не чаял услышать больше, чем услышал {i}тогда{/i}."
    un "Всё же ты не понял... Прости, что обманула твои ожидания..." 
    un "{cps=15}Ведь именно поэтому...{/cps}" 
    un "{cps=10}...{i}я себя{/i} и вырезала...{/cps}" 
    window hide
    stop music 
    play sound sfx_ghost_children_laugh 
    show text ("{size=66}{b}{color=#ff0000}АХАХАХАХАХАХА{/color}{/b}{/size}") zorder 2: 
        pos (600, 300) 
        parallel: 
            zoom 0.2 
            ease 0.5 zoom 0.8 
        parallel: 
            alpha 1.0 
            ease 0.5 alpha 0.0 
    $ renpy.pause (0.1, hard=True)
    show text ("{size=66}{b}{color=#b30900}АХАХАХАХАХАХА{/color}{/b}{/size}") as text2 zorder 2: 
        pos (1320, 780) 
        parallel: 
            zoom 0.2 
            ease 0.5 zoom 0.8 
        parallel: 
            alpha 1.0 
            ease 0.5 alpha 0.0 
    $ renpy.pause (0.1, hard=True) 
    show text ("{size=66}{b}{color=#b30900}АХАХАХАХАХАХА{/color}{/b}{/size}") as text3 zorder 2: 
        pos (600, 780) 
        parallel: 
            zoom 0.2 
            ease 0.5 zoom 0.8 
        parallel: 
            alpha 1.0 
            ease 0.5 alpha 0.0 
    $ renpy.pause (0.1, hard=True) 
    show text ("{size=66}{b}{color=#b30900}АХАХАХАХАХАХА{/color}{/b}{/size}") as text4 zorder 2: 
        pos (1320, 300) 
        parallel: 
            zoom 0.2 
            ease 0.5 zoom 0.8 
        parallel: 
            alpha 1.0 
            ease 0.5 alpha 0.0 
    $ renpy.pause (0.1, hard=True) 
    show text ("{size=66}{b}{color=#b30900}АХАХАХАХАХАХА{/color}{/b}{/size}") as text5 zorder 2: 
        pos (960, 540) 
        parallel: 
            zoom 0.2 
            ease 0.5 zoom 0.8 
        parallel: 
            alpha 1.0 
            ease 0.5 alpha 0.0 
    $ renpy.pause (0.6, hard=True) 
    hide text1 
    hide text2 
    hide text3 
    hide text4 
    hide text5 
    show layer master: 
        truecenter 
        zoom 1.11 
        easein 8 zoom 1.0
    show cg d7_un_suicide with Shake((1, 1, 2, 2), 8.0, dist=30) 
    scene cg d7_un_suicide at idmt_blvrred zorder 2 with dissolve 
    $ renpy.pause (6.66, hard=True) 
    scene idmt_white 
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0) 
    $ renpy.pause (6.66, hard=True) 
    play music idmt_deadpatients 
    $ renpy.pause (1.5, hard=True)
    show idmt_flashback_lena1 zorder 1
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы наши жизни тратили впустую.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы сожалеем, что позволили нашему страху\nи самодовольству управлять нами.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text  
    hide idmt_flashback_lena1 
    show idmt_flashback_lena2 zorder 1
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы не заходили достаточно далеко.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы не жили достаточно.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы не любили достаточно.\nМы не рисковали.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы держали рты на замке и не говорили того,\nчто действительно хотели сказать.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text 
    hide idmt_flashback_lena2 
    show idmt_flashback_lena3 zorder 1 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы должны были больше доверяться,\nбольше верить,\nсмеяться больше,\nлюбить больше.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Мы должны были больше рисковать,\nжить жизнью во всей ее полноте.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text 
    hide idmt_flashback_lena3 
    show idmt_flashback_lena4 zorder 1 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Больше путешествовать,\nменьше работать,\nбольше заниматься сексом.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text with dissolve 
    $ renpy.pause (13.0, hard=True) 
    hide idmt_flashback_lena4 
    show idmt_flashback_final zorder 1 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Для нас уже очень поздно.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dissolve
    $ renpy.pause() 
    hide text with dissolve 
    $ renpy.pause (3.3, hard=True)  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Поздно.{/color}{/size}{/font}") zorder 2 at truecenter with dissolve: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text with dissolve 
    $ renpy.pause (3.3, hard=True)  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Поздно.{/color}{/size}{/font}") zorder 2 at truecenter with dissolve: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text with dissolve 
    $ renpy.pause (3.3, hard=True) 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Поздно.{/color}{/size}{/font}") zorder 2 at truecenter with dissolve: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text with dissolve 
    $ renpy.pause (3.3, hard=True)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Очень поздно.{/color}{/size}{/font}") zorder 2 at truecenter with dissolve: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text with dissolve 
    stop music fadeout 3.5 
    stop ambience fadeout 3.5
    scene idmt_black with Dissolve(3.5) 
    $ renpy.pause (4.5, hard=True) 
    play music idmt_deathvinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}В аду никогда не встретить ни родных, ни близких.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}Я всё же встретил тебя.\nНо ты совсем не та.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause () 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}Я не сумел спасти тебя от тебя самой.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause () 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}Моё последнее желание не исполнилось.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause () 
    hide text with dspr
    show layer master 
    $ renpy.pause (2.5, hard=True)
    scene cg epilogue_un_bad_red with fade 
    $ prolog_time() 
    $ renpy.pause (2.5, hard=True) 
    window show
    me "{cps=10}Что же ты мне расскажешь, Лена...{/cps}" 
    me "{cps=10}Не поверишь, мне вдруг столько всего захотелось у тебя спросить.{/cps}" 
    me "{cps=10}Только ты это, не томи.{/cps}" 
    me "{cps=10}А то мне это...{w} спать охота...{/cps}{nw}" 
    window hide
    $ renpy.pause() 
    stop music 
    scene idmt_white with fade 
    $ renpy.pause (2.5, hard=True) 
    play music idmt_idiedamilliontimes 
    $ renpy.pause (2.5, hard=True)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Сценарий, кодинг\n\nMyLastWitchout{/color}{/size}{/font}") at truecenter with dissolve 
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Оригинальная вселенная\n\nSovietGames{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Вдохновение\n\nТворчество проекта Радость Моя\nРоман Т. Толстой 'Кысь'\nФильм Луиса Бунюэля 'Андалузский пёс'{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Музыка\n\nРадость Моя\nBetween August And December\nКвiтка Цiсик{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Визуальная составляющая взята из модов\n\n7ДЛ Lost Alpha\nНедостающее Звено Другого Мира\nБесконечное Лето 3D{/color}{/size}{/font}") at truecenter 
    with dissolve
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Арт\n\nwhale dream{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Благодарности следующим людям\n\nUnnamed Autor\nTaurus_4Life\nMadGun1337\nРоман Лиманский\nKiller Play\nАртур Мамедов{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}И Тебе - за то, что прочитал модификацию до конца.{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Если понравилось, поставь лайк и напиши комментарий.{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause () 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}КОНЕЦ.{/color}{/size}{/font}") at truecenter 
    with dissolve 
    $ renpy.pause ()
    hide text with dissolve 
    return
