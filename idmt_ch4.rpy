label idmt_ch4: 
    $ save_name = "Я умерла... Пленение 'Помощи не дождусь'"
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}Пленение\n\n\n'Помощи не дождусь'{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    hide text with dspr 
    show layer master 
    stop ambience 
    $ renpy.pause (2.5, hard=True) 
    scene bg semen_room at idmt_bxw_filter with fade
    $ renpy.pause (1.5, hard=True) 
    play ambience idmt_wakeup fadein 60.0
    window auto 
    th "Я...{w} {i}действительно в своей квартире{/i}?" 
    th "Неужели проклятый Совёнок решил отпустить меня?" 
    th "Если да, то...{w} почему я не ощущал радости?" 
    th "Одержимость, тревожность и психозы должны были остаться где-то там, но..."
    th "Что если это была очередная ловушка?" 
    "..."
    "Я лежал на кровати, обводя взглядом тускло освещённую комнату." 
    "Вроде именно так тут и должно быть." 
    "Раскиданные повсюду вещи, светящийся монитор компьютера..." 
    th "Он просто ждал, когда я снова за него сяду.{w} Как трогательно." 
    th "Прости, дружище, но придется тебе подождать ещё."
    "Все было знакомо до боли в груди и незнакомо одновременно." 
    "Из коридора тянуло сыростью и затхлостью.{w} Не думаю, чтобы тут когда-то {i}так{/i} пахло." 
    "В мой слух настойчиво пробивались нескончаемые гудки проводного телефона и едва различимый плеск воды." 
    th "В квартире кто-то был?{w} В ванной?" 
    th "Сюрпрайз-сюрпрайз, я вернулся." 
    "Наверное, я и сам был бы рад, если бы прямо сейчас в комнату кто-нибудь зашёл." 
    "Или кто-то ответил бы на звонок." 
    "Но ни того и ни другого не происходило." 
    "Понимание того, что {i}никто никогда не выйдет из ванной{/i}, пришло окольными путями." 
    th "Если я действительно оказался у себя дома, то расходовать воду и прочее электричество - последнее, чего мне бы хотелось." 
    th "Там, кстати, случайно нигде не оставлен открытым газ?" 
    "Мелкие, подвижные, деятельные мысли ненадолго захватили сознание. Моё тело поднялось." 
    th "Именно так все это и воспринималось.{w} Словно поднялось лишь тело, а сам я остался лежать." 
    play ambience sfx_water_sink_stream 
    play music idmt_devil
    scene idmt_bathdoor with fade
    "Через несколько секунд я стоял у двери ванной, вслушивался в монотонный шум льющейся воды, шумно вдыхал сырой смрадный воздух и остро понимал две вещи." 
    th "Первое: холодная вода намочила мои ступни."
    th "Второе: всё моё существо противилось тому, чтобы войти внутрь." 
    "И только рука, та самая, которая постоянно болела, тянулась к ручке двери независимо от моих желаний и нежеланий." 
    $ witchhouse_shake = 1.25 
    show idmt_bathdoor zorder 1 at idmt_mshake: 
        truecenter 
        zoom 1.03 
    with dspr 
    play sound sfx_knock_door_closed_hard2
    "С каждым дёрганием ручки через руку проходил разряд боли." with vpunch
    play sound sfx_knock_door_closed_hard2
    th "Мне, может, и не хотелось в ванную, но хлипкая дверь всё равно не поддавалась." with vpunch
    window hide 
    $ renpy.pause (2.5, hard=True)
    show blink zorder 2 
    $ renpy.pause (1.5, hard=True) 
    window auto 
    "Я осознал, что лежал, уткнувшись лицом в пол." 
    "Вода заливалась мне в уши.{w} Я захлёбывался." 
    "Кое-как мне удалось встать." 
    hide blink 
    show unblink zorder 2 
    extend " На мгновение у меня возникла безумная идея попытаться посмотреть в зазор, из которого хлестала вода." 
    "Либо же просунуть туда что-нибудь длинное и попытаться подцепить защёлку изнутри." 
    th "Но так ли сильно мне нужно было знать, кто заперся в моей собственной ванной и не выходил?" 
    "Мой дом перестал быть моей крепостью, а темнота снова пугала.{w} Сильнее, чем в былые времена." 
    "К компьютеру даже мысли не возникло подойти."
    "Содрогнувшись от звука, я открыл входную дверь.{w} Она, в отличие от двери ванной, совершенно не сопротивлялась." 
    th "Бегу из дома.{w} Снова."
    play sound sfx_water_emerge 
    play ambience idmt_waterdrops 
    scene idmt_int_etage with dissolve 
    "Поток воды, уже поднявшейся мне выше уровня щиколоток, мерзко зажурчал и хлынул на лестничную клетку, инфернальным водопадом стекая вниз." 
    "Хоть я и покинул нехорошую квартиру, мне легче не стало. Напротив." 
    "В подъезде пахло разложением."
    "Свет на лестничной клетке нервно вспыхивал и гас." 
    "Двери квартир были раскрыты нараспашку.{w} Мне не хотелось заходить внутрь даже не из-за того, что там была частная собственность." 
    "Дверные проемы зияли сосущей бездонной пустотой, по полу тянулись тёмные полузасохшие следы." 
    "Отчаянно хотелось, чтобы плеск воды внизу прекратился.{w} Но, судя по эху, первый этаж был затоплен." 
    scene idmt_ext_emptytown 
    show idmt_int_entrance zorder 1 
    show layer master: 
        zoom 1.05 anchor (48, 27)
        ease 0.10 pos (0,0)
        ease 0.10 pos (25, 25)
        ease 0.10 pos (0, 0)
        ease 0.10 pos (-25, 25)
        repeat
    with dissolve 
    play sound sfx_run_forest
    "Лифт не работал."
    "Я побежал вниз со всех ног, прыгая с верхней ступени лестницы на нижнюю, спотыкаясь, больно падая, вставая и продолжая бежать дальше, лишь бы побыстрее покинуть это место." 
    stop sound fadeout 1.5 
    scene idmt_int_firstetage 
    show layer master at idmt_bloodlake
    with dissolve 
    play ambience ambience_boat_station_night 
    "Уже внизу я на полном ходу вбежал по пояс во что-то... неожиданно теплое." 
    "Это явно была не вода.{w} Вот и всё, что я мог сказать о природе стихийно возникшего затопления в подъезде." 
    "Хотя предположения у меня появились буквально сразу же." 
    "..." 
    window hide 
    stop music fadeout 2.5 
    $ renpy.pause (2.5, hard=True) 
    show idmt_ext_emptytown2 zorder 2 
    with dissolve 
    $ renpy.pause (2.5, hard=True) 
    play music idmt_sicksociety 
    window auto 
    "Наружу я все же вышел.{w} Или выплыл."
    "Осмотревшись, я не смог узнать родной двор, улицу, город..." 
    me "Н-на мес-сте Моск-квы долж-жно б-было стать ог-громное озеро..." with vpunch
    "И оно там стало.{w} Хотя и на 70 лет позже, чем планировалось, может, не самыми лучшими, но все же людьми." 
    "До меня не сразу дошло, что часть тела, возвышавшаяся над уровнем нерукотворного {i}нечто{/i}, замёрзла." 
    "Не самая подходящая ситуация, но мне в этот миг пришло на ум, что я делал правильно, следуя советам древних мудрецов и держа голову в холоде, а ноги в тепле." 
    th "Если слово {i}правильно{/i} тут вообще было уместно." 
    "..." 
    th "Хм, а ведь, следуя логике вещей, всё это, чем бы оно ни являлось, должно было растопить снег и уйти в ливневые канализации." 
    "..." 
    th "К черту логику.{w} Неужели я до сих пор так и не смог этого понять?{w} Она больше не действовала.{w} Нигде." 
    th "Хорошо там, где меня нет.{w} В буквальном смысле."
    "Мои ноги превращались в ил, а туловище тончайшим слоем льда размазывалось по поверхности." 
    "Лишившийся пристанища скорбный дух просто держал путь куда-то, лавируя между домов, появлявшихся в этой вечной темноте внезапно, как айсберги." 
    th "Но разве он не должен просто проходить сквозь стены?" 
    th "Разве холод не должен исчезнуть...{w} разве страх не должен уйти...{w} разве сумасшествие не должно иметь пределов..." 
    th "Разве не должна утихнуть эта чёртова боль..." 
    window hide 
    scene idmt_black
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}Тёплая вода, полумрак и ************ ************\nнаконец подарили мне покой.{/size}{/font}") zorder 1 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}Может быть, я никогда и не был в том пионерлагере.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}А может, я и не возвращался обратно.{/size}{/font}") zorder 1 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr 
    $ renpy.pause () 
    play ambience ambience_boat_station_night 
    scene idmt_bus_stop zorder 3 
    show layer master at idmt_bloodlake
    $ renpy.pause (2.5, hard=True)
    window auto 
    "Я сам не заметил, как оказался у автобусной остановки." 
    "Только там ко мне понемногу начало возвращаться некое подобие ясности мышления." 
    "Может быть, последние искорки угасшего навеки рассудка."
    "Зайдя под козырёк, я присел, оказавшись в озере уже по плечи." 
    "Поверхность поблескивала красноватыми искрами, а обоняние уже привыкло к царившему повсюду запаху тлена." 
    window hide 
    show blink zorder 2 onlayer widgetoverlay
    $ renpy.pause (2.5, hard=True) 
    play sound sfx_owl_far 
    $ renpy.pause (2.5, hard=True) 
    window auto 
    th "{i}И здесь тоже???{/i}" 
    window hide 
    $ renpy.pause (2.5, hard=True) 
    hide blink onlayer widgetoverlay 
    show un normal coat1 at center zorder 1 onlayer widgetoverlay
    show unblink zorder 2 onlayer widgetoverlay 
    $ renpy.pause (2.5, hard=True) 
    window auto 
    "Я поднял взгляд." 
    "Лена.{w} Ну конечно же.{w} Кого я ещё должен был ждать?" 
    "Она, в отличие от меня, прекрасно соблюдала все условности {i}холодной погоды{/i}, тепло одевшись." 
    "Все, кроме одной-единственной." 
    "Она высилась надо мной, стоя прямо на кровавой глади." 
    th "Будто святая." 
    show un angry coat3 at center zorder 1 onlayer widgetoverlay with dspr
    un "Они все просто уехали." 
    "Я закатил глаза."  
    show un sad coat2 at center zorder 1 onlayer widgetoverlay with dspr 
    un "Извини." 
    un "Они очень не хотели уезжать отсюда.{w} {cps=10}Но я была настойчива.{/cps}" 
    me "А ты не находишь, что это несколько..." 
    "Мой голос утонул в горле, не дав мне закончить фразу." 
    show un serious coat3 at center zorder 1 onlayer widgetoverlay with dspr
    un "Да нет, ни капельки." 
    un "Что хорошо - так это то, что теперь ни время, ни дата могут не волновать ни тебя, ни меня."
    "Я внимательно посмотрел на Лену." 
    th "Ну, придушить больше не пыталась, и то ладно."
    "Вообще, на её лице за всё время нашего разговора не промелькнуло ни единой эмоции." 
    me "Может, скажешь мне уже наконец-то, причем тут я?" 
    show un grin coat3 at center zorder 1 onlayer widgetoverlay with dspr
    un "Может, и скажу." 
    show un normal coat1 at center zorder 1 onlayer widgetoverlay with dspr
    un "Но мне было бы приятнее думать, что ты сам догадаешься." 
    un "Ведь это во многом твоя вина." 
    me "Ты бредишь." 
    show un serious coat3 at center zorder 1 onlayer widgetoverlay with dspr 
    un "Ничуть."
    un "Видишь ли, я тоже ищу ответы." 
    un "Всегда есть приёмы, чтобы добиться их." 
    show un angry coat3 at center zorder 1 onlayer widgetoverlay with dspr 
    un "Так что...{w} хотя бы сейчас не расстраивай меня." 
    th "{i}Ответы{/i}...{w} Такое знакомое слово.{w} Чуточку {i}слишком{/i} знакомое." 
    "Внутри меня шевельнулась какая-то своеобразная вина, когда я услышал, что, оказывается, не я один их искал." 
    "Вот только она, по всей видимости, их нашла, в отличие от меня." 
    "Лена...{w} Отталкивающая, одержимая, неспособная найти покой..." 
    "А способен ли я сам освободиться?{w} Или уже нет???" 
    "Кажется, осталось совсем немного - и точка невозврата будет пройдена.{w} Что же, тогда..."
    me "Просто расскажи все, как есть." 
    show un shy coat1 at center zorder 1 onlayer widgetoverlay with dspr 
    "Вместо ответа девушка театрально обвела руками залитое кровью пространство и сделала самое смущённое лицо, на которое была способна." 
    un "Я... стесняюсь говорить такое {i}при людях{/i}." 
    show blink zorder 2 onlayer widgetoverlay  
    "Поверхность кровавого озера отозвалась тихим плеском, когда я вытащил из него руку и схватился ладонью за голову." 
    th "Наверняка, в этот момент я стал похож на орка с отпечатком ладони на лице." 
    "..." 
    th "Ответом Лены был... я?" 
    th "И так ли уж мне хотелось бы это услышать, если дело было именно в этом?" 
    th "Но не останавливаться же на полпути?" 
    "..."
    "А что думал о ней я сам?" 
    "{i}Когда-то что-то наверняка думал...{/i}"
    hide un onlayer widgetoverlay 
    "А пошло оно всё."
    "Мне просто хотелось проснуться в блаженном неведении.{w} Или же наоборот, уснуть." 
    th "Просто исчезнуть из этой системы вещей, в которой грань кошмара и реальности настолько размыта." 
    stop music fadeout 3.5 
    "Мне хотелось слишком многого."
    "И в этот миг, когда казалось, что нужен лишь один выдох грудного младенца, чтобы шарик размером с Землю лопнул," 
    window hide 
    $ renpy.pause (2.5, hard=True) 
    play sound_loop sfx_bus_idle  
    $ renpy.music.set_volume(0.15, delay=0.001, channel="sound_loop") 
    $ renpy.pause (2.5, hard=True) 
    window show
    extend " вдалеке в абсолютно пустом залитом кровью мире раздался рёв мотора." 
    $ renpy.music.set_volume(0.25, delay=0.001, channel="sound_loop")
    "Когда его источник прибудет сюда, я могу сколько угодно не двигаться с места.{w} Этому летучему голландцу с призрачными пассажирами внутри, давным-давно отыгравшими свои роли, торопиться больше некуда." 
    "Он дождётся, когда я сдамся и сяду внутрь, в один конец, туда, где хранились мои самые страшные воспоминания." 
    $ renpy.music.set_volume(0.4, delay=0.001, channel="sound_loop")
    hide blink onlayer widgetoverlay
    show unblink zorder 2 onlayer widgetoverlay 
    "Я открыл глаза.{w} Пустота в том месте, где миг назад стояла Лена, отзывалась болью в зрачках." 
    th "Куда она исчезла за это время?" 
    "..." 
    $ renpy.music.set_volume(1.0, delay=0.001, channel="sound_loop") 
    scene idmt_ext_410 at idmt_blvrred
    with dissolve 
    "Ладно. Автобус уже стоял на остановке передо мной, гостеприимно распахнув свои двери." 
    "А Лена появлялась и исчезала уже несчётное число раз.{w} И лишь это исчезновение оставило после себя тягостное предчувствие."
    "Сиденья находились довольно высоко, чтобы кровь почти не заливалась внутрь.{w} Но какая разница..." 
    "..." 
    window hide 
    stop sound_loop fadeout 4.5 
    stop ambience fadeout 4.5
    scene idmt_black with Dissolve(4.5) 
    $ renpy.pause (2.5, hard=True)  
    play ambience idmt_vinyl 
    play music idmt_help fadein 1.5 
    scene idmt_white
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Знаешь, когда логические объяснения бессильны,\nначинаешь искать какие угодно.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Просто представь себе, что ты\nглавный герой в какой-нибудь игре.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text 
    show idmt_flashbacks_slide zorder 1
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Собираешь симпатии по одной.\nОткрываешь самые разные хорошие концовки.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Распробовав всё, что могла предложить эта игра,\nты так и не решил,\nкакой опыт был для тебя наиболее ценным.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}А, может, просто не помнишь подробностей прошлых опытов.\nПомнишь лишь в общих чертах, что после каждого из них\n ты изменялся изнутри в лучшую сторону.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Да ещё и жизнь доживал не один.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    $ renpy.music.set_volume(0.0, channel="music")
    scene idmt_daysky_bg  
    play ambience ambience_forest_day 
    $ renpy.pause(7.5, hard=True) 
    scene idmt_white 
    $ renpy.music.set_volume(1.0, channel="music")
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0) 
    show idmt_flashback_all zorder 1
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Но теперь ты можешь быть награждён.{/color}{/size}{/font}") zorder 2 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Ты можешь открыть общую концовку, самую хорошую.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    $ renpy.music.set_volume(0.0, channel="music")
    scene idmt_eveningsky_bg 
    play ambience ambience_forest_evening 
    $ renpy.pause(7.5, hard=True) 
    scene idmt_white 
    play ambience idmt_vinyl 
    $ renpy.music.set_volume(1.0, channel="music")
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0) 
    show idmt_flashback_deadlena zorder 1
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Однако, кроме хороших концовок, есть и плохие.{/color}{/size}{/font}") zorder 2 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Когда ты теряешь всё или почти всё, что имел.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}С каждой такой потерей ты приближаешь одну,\nсамую большую.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Наши судьбы скрутятся, как лента Мёбиуса.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text 
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Если разрезать её вдоль, получится не две ленты, а одна.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Никого больше не останется.\nДаже их имена сотрутся из памяти за дальнейшей ненадобностью.{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    hide text  
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=40}{color=#000000}Останусь только я.\nЛишь затем, чтобы ещё один раз умереть на твоих руках...{/color}{/size}{/font}") zorder 2 at truecenter: 
        idmt_dizzy(2.5, 2.5) 
    with dspr
    $ renpy.pause() 
    stop ambience 
    scene idmt_lightningsky_bg 
    play music idmt_meetmethere 
    $ renpy.pause (7.5, hard=True) 
    scene idmt_black
    jump idmt_ch5