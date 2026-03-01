import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "8145998470:AAHCZXZVzvpBuE-fN7tsg5tMI4TNjSrq3-4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# ---------------- СОСТОЯНИЯ ----------------

class UserState(StatesGroup):
    choosing_role = State()
    waiting_code = State()
    guest = State()
    stepa = State()


# ---------------- КНОПКИ ----------------

def start_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Я гость")],
            [KeyboardButton(text="Я Степа")]
        ],
        resize_keyboard=True
    )


def guest_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1 слово")],
            [KeyboardButton(text="Профессия")],
            [KeyboardButton(text="Характер")],
            [KeyboardButton(text="Ассоциации")],
            [KeyboardButton(text="Животное")],
            [KeyboardButton(text="Перезапуск")]
        ],
        resize_keyboard=True
    )


def stepa_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Взгляд со стороны")],
            [KeyboardButton(text="1 слово")],
            [KeyboardButton(text="Профессия")],
            [KeyboardButton(text="Характер")],
            [KeyboardButton(text="Ассоциации")],
            [KeyboardButton(text="Животное")],
            [KeyboardButton(text="Описание и мнения")],
            [KeyboardButton(text="Кто лучше знает?")],
            [KeyboardButton(text="Пожелания")],
            [KeyboardButton(text="Перезапуск")]
        ],
        resize_keyboard=True
    )


# ---------------- START ----------------

@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(UserState.choosing_role)
    await message.answer(
        "Привет! Кто ты? Именинник или Гость?",
        reply_markup=start_keyboard()
    )


# ---------------- ВЫБОР РОЛИ ----------------

@dp.message(F.text == "Я гость")
async def guest_selected(message: Message, state: FSMContext):
    await state.set_state(UserState.guest)
    await message.answer(
        "Супер! Нажимай на кнопки в меню, чтобы посмотреть содержимое бота. Приятного просмотра! (Уточнение : бот обращается к Степе и все его сообщения направлены на Степу.) ",
        reply_markup=guest_menu()
    )


@dp.message(F.text == "Я Степа")
async def stepa_selected(message: Message, state: FSMContext):
    await state.set_state(UserState.waiting_code)
    await message.answer("Отправь секретный код")


# ---------------- ПРОВЕРКА КОДА ----------------

@dp.message(UserState.waiting_code)
async def check_secret_code(message: Message, state: FSMContext):
    if message.text.lower() == "ангел":
        await state.set_state(UserState.stepa)
        await message.answer(
            "Код верный! Ура! С днем рождения! Я очень старалась, приятного просмотра <3",
            reply_markup=stepa_menu()
        )
    else:
        await message.answer("Неверный код, попробуй ещё раз")


# ---------------- РАЗДЕЛЫ ДЛЯ ВСЕХ ----------------


@dp.message(F.text == "1 слово")
async def one_word(message: Message):
    await message.answer("Учитывая все твои качества и твою разносторонность, наверное все таки нельзя описать тебя одним словом, но твои близкие попробовали сделать это!✨ Давай узнаем какие варианты у них получились!💖\n\n"
        "1. Лучший друг\n"
        "2. Вайб\n"
        "3. Любовь\n"
        "4. Сын\n"
        "5. Красавец\n"
        "6. Котя\n"
        "7. Брат\n"
        "8. Кудрявый\n"
        "9. Красавец\n"
        "10. Мужчина\n"
        "11. Барашек/Баленсиага\n"
        "12. Крутой\n"
        "13. Снеговик\n"
        "14. player\n"
        "15. Доброта\n"
        "16. Мужчина\n"
        "17. Роднулька\n"
    )


@dp.message(F.text == "Профессия")
async def profession(message: Message):
    await message.answer("Стоп!Стоп!Стоп!✋ Я знаю, что профессию ты должен выбирать сам,но я думаю, что тебе было бы интересно, в какой професии тебя видит твоя семья и твои друзья.💸Поэтому читай свою мини *профореинтацию*👷\n\n"
        "1. Фрилансер\n"
        "2. Экономист\n"
        "3. Предприниматель\n"
        "4. Креативный директор или продюсер\n"
        "5. Дипломат\n"
        "6. Педагог\n"
        "7. Гонщик ф1\n"
        "8. Репер\n"
        "9. Уролог\n"
        "10. Программист\n"
        "11. Миллиардер\n"
        "12. Продюсер\n"
        "13. Повар х2\n"
        "14. Кладмен\n"
        "15. Управляющий отелем\n"
        "16. Миллионер\n"
        "17. Програмист\n"
    )

    # photo = FSInputFile("photo.jpg")
    # await message.answer_photo(photo)


