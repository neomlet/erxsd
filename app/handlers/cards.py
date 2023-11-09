from aiogram import Router, types

router = Router()

@router.message(commands = ["cards"])
async def number_cards(message: types.Message):
    await message.answer("карточка №5 - /5\nкарточка №6 - /6\nкарточка №7 - /7\nкарточка №8 - /8\nкарточка №9 -/9\nкарточка №10 - /10\nкарточка №11 - /11\nкарточка №12 - /12\nкарточка №13 - /13\nкарточка №14 - /14\nкарточка №15 - /15")

card_table5 = {"альвеолярный": "alveolaris",
                  "блуждающий": "vagus",
                  "внутренний": "internus",
                  "грудная клетка": "thorax",
                  "желудок": "gaster",
                  "зубной": "dentalis",
                  "кисть": "manus",
                  "кость плечевая": "humerus",
                  "матка": "uterus",
                  "наружный": "externus",
                  "опухоль": "tumor",
                  "передний": "anterior",
                  "почечный": "renalis",
                  "сбор": "species",
                  "селезёнка": "splen",
                  "тело": "corpus",
                  "хрусталик": "lens",
                  "эмболия": "embolia",
                  "гранула": "granulum",
                  "гребень": "crista",
                  "диабетический": "diabeticus"}

current_card_index = 0

@router.message(lambda message: message.text.lower() in card_table5.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table5.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table5):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table5.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["5"])
async def cmd_five(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table5):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table5.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table6 = {"ампутация": "amputatio",
               "боль": "dolor",
               "внутричерепной": "intracranialis",
               "грудь": "thorax",
               "желудочек": "ventriculus",
               "извилина": "gyrus",
               "кашель": "tussis",
               "крестец": "os sacrum",
               "меланома": "melanoma",
               "невралгия": "neuralgia",
               "острый": "acutus",
               "перепончатый": "membranaceus",
               "почка": "ren",
               "сердце": "cor",
               "трава": "herba",
               "хрящ": "cartilago",
               "эпилепсия": "epilepsia",
               "дибазол": "dibazolum",
               "димедрол": "dimedrolum",
               "дистрофия": "dystrophia"}

@router.message(lambda message: message.text.lower() in card_table6.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table6.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table6):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table6.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["6"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table6):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table6.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")

card_table7 = {"анамнез": "anamnesis",
               "боль зубная": "odontalgia",
               "вода": "aqua",
               "грудной": "pectoralis",
               "желчегонный": "cholagogus",
               "инсульт": "insultus",
               "кишечник": "intestlnum",
               "кровавый": "sanguineus",
               "кровоизлияние": "haemorrhagia",
               "местный": "localis",
               "нёбный": "palatinus",
               "отвар": "decoctum",
               "пероральный": "peroralis",
               "поясница": "lumbi",
               "склероз": "sclerosis",
               "трёхглавый": "triceps",
               "хрящевой": "cartilagineus",
               "эмульсия": "emulsum",
               "добавочный": "accessorius",
               "доза": "dosis",
               "доля": "lobus"}

@router.message(lambda message: message.text.lower() in card_table7.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table7.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table7):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table7.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["7"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table7):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table7.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table8 = {"анастезия": "anaesthesia",
               "боль в желудке": "gastralgia",
               "водянка": "hydrops",
               "грыжа": "hernia",
               "желчь": "chole",
               "инфаркт": "infarctus",
               "кишечный": "intestinalis",
               "кровь": "haema",
               "миокард": "miocardium",
               "некроз": "necrosis",
               "отводящий": "abducens",
               "печень": "hepar",
               "правый": "dexter",
               "слабоумие": "dementia",
               "тромб": "thrombus",
               "цветок": "flos",
               "этиловый": "aethyllcus",
               "железо": "ferrum",
               "жёлтый": "flavus",
               "желчный": "biliaris"}

@router.message(lambda message: message.text.lower() in card_table8.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table8.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table8):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table8.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["8"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table8):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table8.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table9 = {"артериальный": "arteriosus",
               "боль в области сердца": "cardialgia",
               "воспалительный": "inflammatorius",
               "губа": "labium",
               "живот": "abdomen",
               "инфекция": "infectio",
               "кишка": "intestinum",
               "левый": "sinister",
               "мозг": "medulla",
               "нерв": "nervus",
               "отек": "oedema",
               "пищевод": "oesophagus",
               "прямой": "rectus",
               "слёзный": "lacrimalis",
               "трофический": "trophicus",
               "центральный": "centralis",
               "юношеский": "juvenilis",
               "закрытый": "clausus",
               "занавеска": "velum",
               "запястье": "carpus"}

@router.message(lambda message: message.text.lower() in card_table9.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table9.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table9):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table9.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["9"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table9):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table9.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table10 = {"артрит": "arthitis",
                "боль головы": "alia",
                "врождённый": "congenitus",
                "давление": "tensio",
                "жидкий": "fluidus",
                "инъекция": "injectio",
                "клапан": "valva",
                "лёгкое": "pulmo",
                "мозговая оболочка": "mater",
                "нефрит": "nephritis",
                "отросток": "processus",
                "плевра": "pleura",
                "пузырь": "vesica",
                "слепой": "caecus",
                "туберкулёз": "tuberculosis",
                "частичный": "partialis",
                "ягодичный": "gluteus",
                "камфора": "camphora",
                "капсула": "capsula",
                "карбонат": "carbonas"}

