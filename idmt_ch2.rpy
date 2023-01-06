label idmt_ch2: 
    $ save_name = "Я умерла... Сочетание 'Считалка'"
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}Сочетание\n\n\n'Считалка'{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    hide text with dspr 
    show layer master 
    stop ambience 
    $ renpy.pause (2.5, hard=True)
    window show 
    "Я медленно выныривал из глубин какого-то страшного сна." 
    "Где-то на периферии сознания всё еще мелькали его разрозненные отрывки." 
    "Не получалось ни вздохнуть, ни пошевелиться, ни открыть глаза, ни просто подумать о чём-то.{w} И это совершенно не волновало меня." 
    "..." 
    window hide 
    $ renpy.pause (4.5, hard=True) 
    play ambience idmt_int_cabin_night_reverb
    scene idmt_int_house_of_un_night 
    show layer master: 
        blur 15
    show idmt_int_house_of_un_night as idmtbginthouseofunnight zorder 1: 
        alpha 0.25 
        idmt_dizzy (2.5, 2.5) 
    show un serious pioneer zorder 2 at center: 
        matrixcolor BrightnessMatrix(-1.0)
    camera: 
        perspective True 
        zpos -750 ypos -50 matrixtransform RotateMatrix (0,0,-30) 
    show unblink onlayer widgetoverlay 
    $ renpy.pause (2.5, hard=True) 
    window show 
    "Контроль над телом и его функциями возвращался медленно и болезненно."
    "Кое-как разлепив веки, я смог лишь понять, что чей-то тёмный силуэт стоял прямо передо мной.{w} Всё вокруг тонуло в каком-то тумане." 
    "Во рту начало ощущаться противное послевкусие... домашнего самогона, в который чего только не добавляли для крепости.{w} Серьёзно?" 
    th "Это что же получается..." 
    th "Ну, кажется, кое-что прояснилось.{w} Перебрал - так перебрал.{w} Сильнее любой свиньи.{w} Надо это признать." 
    show un serious pioneer zorder 2 at center: 
        matrixcolor BrightnessMatrix(-1.0) 
        ease 5 matrixcolor BrightnessMatrix(-0.6) 
    "Силуэт передо мной постепенно становился более чётким.{w} Спина ощущала под собой пружинистую и якобы мягкую опору." 
    "Я лежал на кровати.{w} А надо мной склонилось озабоченное лицо...{nw}" 
    window hide 
    camera: 
        perspective True 
        zpos -750 ypos -50 matrixtransform RotateMatrix (0,0,-30) 
        ease 5 zpos 0 ypos 0 matrixtransform RotateMatrix (0,0,0) 
    show layer master: 
        blur 15 
        ease 5 blur 0 
    show un serious pioneer zorder 2 at center: 
        matrixcolor BrightnessMatrix(-0.6) 
        ease 5 matrixcolor BrightnessMatrix(0.0) 
    stop ambience fadeout 5.0 
    $ renpy.pause (5.0, hard=True) 
    play ambience ambience_int_cabin_night 
    play music idmt_sdneirfebstel 
    window show 
    extend " Лены?" 
    th "Ну да, её.{w} Значит, и домик её?{w} Но как..." 
    "Мысли шевелились внутри моей черепной коробки, как умирающие гусеницы в опрысканных яблоках."
    "Зелёные глаза девушки глядели устало и укоряюще.{w} Даже сквозь дурноту я не мог не почувствовать укол совести, посмотрев на Лену в ответ." 
    th "Не совсем пропащий, похоже." 
    hide idmtbginthouseofunnight with dissolve
    "Моих сил и угрызений совести хватило ровно на то, чтобы я слегка дёрнулся и что-то слабо простонал." with vpunch
    un "Ну наконец-то." 
    show blink zorder 3 
    "Я промолчал.{w} Мне нечего было сказать в своё оправдание." 
    th "Напился - веди себя прилично."
    "Хотя, по правде говоря, я не мог вспомнить обстоятельств лагерного застолья, хоть убей." 
    "..."
    th "Как будто слабого состояния и мерзкого послевкусия во рту было недостаточно, чтобы с уверенностью сказать, что я пил." 
    th "В лагере мест, где можно было бы распить бутылочку, не рискуя быть пойманным со всеми вытекающими, было мало." 
    th "Отлучки рано или поздно стали бы заметны и ко мне неминуемо появились бы вопросы."
    th "А достать столько спиртного, чтобы от него так свалило, было и вовсе нереально." 
    th "Хотя с такой дозы велик шанс и не дожить до вечера." 
    "Что же, способность выстраивать логические цепочки осталась при мне.{w} Но в конце концов, мои размышления зашли в тупик." 
    "..."
    "Этот {i}сон{/i}...{w} Это действительно был просто сон?" 
    "Кажется, я от кого-то пытался убежать.{w} А попал..." 
    th "{i}Кажется, я всё ещё убегал{/i}."
    window hide 
    $ renpy.pause (3.5, hard=True) 
    stop music 
    scene idmt_white 
    play ambience idmt_vinyl 
    show layer master at idmt_blur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}Ты ровесник мой,\nПокорен и гол,\nЖил и умирал,\nНо ко мне пришел.{/color}{/size}{/font}") zorder 1 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (15.0, hard=True) 
    show layer master at idmt_oldcinema
    show bg int_house_of_un_day zorder 2: 
        blur 3.5 
    show un smile3 pioneer at center zorder 3: 
        blur 3.5 
    play music idmt_reganeet 
    $ renpy.pause (7.5, hard=True)
    stop music 
    scene idmt_int_house_of_un_night 
    play ambience ambience_int_cabin_night 
    $ renpy.pause (3.5, hard=True)
    play music idmt_mantra 
    window show 
    "{i}Вот, опять{/i}."
    "Что-то подобное и было со мной в том сне.{w} Словно на сеансе гипноза, из меня вытягивали сокрытое на самом дне памяти." 
    "Но я точно знал, что {i}этим воспоминаниям неоткуда было взяться{/i}." 
    "Я медленно обвёл взглядом комнату и ничего не мог в ней узнать.{w} Закономерно, ведь {i}я был тут в первый раз{/i}." 
    th "Или же нет?" 
    "..." 
    th "Да к чёрту всё.{w} Слишком много думать вредно для здоровья, как и слишком мало."
    "Может, в глубине души мне и хотелось бы уединения с этой девушкой...{w} Но мне {i}не выпало ни разу за смену{/i} такого шанса." 
    "А в моём теперешнем состоянии об этом нечего было и говорить.{w} Разве что ей самой взбрело бы в голову воспользоваться моей беспомощностью." 
    "Вот только, похоже, она и не собиралась." 
    th "Кажется, меня вело куда-то совсем не в ту степь."
    show un sad pioneer close at center zorder 1 with dissolve 
    un "..."
    me "Ты что-то сказала?" 
    show un grin pioneer close at center zorder 1 with dspr 
    un "Я сказала - как ты себя чувствуешь?" 
    me "Я?...{w} {cps=10}Нормально, наверное{/cps}..." 
    hide un with dissolve
    "Я мог поклясться, что она сказала что-то другое." 
    "Исполненное скорее злобной радости, нежели заботы и участия." 
    "Ладно.{w} Не суть важно." 
    "Сходить с ума было уже достаточно." 
    "Видения, тайны...{w} Что-то третье..." 
    show blink  
    "Мне стало так плохо, что я едва успел склониться над {i}предусмотрительно{/i} поставленным внизу тазиком..." 
    window hide 
    $ renpy.pause (4.5, hard=True) 
    hide blink 
    show unblink  
    $ renpy.pause (1.5, hard=True) 
    window show 
    "Прочистив нутро, я с огромным трудом присел." 
    "По-хорошему, мне надо было бы пойти к умывальникам, но я не мог даже встать." 
    show un sad pioneer at center zorder 1 with dissolve 
    th "Мда... Ну и как я себя при девушке повел?" 
    me "Извини." 
    un "Ну и натворил ты дел." 
    me "Знать бы еще, что я натворил..." 
    show un normal pioneer at center zorder 1 with dspr 
    un "А, так ты ничего не помнишь?" 
    me "А что я должен помнить... Похоже, я перебрал. Но..." 
    "С ответом пионерка задержалась." 
    "..." 
    show un angry2 pioneer at center zorder 1 with dspr 
    un "Не то слово. Ты был настолько в дрова, что тебя чуть в костер не бросили." 
    me "Хорошая шутка.{w} А какой костер?" 
    un "Дааа... {cps=10}Тот, который жгли во время похода.{/cps}{nw}" 
    window hide 
    show layer master: 
        blur 0 
        ease 4.5 blur 10 
    $ renpy.pause (4.5, hard=True) 
    window show 
    extend " Тебе память совсем отшибло?" 
    show blink onlayer widgetoverlay
    th "Поход, значит."
    "По моим прикидкам, это была последняя ночь в лагере.{w} А поход был уже... {i}давно{/i}."
    "Не мог же я проваляться в таком виде в её домике {i}так долго{/i}?" 
    "Не говоря уже о том, чтобы напиваться, считай, перед сауроновым оком вожатой." 
    "Всё совершенно точно было не так. Но..."
    "..." 
    window hide 
    show layer master
    $ renpy.pause (1.5, hard=True) 
    hide blink onlayer widgetoverlay 
    show unblink onlayer widgetoverlay
    $ renpy.pause (1.5, hard=True) 
    window show 
    me "Завтра конец... смены... Поход уже был. Я не мог тут все время проваляться."
    un "Ты бредишь. Конец смены {i}послезавтра{/i}." 
    hide un with dissolve 
    "Развернувшись, Лена поставила точку в едва начавшемся споре и направилась к аптечке." 
    "Меня немного смутило, что на том месте металлического ящичка, где раньше угадывался красный крестик, теперь виднелись довольно глубокие следы ногтей." 
    th "А хотя, что, собственно, с того?{w} Аптечка - она аптечка и есть." 
    th "Да и вроде как именно Лена чаще всего помогала медсестре.{w} Так что доверять ей в этом было можно." 
    "..." 
    show un sad pioneer close at center zorder 1 with dissolve
    un "Пей. Тебе станет легче." 
    play sound sfx_owl_far 
    "Вновь прозвучала безумная серенада моей амнезии." 
    "..." 
    show blink zorder 2 
    "Проглотив какую-то {i}безвкусную{/i} жидкость, я зажмурился и внутри себя наблюдал..."
    "...как {i}облегчение{/i} холодной змеей разносилось по моим кровеносным сосудам, по обожженным нервам, попадало в мозг." 
    "Я абстрагировался от враждебной ко мне действительности как умел." 
    "Абстрагировался от внимательного взгляда холодных зелёных глаз Лены, за которыми, как я подозревал, скрывалось какое-то {i}знание{/i}."
    "Тиканье часов походило на пытку каплями воды, падающими на макушку." 
    show un sad pioneer at center zorder 1
    hide blink 
    show unblink zorder 2 
    "Так и не дождавшись обещанного эффекта плацебо, я не выдержал." 
    me "Как я сюда попал?" 
    show un angry2 pioneer at center zorder 1 with dspr 
    un "Хотелось бы мне и самой это знать; прямо-таки удивительно, как ты в таком состоянии нашёл дорогу {i}домой{/i}."
    th "Что???" 
    me "И как давно здесь мой дом?" 
    show un serious pioneer at center zorder 1 with dspr 
    un "Не поверишь, с самого начала смены." 
    show un normal pioneer at center zorder 1 with dspr 
    un "Ты только не подумай, я и сама была не рада такому расселению. Но так получилось." 
    "Голос её не дрогнул ни разу, пока она это говорила." 
    th "Именно так и вводят обычно человека в заблуждение." 
    "Вот только меня в заблуждение уже было невозможно ввести.{w} Потому что я уже и сам не знал, где правда, а где ложь." 
    "Завтра ли конец смены, здесь ли я жил, пребывал ли я вообще в лагере..." 
    "С каждым мигом, проведенным в этом домике, непонятное беспокойство во мне лишь нарастало." 
    me "Я... пойду домой. Я тут никогда не жил." 
    th "Пойду, ахаха."
    show un rage pioneer at center zorder 1 with dspr 
    un "Куда ты пойдешь?" with vpunch
    show un sad pioneer at center zorder 1 with dspr 
    un "А хотя... иди." 
    me "Так... мне идти или нет?" 
    "Её внезапная вспышка гнева все же сбила меня с толку." 
    "В этом статичном мирке такое проявление эмоций казалось... чем-то действительно настоящим." 
    "Жаль только, что длилось оно всего мгновение." 
    show un serious pioneer at center zorder 1 with dspr 
    un "Как хочешь." 
    me "Но ведь я тут живу. Ты сама сказала." 
    show un angry2 pioneer at center zorder 1 with dspr 
    un "Ты сказал ровно обратное." 
    un "Уходя - уходи." 
    hide un with dissolve 
    "Я послушался, неожиданно легко встал и, развернувшись как сомнамбула, вышел из домика." 
    play sound sfx_open_door_squeak_2 
    window hide 
    stop music fadeout 5.5 
    stop ambience fadeout 5.5 
    scene idmt_black with Dissolve(5.5) 
    $ renpy.pause (7.7, hard=True) 
    window show 
    "..." 
    window hide 
    $ renpy.pause (1.5, hard=True)
    play music idmt_htaednaissur
    $ set_mode_nvl()
    window show 
    "Темнота." 
    "Пустота." 
    "Страх. Бегство из собственного жилища." 
    "Временные петли."  
    "Забвенные миры. Множество миров." 
    "Множественные исходы." 
    "Желание умереть."
    "Лязг ножа. Привкус крови и приятная слабость во всём теле." 
    "Агония, длящаяся вечность."
    "..." 
    "За бесконечно малое мгновение мой разум пропустил через себя йоттабайты информации и, похоже, сгорел." 
    "То, что осталось от него, было способно лишь ощущать бескрайний ужас."
    "..." 
    "Мой сон не был сном."
    "Я... я - это всё ещё я." 
    "Мне нужно что-то простое. Вещественное. Что-то, с чем станет храбрее идти до конца, разобраться во всем происходящем." 
    nvl clear
    window hide  
    $ set_mode_adv() 
    $ renpy.pause (3.5, hard=True)
    window show 
    "Я развернул свое тело к дверному проему, из которого только что вышел." 
    scene expression(idmt_bloodypict("bg int_house_of_un_day")): 
        truecenter 
        zoom 0.47 
    show idmt_ext_house_of_un_night_without_doors zorder 1
    show unblink zorder 2 
    "Рама была пуста.{w} Сквозь неё виднелось нечто, походившее скорее на портал в преисподнюю, чем на комнатку пионерского домика." 
    me "Лена..." 
    me "Лен, подай фонарик..." 
    me "Лен, прекрати дурить." 
    $ witchhouse_shake = 6.66 
    show layer master at idmt_mshake: 
        truecenter 
        zoom 1.05 
    with dspr
    me "ЛЕНА, ВЫНЕСИ ДОЛБАНЫЙ ФОНАРИК, МНЕ СТРАШНО!!!" with vpunch
    "Я кричал во всю мощь голосовых связок, хотя ясно видел, что внутри не было и не могло быть той, кому предназначались эти слова." 
    "Тогда с кем же я разговаривал всего... всего сколько-то там времени назад?" 
    "И двери вроде бы были на месте..." 
    show blink onlayer widgetoverlay
    "Наконец, охрипнув, я опустился на холодную землю, уткнулся головой в колени и заплакал." 
    "Разговор с Леной казался лишним в этом сценарии, словно пьяный писатель всего этого бреда вписал его туда, уже пребывая в состоянии delirium tremens." 
    "Кто-нибудь...{w} что-нибудь...{w} я больше не могу." 
    play sound sfx_owl_far 
    dreamgirl "Кы-ысь... кы-ысь..." 
    th "Только ты одна всегда меня услышишь и придешь..." 
    th "Хоть я от тебя уже до смерти устал." 
    stop music fadeout 4.5 
    window hide 
    $ renpy.pause (6.5, hard=True) 
    play music idmt_skin 
    $ renpy.pause (20.0, hard=True) 
    window show 
    "Все же осмелившись поднять башку, я не смог узнать ничего." 
    window hide 
    $ renpy.pause (1.5, hard=True) 
    hide blink onlayer widgetoverlay 
    scene idmt_black at idmt_mvtrix 
    show unblink zorder 2 
    $ renpy.pause (1.5, hard=True) 
    $ set_mode_nvl()
    window show 
    "Лагерь, его улочки, домики, трава, деревья - всё выглядело как картинка, открытая в текстовом редакторе." 
    th "Удали всего лишь один символ - и изображение станет неузнаваемо, а может, и вовсе не откроется больше. А с ним, наверное, не откроюсь и я." 
    "Здесь, за изнанкой лагеря, я ощутил, как сквозь меня снова прошла волна информации, и в конце концов, я стал её частью." 
    "Я едва осознавал себя, зато впитывал прошлое, настоящее и будущее, как губка." 
    "Меня просто несло в потоке куда-то." 
    nvl clear
    $ set_mode_adv() 
    "Другое такое же отработанное человеческое топливо то и дело проносилось мимо." 
    window hide 
    $ renpy.pause(1.0, hard=True)
    show dv faceless at center: 
        zoom 0.75 xpos 1.15 ypos 0.0 rotate 0 alpha 0.9
        linear 14.0123 xpos -1.16 rotate -90 ypos 0.1
        repeat 
    show mi faceless at center: 
        zoom 0.75 xpos -1.25 ypos 0.1 rotate 0 alpha 0.9
        linear 17.0364 xpos 1.15 rotate 90 ypos 0.2
        repeat 
    show mz faceless at center: 
        zoom 0.75 xpos -1.35 ypos 0.3 rotate 0 alpha 0.9
        linear 13.041 xpos 1.1542 rotate -90 ypos 0.4
        repeat 
    show sl faceless at center: 
        zoom 0.75 xpos 1.1457 ypos 0.4 rotate 0 alpha 0.9
        linear 19.8346 xpos -1.18 rotate 90 ypos 0.5
        repeat 
    show us faceless at center: 
        zoom 0.75 xpos 1.18 ypos 0.55 rotate 0 alpha 0.9
        linear 18.0 xpos -1.15 rotate -90 ypos 0.6
        repeat 
    $ renpy.pause (5.5, hard=True) 
    window show 
    "Фигуры в одинаковых пионерских одеждах, незапоминающиеся, скрученные." 
    "С их лиц как будто заживо содрали кожу. Из-за воротников рубашек торчали куски верёвок." 
    th "Спят убитые игрушки вечным сном."
    "..." 
    "А буква Ё была хорошая, да..." 
    "{cps=10}{i}Как будто её больше нет.{w} По крайней мере, тут.{/i}{/cps}" 
    window hide 
    stop music fadeout 5.5
    scene idmt_black with Dissolve(5.5) 
    $ renpy.pause(2.5, hard=True) 
    window show
    "Адский трип прекратился.{w} Я, вылетев из ниоткуда в позе эмбриона, вновь почувствовал под собой землю." 
    "{cps=10}Ожидая увидеть перед собой домик Лены или, на худой конец, свой домик, я-{/cps}{nw}" 
    window hide
    play music idmt_blackearrape
    scene cg epilogue_mi_4 with vpunch
    $ renpy.pause (6.6, hard=True) 
    window show 
    "{cps=10}{size=66}{color=#ff0000}КАКОГО...{/color}{/size}{/cps}{nw}" with vpunch
    window hide 
    $ renpy.pause (1.5, hard=True) 
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound idmt_glitch
    $ renpy.pause (0.3, hard=True)
    stop sound
    hide screen tear 
    call idmt_teardebug
    scene idmt_mysticforest: 
        subpixel True
        zoom 1.0 align (0.5, 0.5) matrixcolor HueMatrix(0.0)
        ease 31.98 zoom 2.22 align (0.5, 0.2) matrixcolor HueMatrix(360.0)
    show un evil_smile pioneer close at center zorder 1: 
        subpixel True
        zoom 1.0 align (0.5, 0.5) matrixcolor HueMatrix(0.0)
        ease 31.98 zoom 2.22 align (0.5, 0.2) matrixcolor HueMatrix(360.0)
    $ renpy.pause (6.66, hard=True) 
    show idmt_white zorder 2
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}Ты же{/color}{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (4.0, hard=True) 
    stop ambience
    hide idmt_white 
    hide text
    $ witchhouse_shake = 1.5 
    show layer master at idmt_mshake 
    $ renpy.pause (6.66, hard=True) 
    show idmt_white zorder 2
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}хотел{/color}{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (4.0, hard=True) 
    stop ambience
    hide idmt_white 
    hide text 
    $ witchhouse_shake = 3.33 
    show layer master at idmt_mshake 
    $ renpy.pause (6.66, hard=True) 
    show idmt_white zorder 2
    play ambience idmt_vinyl 
    show layer master at idmt_fastblur: 
        mesh True shader "witchhouse.oldcinema" 
        u_resolution (1920, 1080)    
        u_mouse (960, 540, 0)
    show text ("{font=IDMT/fonts/LC Chalk.ttf}{size=55}{color=#000000}быть со мной.{/color}{/size}{/font}") zorder 3 at truecenter with dspr: 
        idmt_dizzy(2.5, 2.5) 
    $ renpy.pause (4.0, hard=True) 
    stop ambience
    hide idmt_white 
    hide text 
    $ witchhouse_shake = 6.66 
    show layer master at idmt_mshake 
    $ renpy.pause (6.66, hard=True) 
    stop music 
    scene idmt_black 
    play sound sfx_fall_grass 
    $ renpy.pause (4.5, hard=True) 
    jump idmt_ch3
