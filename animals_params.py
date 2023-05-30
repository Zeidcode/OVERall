animal_name = ['Арчи', 'Боб', 'Черри', 'Крокс', 'Фокс', 'Джек', 'Джерри', 'Китти', 'Майлз', 'Пиклз', 'Спэрроу', 'Спайк',
               'Старлайт', 'Танго', 'Тедди', 'Титан', 'Том', 'Виски', 'Вуди', 'Бастер', 'Бисквит', 'Барни', 'Корбин',
               'Чип', 'Динго', 'Чарли', 'Ларк', 'Логан', 'Лаки', 'Ник', 'Оскар', 'Пэдди', 'Ральф', 'Виспер', 'Майло',
               'Макс', 'Локи', 'Кларк', 'Флауэр', 'Грейс', 'Пикси', 'Пайпер', 'Уиллоу', 'Пампкин', 'Начо', 'Тако',
               'Куки',
               'Зевс', 'Олаф', 'Симба']
animal_species = ["Кот", "Собака", "Хомяк", "Лошадь", "Верблюд", "Осел"]
animal_type = ["Домашнее животное", "Вьючное животное"]
all_animals = []
animal_facts = ['... Хамелеоны могут двигать глазами в разных направлениях одновременно',
                '... Белка – лучший садовник. Миллионы деревьев вырастают потому, что белки забывают, куда спрятали семечки',
                '... Зуб слона может весить до девяти килограмм!',
                '... У млекопитающих кровь красная, у насекомых жёлтая, у омаров синяя.',
                '... В среднем коровы какают 16 раз в день.',
                '... Муравьи никогда не спят. Вместо этого, они «отдыхают» по восемь минут “отдохнуть” два раза в день. Отдых королевы муравьев занимает  90 минут в день.',
                '... Басенджи – единственная собака, которая не может лаять.',
                '... Только половина мозга дельфина спит. Вторая половина в то время  бодрствует, и следит за окружающей обстановкой.',
                '... Блоха может передвигаться только прыжками, мышцы её лапок устроены как катапульты - они накапливают энергию и “выстреливают” блоху в прыжок.',
                '... Глаз гигантского кальмара размером с баскетбольный мяч.',
                '... Бегемоты рожают под водой, чтобы защитить своих детей от падения!',
                '... У лебедя более 25000 перьев на теле.',
                '... 20-метровый угорь может вырабатывать энергию, способную зажечь 12 лампочек.',
                '... Змеи  видят -через веки.',
                '... Крысы могут смеяться, если их пощекотать.',
                '... Крот может выкопать тоннель длиной до 300 метров за одну ночь.',
                '... Из-за своей постоянной улыбки, квокка известен считается самым счастливым животным.',
                '... Морские котики  могут задерживать дыхание на два часа.',
                '... Когда устрицам необходимо размножаться, они  могут менять свой пол.',
                '... Вороны настолько умны, что они любят проказничать! Они даже могут подкрасться к собаке сзади и играя хватать ее клювом за хвост.',
                '... Жирафы не имеют голосовых связок, поэтому они не могут “говорить!”',
                '... Горбатые киты издают самый громкий звук любого млекопитающего, он  может быть слышан за 20 километров!',
                '... Лошади имеют хорошую память, они могут помнить вещи, людей, которых они встречали, а также навыки, которыми владели несколько лет назад.',
                '... Зебры бегут зигзагами, чтобы спастись от хищников.',
                '... Божьи Коровки могут убирать за собой еду.',
                '... У нарвала цвет кожи зависит от его возраста: чем светлее кожа, тем старше нарвал.',
                '... У коал отпечатки пальцев похожи на человеческие.',
                '... Все сурикаты  имеют обязанности в группе, в которой живут.',
                '... Крокодилы не могут высовывать язык!',
                '... Когда обезьяны-пауки встречаются, то они обнимают друг друга.',
                '... Кошки имеют 32 мышцы в каждом из своем ухе.',
                '... Летучие мыши являются единственными млекопитающими которые могут летать?',
                '... Белые медведи-левши.',
                '... У золотой рыбки память 3 секунды',
                '... Даже после того, как медуза умерла, она все еще может ужалить.',
                '... Навозные жуки могут переносить на себе грузы в 50 раз превышающие его массу тела .',
                '... Сердце креветки находится в голове.',
                '... Улитка может спать три года подряд.',
                '... Щеки бурундука могут растягиваться от орешек и еды в три раза больше, чем его голова.',
                '... У тигра не только полосатая шкура, но и тело тоже.',
                '... Морские коньки плавают “держась за руки”, это они связывают вместе свои хвосты.',
                '... Глаз у страуса больше, чем размер его мозга.',
                '... Волки могут съесть 20 кг мяса за один прием пищи.',
                '... Бабочки пробуют пищу ногами.',
                '... Беркут может летать со скоростью свыше 250 км/час.',
                '... Яд лягушки–стрелка может убить 2200 человек.',
                '... Львы не могут рычать, пока им не исполнится 2 года.',
                '... Скунсы может распылить защитную вонь в радиусе 10 метров.',
                '... Акулы жили раньше, чем динозавры! Окаменелости акул датируются возрастом в 450 миллионов лет.',
                '... В отличие от большинства видов кошек, оцелоты отлично плавают.',
                '... Луговые собаки живут в норах, которые имеют отдельную ванную комнату, детскую зону и зону для отдыха.',
                '... Рыба-парусник является самой быстрой рыбой и достигает скорости 115 км/час.',
                '... Самец–пингвин “предлагает” руку и сердце самке, даря ей камень. Если она принимает его, то кладет этот подарок в свое гнездо.',
                '... Павлин считается самой красивой птицей среди курообразных. Павлин — очень близкий родственник петуха.',
                '... Новорождённый слонёнок весит около 100 килограммов.',
                '... Сурки свистят, когда им угрожает опасность.',
                '... Императорские пингвины могут нырять на глубину до 500 метров и способны задерживать дыхание на 18 минут.',
                '... В Индии 50 миллионов обезьян.',
                '... Мухи жужжат нотой ФА.',
                '... Синий Кит весит как три слона.',
                '... Гиббоны имеют самые длинные руки среди всех приматов.',
                '... У коз частая отрыжка.',
                '... У зубатки вкусовые рецепторы по всему телу.',
                '... Брызгун может поражать добычу плевком с расстояния 1,5 метров.',
                '... У вомбат какашки квадратной формы.',
                '... Ламы не имеют копыт.',
                '... Детеныши дикобраза рождаются с мягкими иголками, которые затвердевают через несколько дней.',
                '... Верблюд может обходиться без воды две недели.',
                '... Лось имеет очень чувствительные рога.',
                '... Гекконы иногда едят свои хвосты после потери.',
                '... В течение жизни хлопотливая пчёлка производит одну двенадцатую чайной ложечки мёда.',
                '... Скорость размножения крыс так велика, что при благоприятных обстоятельствах 2 крысы могли бы дать потомство в 1 миллион крыс в течение полутора лет.',
                '... Некоторые мотыльки могут вырастать размером с ладонь взрослого человека.',
                '... Детеныши шакала рождаются под землей.',
                '... Кузнечик может прыгать на расстояние в 20 раз превышающее  длину его тела.',
                '... У фламинго их красивый цвет получается от водорослей, диатомеи и мелких ракообразных, которых они едят и которые богаты каротином.',
                '... Пол черепахи можно распознать по звуку: самцы ворчат, самки шипят.',
                '... Бойцовая рыбка может выжить без воды в течение нескольких часов.',
                '... Стрекозы могут летать в любом направлении – вперёд, назад и в стороны. Это самые быстрые летающие насекомые, их скорость достигает почти 100 километров в час.',
                '... Голубые киты – самые крупные животные на Земле.',
                '... Сфотографировать живого гигантского кальмара люди сумели только в 2006 году. Живут эти полутонные чудовища на глубине от 200 метров до километра.',
                '... Жужжание пчелы производится четырьмя крыльями, которые делают по 11 400 взмахов в минуту.',
                '... Скорость полёта пчелы – 25 километров в час.',
                '... Азиатский гигантский шершень кусается больнее всех насекомых. У нас он встречается в Приморском крае.',
                '... Паук Тарантул может жить без пищи два года.',
                '... Раненый или напуганный опоссум падает мёртвым, у него стекленеют глаза, изо рта течёт пена, а из анальных желёз источается зловоние. После того, как опасность минует, опоссум оживает и выздоравливает.',
                '... В Ирландии, Исландии, Гренландии и Антарктиде нет змей.',
                '... Гуси любят чернику!',
                '... Серебряные муравьи пустыни  Сахары могут жить при температуре до 158 градусов.',
                '... В козьем молоке в 5 раз меньше жира, чем в коровьем. Коровье молоко усваивается час, козье – 20 минут',
                '... Скорпионы светятся в темноте.',
                '... Чайки могут пить соленую воду. У них есть специальные железы, которые удаляют лишнюю  соль из организма.',
                '... Красные панды используют свой пушистый хвост в качестве одеяла, чтобы согреться.',
                '... Единственная собака, у которой язык не розовый – чау-чау',
                '... Японские макаки научились покупать товары из торговых автоматов.',
                '... В отличие от сухопутных черепах, морские  не втягивают головы в панцирь.',
                '... Эму не могут ходить назад.',
                '... Губки создают свои собственные специальные химические вещества, выделяемые в воде для защиты от хищников.',
                '... Мыши имеют больше костей, чем у человека:  около 230. У человека их 206',
                '... В среднем курица откладывает 190 яиц в год',
                '... Если начнут драться лев и белый медведь, то победит белый медведь']