@dp.message(F.text == "Характер")
async def character(message: Message):
    await message.answer("У тебя прекрасный характер, но вот какие черты твоего характера выделили твои близкие:\n"
        "1.Креативность\n"
        "2.Уверенность\n"
        "3.Антинытье\n"
        "4.Достигаторство\n"
        "5.Вниматльность\n"
        "6.Спокойствие\n"
        "7.Недежный, взаимно ласковый\n"
        "8.Веселый\n"
        "9.Чистюля\n"
        "10.Оптимизм х2\n"
        "11.Отзывчивость\n" 
        "12.Искренность\n"
        "13.Честность\n"
        "14.Решительность\n"
        "15.Абмициозность\n"
        "16.Кудрявый\n"
  )

@dp.message(F.text == "Ассоциации")
async def song(message: Message):
    await message.answer("В этом разделе ты узнаешь с какими артистами и песнями ты ассоциируешься у своих близких.🕺🏽🎶 Ассоциации с определенными песнями зачастую связаны с воспоминаниями, а ассоциации с артистами могут показать твое поведение в обществе со стороны🎵\n\n"
        "Песни и артисты:\n"
        "1. ROCKET - Убитый\n"
        "2. Чиж и К - О любви\n"
        "3. Джо Дассен\n"
        "4. FENDIGLOCK - Движет\n"
        "5. FRIENDLY THUG\n"
        "6. Kai Аngel - godmode\n"
        "7. Kai Angel - john galliano\n"
        "8. Григорий Лепс\n"
        "9. August - Jimi Hndrx\n"
        "10. LILDRUGHILL - Adrenaline\n"
        "11. PLOXOYPAREN - ПЛАНЕТЫ\n"
        "12. ROCKET - Boenos Dias\n"
        "13. August - Jimi Hndrx\n"
        "14. Kai Angel - 101 причина\n"
        "15. Фунтик - хорошо бродить по свету...\n"
        "16. Леонид Агутин\n"
        "17. Валентина толкунова - носики-курносики\n"
        "18. Karna.val - Ромашки\n"
        "19. SQWORE\n"
        "20. PHARAOH - Эми\n"
    )

    # audio = FSInputFile("audio.mp3")
    # await message.answer_audio(audio)



@dp.message(F.text == "Животное")
async def animal(message: Message):
    await message.answer("✨Давай пофантазируем, что ты чудесным образом превратился в какое-то животное.🦁 Как думаешь, кем бы ты стал? Твои близкие уже сделали свои предположения,читай их ниже)\n\n"
        "1. Львом х4\n"
        "2. Псом кудрявым\n"
        "3. Лисёнком\n"
        "4. Котеем\n"
        "5. Хомячком\n"              
        "6. Снежным барсом\n"
        "7. Псом\n"
        "8. Барашком\n"       
        "9. Хорьком\n"
        "10. Пуделем\n"
        "11. Ящерицой\n"
        "12. Котиком\n"
        "13. goat'ом\n"
        "14. Волком\n"
        "15. Лабрадором\n"
        "17. Самоедом\n"
                
        
    )

    # photo = FSInputFile("photo.jpg")
    # await message.answer_photo(photo)


# ---------------- ТОЛЬКО ДЛЯ СТЕПЫ ----------------

