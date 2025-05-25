from aiogram import types, F, Router
from aiogram.filters import Command

router = Router()

@router.message(F.text.startswith("/start"))
async def start_cmd(message: types.Message) -> None:
    global full_name
    full_name = message.from_user.full_name
    kb = [
        [types.InlineKeyboardButton(text='Обо мне', callback_data='about_me')],
        [types.InlineKeyboardButton(text='Мои раБоты🤖', callback_data='portfolio'),
         types.InlineKeyboardButton(text='Мое образование📖', callback_data='study')],
        [types.InlineKeyboardButton(text='Написать мне📝', url='https://t.me/misheninrb')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f'🙋Приветствую, {full_name}!\n'
                         'Данный бот = мое портфолио🤖\n'
                         'Для изучения подробной информации:\n'
                         'воспользуйтесь кнопками ниже ⬇️', reply_markup=keyboard)

@router.callback_query(F.data == 'menu')
async def menu_cmd(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text='Обо мне', callback_data='about_me')],
        [types.InlineKeyboardButton(text='Мои раБоты🤖', callback_data='portfolio'),
         types.InlineKeyboardButton(text='Мое образование📖', callback_data='study')],
        [types.InlineKeyboardButton(text='Написать мне📝', callback_data='write_me')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'🙋Приветствую, {full_name}!\n'
                         'Данный бот = мое портфолио🤖\n'
                         'Для изучения подробной информации:\n'
                         'воспользуетесь кнопками ниже ⬇️', reply_markup=keyboard)
    
@router.callback_query(F.data == 'about_me')
async def about_me_cb(callback: types.CallbackQuery):
    kb = [[types.InlineKeyboardButton(text='⬅️Вернуться', callback_data='menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
    'ИТ-специалист.\n' \
    'Работаю в Департаменте ИТ г. Москвы.\n' \
    'Занимаюсь автоматизацией, созданием Telegram-ботов и баз данных.\n' \
    'Работаю быстро, понятно и по делу.',
    reply_markup=keyboard
    )

@router.callback_query(F.data == 'portfolio')
async def portfolio_cmd(callback: types.callback_query):
    kb = [[types.InlineKeyboardButton(text='⬅️Вернуться', callback_data='menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
    'В список моих работ входит:\n'
    '@MisheninRB_bot - текущий бот.\n'
    '@collect_quest_bot - выполняет роль ассистента для HR-специалистов. ' \
    'Собирает анкеты от пользователей, направляет их в отдельный канал (архив), ' \
    'и также дает пользователю ссылку на прохождение собеседования.', reply_markup=keyboard)

@router.callback_query(F.data == 'study')
async def study_cmd(callback: types.callback_query):
    kb = [[types.InlineKeyboardButton(text='⬅️Вернуться', callback_data='menu')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Закончил курсы:\n' \
    ' - "Поколение Python": курс для начинающих. \n' \
    ' - "Поколение Python": курс для продвинутых. \n' \
    ' - "Web-dev для начинающих": HTML и CSS. \n' \
    ' - "Основы Python": создание телеграм-бота. \n' \
    ' - "Создание телеграм ботов с нуля". ', reply_markup=keyboard)
