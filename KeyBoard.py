from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#============================================================================
menu_kb1 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Направления"), KeyboardButton(text="О IT-Cube🎲")]
],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт в меню."
)

menu_kb2 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Программирование на Python"), KeyboardButton(text="VR/AR-разработка")],
        [KeyboardButton(text="Веб-разработка"), KeyboardButton(text="Мобильная разработка")],
        [KeyboardButton(text="Системное администрирование"), KeyboardButton(text="Беспилотные авиационные системы")],
        [KeyboardButton(text="⬅️Назад"), KeyboardButton(text="3D-моделирование")]
],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт в меню."
)
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт IT-Cube", url="https://it-cube39.ru/directions")]
        ])
#============================================================================

#============================================================================
inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info1")]
])

inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info2")]
])

inline_kb3 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info3")]
])

inline_kb4 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info4")]
])

inline_kb5 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info5")]
])

inline_kb6 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info6")]
])

inline_kb7 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info7")]
])
#============================================================================