@router.message(lambda message: message.text.lower() in card_table10.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table10.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table10):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table10.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["10"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table10):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table10.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table11 = {"асептический": "asepticus",
                "бородавка": "verruca",
                "вторичный": "secundarius",
                "деформирующий": "deformans",
                "диабет": "diabetes",
                "жидкость": "liquor",
                "истерический": "hystericus",
                "кожа": "cutis",
                "лёгочный": "pulmonalis",
                "мозолистый": "callosus",
                "нижний": "inferior",
                "очаговый": "focalis",
                "плеврит": "pleuritis",
                "плечо": "brachium",
                "пустырник": "leonurus",
                "слизистый": "mucosus",
                "тяжёлый": "gravis",
                "часть": "pars",
                "корень": "radix",
                "корневище": "rhizoma",
                "короткий": "brevis"}

@router.message(lambda message: message.text.lower() in card_table11.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table11.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table11):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table11.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["11"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table11):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table11.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table12 = {"атрофия": "atrophia",
                "боярышник": "crataegus",
                "гастрит": "gastritis",
                "диафрагма": "diaphragma",
                "жизнь": "vita",
                "каменистый": "petrosus",
                "колено": "genu",
                "лекарственный": "medicamentosa",
                "мозоль": "clavus",
                "нитрат": "nitras",
                "открытый": "apertus",
                "плод": "fructus",
                "размягчение костей": "osteomalicia",
                "сложный": "compositus",
                "узел": "ganglion",
                "верхняя челюсть": "maxilla",
                "ядро": "nucleus",
                "латеральный": "lateralis",
                "лейкодерма": "leucoderma",
                "линия": "linea"}

@router.message(lambda message: message.text.lower() in card_table12.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table12.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table12):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table12.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["12"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table12):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table12.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table13 = {"аорта": "aorta",
                "вегетативно-сосудистый": "vegeto-vascularis",
                "глаз": "oculus",
                "дистония": "dystonia",
                "жировой": "adiposus",
                "канал": "canalis",
                "конечность": "membrum",
                "лимфатический": "lymphaticus",
                "мост": "pons",
                "нитрит": "nitris",
                "пазуха": "sinus",
                "плечо": "brachium",
                "разрез": "sectio",
                "слуховой": "acusticus",
                "устье": "ostium",
                "нижняя челюсть": "mandibula",
                "язва": "ulcus",
                "магний": "magnesium",
                "мазь": "unguentum",
                "малоберцовый": "fibularis"}

@router.message(lambda message: message.text.lower() in card_table13.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table13.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table13):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table13.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["13"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table13):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table13.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table14 = {"барабанный": "tympanicus",
                "веко": "palpebra",
                "глазной": "opthalmicus",
                "ребёнок": "infans",
                "задний": "posterior",
                "капиллярный": "capillaris",
                "кора": "cortex",
                "лицевой": "facialis",
                "мочевой": "urinarius",
                "ноготь": "unguis",
                "палец": "digitus",
                "подкожный": "subcutaneus",
                "разрыв": "raptura",
                "слюнный": "salivatorius",
                "ухо": "auris",
                "череп": "cranium",
                "язвенный": "ulcerosus",
                "междолевой": "interlobaris",
                "мембрана": "membrana",
                "ментол": "mentholum"}

@router.message(lambda message: message.text.lower() in card_table14.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table14.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table14):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table14.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["14"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table14):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table14.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")


card_table15 = {"бедренная кость": "femur",
                "вена": "vena",
                "глотка": "pharynx",
                "длинный": "longus",
                "задний проход": "anus",
                "капля": "gutta",
                "костно-мозговой": "medullaris",
                "лицо": "facies",
                "мышечный": "muscularis",
                "ножка": "peduncula",
                "палец стопы большой": "hallux",
                "позвонок": "vertebra",
                "раствор": "solutio",
                "сосуд": "vas",
                "ушной": "auricularis",
                "шейка": "cervix",
                "язык": "lingua",
                "микстура": "mixtura",
                "мнимый": "spurius",
                "множественный": "multiplex"}

@router.message(lambda message: message.text.lower() in card_table15.values())
async def check_translation(message: types.Message):
    global current_card_index
    translated_word = message.text.lower()
    for russian_word, english_word in card_table15.items():
        if english_word == translated_word:
            await message.answer(f"Верно! '{russian_word}' переводится как '{english_word}'.")
            current_card_index += 1
            if current_card_index >= len(card_table15):
                await message.answer("Вы уже перевели все слова.")
                return
            else:
                next_card = list(card_table15.keys())[current_card_index]
                await message.answer(f"Переведите слово '{next_card}' с русского на латинский.")
            break

@router.message(commands=["15"])
async def cmd_six(message: types.Message):
    global current_card_index
    if current_card_index >= len(card_table15):
        await message.answer("Вы уже перевели все слова.")
        return

    current_card = list(card_table15.keys())[current_card_index]
    await message.answer(f"Переведите слово '{current_card}' с русского на латинский.")