@dp.message(F.text == "Описание и мнения")
async def opinions(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != UserState.stepa:
        return

    await message.answer("Хм... Тебе когда нибудь было интересно, что о тебе думают другие?👀 А я это узнала!))💌 Читай скорее! ...Это секрет!...🙊\n\n"
        "Родной, любимый, всегда надежный и  большой помощник нам во всем, 100% справедливый, вдумчивый, хороший друг и товарищ, добрый, засоня)\n\n"
                         
        "степа добрый перец , не унывает и ищет выход из любой ситуации , всегда доказывает свою точку зрения\n\n"
                         
        "с-смелый\n"
        "т-творец\n"
        "ё-ёбнутый (в хорошем смысле хввххв)\n"
        "п-прикольный\n"
        "а-амбициозны\n"
        "н-надежный\n\n"

                         
        "Здравый, инициативный пацан, у которого все в жизни будет ахуенно\n\n"

        "Человек который может взять на себя инициативу, искренний, умный, понимает чего хочет от жизни\n\n"

        "вайбовый братик, всегда на позитиве, можно поговорить на любую тему\n\n"
                         
        "Самый лучший, любимый, красивый, сильный, умный, секси человек  на планете. Не могу представить более похожего на меня и подходящего для меня человека. может быть спокойным, но и очень веселым и активным, лидер, знает что делать в сложных ситуациях. иногда прав ;)\n\n"

        " хороший друн, который не ноет и че то знает🤫\n\n"

        " Красивенький, смазливый пацык, не селюк, лучший волк стая брат\n\n"

        "Человек в нашей семье на которого всегда можно положиться!\n\n"
        
        "с - сногсшибательный\n"
        "т - топовый\n"
        "е - единственный\n"
        "п - прикольненький\n"
        "а - артистичный\n\n"

        "Степа очень веселый и жизнерадостный человек, человек, который всегда твердо стоит на своем, ценит близких, готов всегда прийти на помощь\n\n"

        "искренний браток, порядочный семьянин\n\n"
 )


   # audio = FSInputFile("audio.mp3")
    # await message.answer_audio(audio)
    

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message(F.text == "Взгляд со стороны")
async def view(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != UserState.stepa:
        return
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Посмотри, как ты выглядишь со стороны 💛", url="https://disk.yandex.ru/a/PvtQIllxk5qmkg")]
        ]
    )

    await message.answer(
        "Нажми на кнопку ниже 👇",
        reply_markup=kb
    )


@dp.message(F.text == "Кто лучше знает?")
async def quiz(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != UserState.stepa:
        return

    await message.answer("Тебе интересно,кто же из твоих близких тебя лучше знает?В файле есть заполненные анкеты,открой его и узнай, кто как ответил))")

    quizFile = FSInputFile("document.pdf")
    await message.answer_document(quizFile)


@dp.message(F.text == "Пожелания")
async def wishes(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != UserState.stepa:
        return
    
    await message.answer("Текстовые пожелания:\n\n"
                          
      " Аня : поздравляю тебя, мальчик мой. Ты перешел на новый этап, я верю в тебя и знаю, что ты самый-самый молодец, бесконечно люблюююю!!\n\n"
      "Матвей : Желаю тебе счастья, здоровья, любовь уже крепкая у тебя, так что норм , и сдать все экзамены хорошо и поступить куда желаешь брат\n\n"
      "Игорь:  Желаю тебе брат добиться всего того, что ты хочешь, чтобы близкие всегда были рядом и поддерживали тебя,  чтобы ты оставался таким же усердным и огонь в твоих глазах никогда не угасал\n\n"
      "Саймон : степа с днюхой, желаю оставаться таким же ахуенным и добрым типом, и самое главное здоровья\n\n"
      "Вика: хэппи бездей😔 теперь ты совсем большой, вот таким вот помню🤏 теперь мне не надо ходить тебе за пивом, дорос - сам справишься. хочу, чтобы ты всегда был счастлив и в прайме. безмерно люблю 💖 \n\n"
      "Илья: Степа, поздравляю тебя с днем рождения, желаю счастья в личной жизни, здоровья тебе и твои близким, успехов во всем и удачи\n\n"
    )


    from aiogram.types import FSInputFile

    await message.answer_audio(
        audio=FSInputFile("yura.mp3"),
        title="yura"
    )

    await message.answer_audio(
        audio=FSInputFile("roma.mp3"),
        title="roma"
    )

    await message.answer_audio(
        audio=FSInputFile("smolyak.mp3"),
        title="smolyak"
    )

    await message.answer_audio(
        audio=FSInputFile("arsen.mp3"),
        title="arsen"
    )

    await message.answer_audio(
        audio=FSInputFile("kosta.mp3"),
        title="kosta"
    )

    await message.answer_audio(
        audio=FSInputFile("rus.mp3"),
        title="rus"
    )



# ---------------- ПЕРЕЗАПУСК ----------------

@dp.message(F.text == "Перезапуск")
async def restart(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Бот перезапущен 💫\n\nПривет! Кто ты? Именинник или Гость?",
        reply_markup=start_keyboard()
    )


# ---------------- ЗАПУСК ----------------

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
