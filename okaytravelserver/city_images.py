def get_city_id(city):
    for id in AVAILABLE_CITY_IMAGES:
        if city in AVAILABLE_CITY_IMAGES[id].values():
            return id
    return None


AVAILABLE_CITY_IMAGES = {
    "1": {
        "ru_RU": "Гонконг",
        "en_EN": "Hong Kong"
    },
    "2": {
        "ru_RU": "Таиланд, Бангкок",
        "en_EN": "Thailand, City of Bangkok"
    },
    "3": {
        "ru_RU": "Великобритания, Лондон",
        "en_EN": "United Kingdom, London"
    },
    "4": {
        "ru_RU": "Сингапур",
        "en_EN": "Singapore"
    },
    "5": {
        "ru_RU": "Макао",
        "en_EN": "Macau"
    },
    "6": {
        "ru_RU": "Объединенные Арабские Эмираты, Дубай",
        "en_EN": "United Arab Emirates, city of Dubai"
    },
    "7": {
        "ru_RU": "Франция, Иль-де-Франс, Париж",
        "en_EN": "France, Île-de-France, Paris"
    },
    "8": {
        "ru_RU": "Соединённые Штаты Америки, штат Нью-Йорк",
        "en_EN": "United States of America, New York"
    },
    "9": {
        "ru_RU": "Китай, провинция Гуандун, город Шэньчжэнь",
        "en_EN": "China, Guangdong Province, City of Shenzhen"
    },
    "10": {
        "ru_RU": "Малайзия, Куала-Лумпур",
        "en_EN": "Malaysia, City of Kuala Lumpur"
    },
    "11": {
        "ru_RU": "Таиланд, Пхукет, остров Пхукет",
        "en_EN": "Thailand, Phuket"
    },
    "12": {
        "ru_RU": "Италия, Рим",
        "en_EN": "Italy, Rome"
    },
    "13": {
        "ru_RU": "Япония, Токио",
        "en_EN": "Japan, Tokyo, Ostrovnyye territorii Tokio"
    },
    "14": {
        "ru_RU": "Тайвань, Тайбэй",
        "en_EN": "Тайвань, Тайбэй"
    },
    "15": {
        "ru_RU": "Турция, Стамбул",
        "en_EN": "Türkiye, İstanbul"
    },
    "16": {
        "ru_RU": "Республика Корея, Сеул",
        "en_EN": "Republic of Korea, Seoul"
    },
    "17": {
        "ru_RU": "Китай, провинция Гуандун, город субпровинциального значения Гуанчжоу, Гуанчжоу",
        "en_EN": "China, Guangdong Province, Sub-provincial city Guangzhou, Guangzhou"
    },
    "18": {
        "ru_RU": "Чехия, Прага",
        "en_EN": "Czechia, Praha"
    },
    "19": {
        "ru_RU": "Саудовская Аравия, Мекка",
        "en_EN": "Saudi Arabia, Makkah"
    },
    "20": {
        "ru_RU": "Соединённые Штаты Америки, штат Флорида, Дейд-Каунти, город Майами",
        "en_EN": "United States of America, Florida, Dade County, City of Miami"
    },
    "21": {
        "ru_RU": "Индия, Дели",
        "en_EN": "India, Deli"
    },
    "22": {
        "ru_RU": "Индия, штат Махараштра, Мумбаи",
        "en_EN": "India, State of Maharashtra, Mumbai"
    },
    "23": {
        "ru_RU": "Испания, Каталония, город Барселона",
        "en_EN": "Spain, Comunidad Autònoma de Catalunya, City of Barcelona"
    },
    "24": {
        "ru_RU": "Таиланд, город Паттайя",
        "en_EN": "Thailand, Pattaya"
    },
    "25": {
        "ru_RU": "Китай, Шанхай",
        "en_EN": "China, Shanghai"
    },
    "26": {
        "ru_RU": "Соединённые Штаты Америки, штат Невада, Кларк-Каунти, город Лас-Вегас",
        "en_EN": "United States of America, Nevada, Clark County, City of Las Vegas"
    },
    "27": {
        "ru_RU": "Италия, Ломбардия, Милан",
        "en_EN": "Italy, Lombardia, Milan"
    },
    "28": {
        "ru_RU": "Нидерланды, Амстердам",
        "en_EN": "Netherlands, Amsterdam"
    },
    "29": {
        "ru_RU": "Турция, Анталья",
        "en_EN": "Turkey, Antalya"
    },
    "30": {
        "ru_RU": "Австрия, Вена",
        "en_EN": "Austria, Wien"
    },
    "31": {
        "ru_RU": "Соединённые Штаты Америки, Калифорния, Лос-Анджелес",
        "en_EN": "United States of America, California, Los Angeles"
    },
    "32": {
        "ru_RU": "Мексика, Кинтана-Роо, город Канкун",
        "en_EN": "Mexico, Quintana Roo, Cancun"
    },
    "33": {
        "ru_RU": "Япония, префектура Осака, Осака",
        "en_EN": "Japan, Osaka Prefecture, Osaka City"
    },
    "34": {
        "ru_RU": "Германия, Берлин",
        "en_EN": "Germany, Berlin"
    },
    "35": {
        "ru_RU": "Индия, штат Уттар-Прадеш, Агра",
        "en_EN": "India, State of Uttar Pradesh, Agra"
    },
    "36": {
        "ru_RU": "Вьетнам, город центрального подчинения Хошимин, город Хошимин",
        "en_EN": "Vietnam, Hồ Chí Minh Municipality, Ho Chi Minh City"
    },
    "37": {
        "ru_RU": "Южно-Африканская Республика, провинция Гаутенг, Йоханнесбург",
        "en_EN": "Republic of South Africa, Gauteng Province, Johannesburg"
    },
    "38": {
        "ru_RU": "Италия, Венеция",
        "en_EN": "Italy, Veneto, Venice"
    },
    "39": {
        "ru_RU": "Испания, Мадрид",
        "en_EN": "Spain, Madrid"
    },
    "40": {
        "ru_RU": "Соединённые Штаты Америки, штат Флорида, округ Ориндж, Орландо",
        "en_EN": "United States of America, Florida, Orange County, Orlando"
    },
    "41": {
        "ru_RU": "Саудовская Аравия, Эр-Рияд",
        "en_EN": "Saudi Arabia, Ar Riyad"
    },
    "42": {
        "ru_RU": "Малайзия, Джохор",
        "en_EN": "Malaysia, Johor"
    },
    "43": {
        "ru_RU": "Ирландия, Дублин",
        "en_EN": "Ireland, Dublin"
    },
    "44": {
        "ru_RU": "Италия, Тоскана, Флоренция",
        "en_EN": "Italy, Toscana, Firenze, Florence"
    },
    "45": {
        "ru_RU": "Индия, штат Тамилнад, Ченнаи",
        "en_EN": "India, State of Tamil Nadu, Chennai"
    },
    "46": {
        "ru_RU": "Россия, Москва",
        "en_EN": "Russia, Moscow"
    },
    "47": {
        "ru_RU": "Греция, Афины",
        "en_EN": "Greece, Athens"
    },
    "48": {
        "ru_RU": "Индия, штат Раджастхан, Джайпур",
        "en_EN": "India, State of Rajasthan, Jaipur"
    },
    "49": {
        "ru_RU": "Китай, Пекин",
        "en_EN": "China, Beijing"
    },
    "50": {
        "ru_RU": "Индонезия, провинция Бали, Денпасар",
        "en_EN": "Indonesia, Bali, Denpasar"
    },
    "51": {
        "ru_RU": "Канада, провинция Онтарио, город Торонто",
        "en_EN": "Canada, Ontario, City of Toronto"
    },
    "52": {
        "ru_RU": "Вьетнам, Ханой",
        "en_EN": "Vietnam, Hanoi"
    },
    "53": {
        "ru_RU": "Австралия, Новый Южный Уэльс, город Сидней",
        "en_EN": "Australia, New South Wales, Сity of Sydney"
    },
    "54": {
        "ru_RU": "Соединённые Штаты Америки, Калифорния, округ Сан-Франциско, город Сан-Франциско",
        "en_EN": "United States of America, California, San Francisco County, City and County of San Francisco"
    },
    "55": {
        "ru_RU": "Венгрия, Будапешт",
        "en_EN": "Hungary, Budapest"
    },
    "56": {
        "ru_RU": "Вьетнам, бухта Халонг",
        "en_EN": None
    },
    "57": {
        "ru_RU": "Доминиканская Республика, Ла Альтаграсия, аэропорт Пунта Кана",
        "en_EN": "Dominican Republic, La Altagracia, Punta Cana"
    },
    "58": {
        "ru_RU": "Саудовская Аравия, Эш-Шаркия, город Эд-Даммам",
        "en_EN": "Saudi Arabia, Eastern Province, City of Dammam"
    },
    "59": {
        "ru_RU": "Германия, Бавария, Мюнхен",
        "en_EN": "Германия, Бавария, Мюнхен"
    },
    "60": {
        "ru_RU": "Китай, провинция Гуандун, городской округ Чжухай, город Чжухай",
        "en_EN": "China, Guangdong Province, Zhuhai District, Zhuhai City"
    },
    "61": {
        "ru_RU": "Португалия, Лиссабон",
        "en_EN": "Portugal, Lisbon District"
    },
    "62": {
        "ru_RU": "Египет, Каир",
        "en_EN": "Egypt, Cairo"
    },
    "63": {
        "ru_RU": None,
        "en_EN": "Malaysia, Penang"
    },
    "64": {
        "ru_RU": "Катар, Доха",
        "en_EN": "Qatar, Doha"
    },
    "65": {
        "ru_RU": "Дания, Столичная область, Копенгаген",
        "en_EN": "Denmark, Copenhagen"
    },
    "66": {
        "ru_RU": "Греция, периферия Крит, Ираклион",
        "en_EN": "Greece, periferiya Krit, City of Heraklion"
    },
    "67": {
        "ru_RU": "Израиль, Иерусалим",
        "en_EN": "Israel, Jerusalem"
    },
    "68": {
        "ru_RU": "Турция, Эдирне",
        "en_EN": "Turkey, Edirne"
    },
    "69": {
        "ru_RU": "Камбоджа, Пномпень",
        "en_EN": "Cambodia, Phnom Penh"
    },
    "70": {
        "ru_RU": "Россия, Санкт-Петербург",
        "en_EN": "Russia, Saint Petersburg"
    },
    "71": {
        "ru_RU": "Республика Корея, провинция с особой автономией Чеджудо, Чеджу",
        "en_EN": "Republic of Korea, Jeju Special Self-Governing Province, Jeju"
    },
    "72": {
        "ru_RU": "Япония, префектура Киото, Киото",
        "en_EN": "Japan, Kyoto Prefecture, Kyoto CIty"
    },
    "73": {
        "ru_RU": "Таиланд, Chiang Mai, город Чиангмай",
        "en_EN": "Thailand, Chiang Mai"
    },
    "74": {
        "ru_RU": "Польша, Варшава",
        "en_EN": "Poland, Warsaw"
    },
    "75": {
        "ru_RU": "Польша, Малопольское воеводство, Повят-Кракув, Кракув, Краков",
        "en_EN": "Poland, Lesser Poland Voivodeship, Powiat Kraków, Kraków, Krakow"
    },
    "76": {
        "ru_RU": "Соединённые Штаты Америки, штат Огайо, Хайленд-Каунти, Гонолулу",
        "en_EN": "United States of America, Hawaii, Honolulu County"
    },
    "77": {
        "ru_RU": "Австралия, Виктория, город Мельбурн",
        "en_EN": "Australia, Victoria, City of Melbourne"
    },
    "78": {
        "ru_RU": "Израиль, Тель-Авив",
        "en_EN": "Israel, Tel Aviv"
    },
    "79": {
        "ru_RU": "Марокко, город Марракеш",
        "en_EN": "Morocco, gorod Marrakesh"
    },
    "80": {
        "ru_RU": "Бельгия, Брюссель",
        "en_EN": "Belgium, Brussels"
    },
    "81": {
        "ru_RU": "Новая Зеландия, Окленд",
        "en_EN": "New Zealand, Auckland Region, Auckland"
    },
    "82": {
        "ru_RU": "Канада, провинция Британская Колумбия, Метро-Ванкувер-Риджинал-Дистрикт, город Ванкувер",
        "en_EN": "Canada, British Columbia, Metro Vancouver Regional District, Vancouver"
    },
    "83": {
        "ru_RU": "Индонезия, Джакарта",
        "en_EN": "Indonesia, Special Capital Region of Jakarta"
    },
    "84": {
        "ru_RU": "Германия, Гессен, город Франкфурт-на-Майне",
        "en_EN": "Germany, Hessen, Frankfurt am Main"
    },
    "85": {
        "ru_RU": "Турция, Артвин",
        "en_EN": "Turkey, Artvin"
    },
    "86": {
        "ru_RU": "Китай, Гуанси-Чжуанский автономный район, городской округ Гуйлинь, город Гуйлинь",
        "en_EN": "China, Guangxi Zhuang Autonomous Region, Guilin District"
    },
    "87": {
        "ru_RU": "Швеция, Стокгольм",
        "en_EN": "Sweden, Stockholm"
    },
    "88": {
        "ru_RU": "Бразилия, Рио-де-Жанейро",
        "en_EN": "Brasil, Rio de Janeiro"
    },
    "89": {
        "ru_RU": "Индия, штат Западная Бенгалия, Калькутта",
        "en_EN": "India, State of West Bengal, Kolkata"
    },
    "90": {
        "ru_RU": "Аргентина, Буэнос-Айрес",
        "en_EN": "Argentina, Ciudad Autónoma de Buenos Aires"
    },
    "91": {
        "ru_RU": "Япония, префектура Тиба, город Тиба",
        "en_EN": "Japan, Chiba Prefecture, gorod Tiba"
    },
    "92": {
        "ru_RU": "Камбоджа, город Сиемреап",
        "en_EN": None
    },
    "93": {
        "ru_RU": "Франция, Прованс-Альпы-Лазурный Берег, Приморские Альпы, город Ницца",
        "en_EN": "France, Provence-Alpes-Côte d'Azur, Alpes-Maritimes, Nice"
    },
    "94": {
        "ru_RU": "Мексика, Мехико",
        "en_EN": "Mexico"
    },
    "95": {
        "ru_RU": "Перу, Лима",
        "en_EN": "Perú, Lima"
    },
    "96": {
        "ru_RU": "Тайвань, Тайчжун",
        "en_EN": "Taiwan, Taichung, City of Taichung"
    },
    "97": {
        "ru_RU": None,
        "en_EN": None
    },
    "98": {
        "ru_RU": "Соединённые Штаты Америки, округ Колумбия, Вашингтон",
        "en_EN": "United States of America, District of Columbia, City of Washington"
    },
    "99": {
        "ru_RU": "Объединенные Арабские Эмираты, Абу-Даби",
        "en_EN": "United Arab Emirates, City of Abu Dhabi"
    },
    "100": {
        "ru_RU": "Шри-Ланка, Западная провинция, Коломбо",
        "en_EN": "Sri Lanka, Western, Colombo"
    },
    "101": {
        "ru_RU": "Россия, Челябинская область, Магнитогорск",
        "en_EN": "Russia, Chelyabinsk Region, Magnitogorsk"
    },
    "102": {
        "ru_RU": "Россия, Свердловская область, Екатеринбург",
        "en_EN": "Russia, Sverdlovsk Region, Yekaterinburg"
    },
    "103": {
        "ru_RU": "Россия, Новосибирск",
        "en_EN": "Russia, Novosibirsk"
    },
    "104": {
        "ru_RU": "Россия, Нижний Новгород",
        "en_EN": "Russia, Nizhniy Novgorod"
    },
    "105": {
        "ru_RU": "Россия, Челябинск",
        "en_EN": "Russia, Chelyabinsk"
    },
    "106": {
        "ru_RU": "Россия, Республика Башкортостан, Уфа",
        "en_EN": "Russia, Republic of Bashkortostan, Ufa"
    },
    "107": {
        "ru_RU": "Россия, Приморский край, Владивосток",
        "en_EN": "Russia, Primorye Territory, Vladivostok"
    },
    "108": {
        "ru_RU": "Россия, Краснодарский край, Сочи",
        "en_EN": "Russia, Krasnodar Territory, Sochi"
    },
    "109": {
        "ru_RU": "Россия, Ростов-на-Дону",
        "en_EN": "Russia, Rostov-on-Don"
    },
    "110": {
        "ru_RU": "Россия, Краснодар",
        "en_EN": "Russia, Krasnodar"
    },
    "111": {
        "ru_RU": "Россия, Калининград",
        "en_EN": "Russia, Kaliningrad"
    },
    "112": {
        "ru_RU": "Россия, Ярославль",
        "en_EN": "Russia, Yaroslavl"
    },
    "113": {
        "ru_RU": "Россия, Самара",
        "en_EN": "Russia, Samara"
    },
    "114": {
        "ru_RU": "Россия, Саратов",
        "en_EN": "Russia, Saratov"
    },
    "115": {
        "ru_RU": "Россия, Тверь",
        "en_EN": "Russia, Tver"
    },
    "116": {
        "ru_RU": "Россия, Тюмень",
        "en_EN": "Russia, Tyumen"
    },
    "117": {
        "ru_RU": "Россия, Омск",
        "en_EN": "Russia, Omsk"
    },
    "118": {
        "ru_RU": "Россия, Самарская область, Тольятти",
        "en_EN": "Russia, Samara Region, Tolyatti"
    },
    "119": {
        "ru_RU": "Россия, Республика Марий Эл, Йошкар-Ола",
        "en_EN": "Russia, Republic of Mari El, Yoshkar-Ola"
    },
    "120": {
        "ru_RU": "Россия, Красноярск",
        "en_EN": "Russia, Krasnoyarsk"
    },
    "121": {
        "ru_RU": "Албания, Тирана",
        "en_EN": "Shqipërisë, Tirana"
    },
    "122": {
        "ru_RU": "Андорра, община Андорра-ла-Велья",
        "en_EN": "Andorra, Parròquia Andorra la Vella"
    },
    "123": {
        "ru_RU": "Беларусь, Минск",
        "en_EN": "Belarus, Minsk"
    },
    "124": {
        "ru_RU": "Болгария, София",
        "en_EN": "Bulgaria, Sofia"
    },
    "125": {
        "ru_RU": "Босния и Герцеговина, Сараево",
        "en_EN": "Bosnia and Herzegovina, Sarajevo"
    },
    "126": {
        "ru_RU": "Ватикан",
        "en_EN": "Vatican"
    },
    "127": {
        "ru_RU": "Исландия, Рейкьявик",
        "en_EN": "Iceland, Reykjavíkurborg"
    },
    "128": {
        "ru_RU": "Латвия, Рига",
        "en_EN": "Latvia, Riga"
    },
    "129": {
        "ru_RU": "Литва, Вильнюс",
        "en_EN": "Lithuania, Vilnius"
    },
    "130": {
        "ru_RU": "Лихтенштейн, Вадуц",
        "en_EN": "Liechtenstein, Vaduz"
    },
    "131": {
        "ru_RU": "Бельгия, Люксембург",
        "en_EN": "Belgium, Luxembourg"
    },
    "132": {
        "ru_RU": "Северная Македония, Скопье",
        "en_EN": "North Macedonia, Skopje"
    },
    "133": {
        "ru_RU": "Мальта, Валлетта",
        "en_EN": "Malta, Valletta"
    },
    "134": {
        "ru_RU": "Молдова, Кишинёв",
        "en_EN": "Moldova, Chisinau"
    },
    "135": {
        "ru_RU": "Монако",
        "en_EN": "Monaco"
    },
    "136": {
        "ru_RU": "Норвегия, Осло",
        "en_EN": "Norway, Oslo"
    },
    "137": {
        "ru_RU": "Румыния, Бухарест",
        "en_EN": "Romania, Bucharest"
    },
    "138": {
        "ru_RU": "Сан-Марино",
        "en_EN": "San Marino, city of San Marino"
    },
    "139": {
        "ru_RU": "Сербия, Белград",
        "en_EN": "Serbia, Belgrade"
    },
    "140": {
        "ru_RU": "Словакия, Братислава",
        "en_EN": "Slovakia, Bratislava"
    },
    "141": {
        "ru_RU": "Словения, Любляна",
        "en_EN": "Slovenia, Ljubljana"
    },
    "142": {
        "ru_RU": "Украина, Киев",
        "en_EN": "Ukraine, Kyiv"
    },
    "143": {
        "ru_RU": "Финляндия, Хельсинки",
        "en_EN": "Finland, Helsinki"
    },
    "144": {
        "ru_RU": "Черногория, Подгорица",
        "en_EN": "Montenegro, Podgorica"
    },
    "145": {
        "ru_RU": "Хорватия, Загреб",
        "en_EN": "Croatia, Zagreb"
    },
    "146": {
        "ru_RU": "Швейцария, Берн",
        "en_EN": "Schweiz, Bern"
    },
    "147": {
        "ru_RU": "Эстония, Таллин",
        "en_EN": "Estonia, Tallinn"
    },
    "148": {
        "ru_RU": "Россия, Республика Татарстан, Казань",
        "en_EN": "Russia, Republic of Tatarstan, City of Kazan"
    }
}