from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#============================================================================
menu_kb1 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Направления")]
],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт в меню."
)

menu_kb2 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="👨‍💻Программирование на Python"), KeyboardButton(text="🥽VR/AR-разработка")],
        [KeyboardButton(text="🌐Веб-разработка"), KeyboardButton(text="📱Мобильная разработка")],
        [KeyboardButton(text="⚙️Системное администрирование"), KeyboardButton(text="✈️Беспилотные авиационные системы")],
        [KeyboardButton(text="🧊3D-моделирование"), KeyboardButton(text="🎓Как поступить в IT-Cube")]
],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт в меню."
)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝Записаться на обучение", url="https://it-cube39.ru/sign-up")]
])
#============================================================================

#============================================================================
inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info1"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/python")]
])

inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info2"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/vr-ar")]
])

inline_kb3 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info3"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/web")]
])

inline_kb4 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info4"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/mobile-development")]
])

inline_kb5 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info5"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/system-administration")]
])

inline_kb6 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info6"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/uav")]
])

inline_kb7 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Доп. информация", callback_data="info7"), InlineKeyboardButton(text="➡️Перейти на сайт⬅️", url="https://it-cube39.ru/directions/3d")]
])
#============================================================================