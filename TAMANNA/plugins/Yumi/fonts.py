# ---------------------------------------------------------
# BeatGuard Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the BeatGuard Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BeatGuard.utils.Sona_font import Fonts
from BeatGuard import app

@app.on_message(filters.command(["font", "fonts"]))
async def style_buttons(c, m):
    if len(m.text.split(" ", 1)) < 2:
        return await m.reply_text("Please provide some text after /fonts command.")

    text = m.text.split(" ", 1)[1]

    buttons = [
        [
            InlineKeyboardButton("𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛", callback_data="style+typewriter"),
            InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
            InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
        ],
        [
            InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒇", callback_data="style+bold_cool"),
            InlineKeyboardButton("𝑆𝑒𝑟𝑖𝑓", callback_data="style+cool"),
            InlineKeyboardButton("Sᴍᴀʟʟ Cᴀᴘs", callback_data="style+small_cap"),
        ],
        [
            InlineKeyboardButton("𝓈𝒸𝓇𝒾𝓅𝓉", callback_data="style+script"),
            InlineKeyboardButton("𝓼𝓬𝓻𝓲𝓹𝓽", callback_data="style+script_bolt"),
            InlineKeyboardButton("ᵗⁱⁿʸ", callback_data="style+tiny"),
        ],
        [
            InlineKeyboardButton("ᑕOᗰIᑕ", callback_data="style+comic"),
            InlineKeyboardButton("𝗦𝗮𝗻𝘀", callback_data="style+sans"),
            InlineKeyboardButton("𝙎𝙖𝙣𝙨", callback_data="style+slant_sans"),
        ],
        [
            InlineKeyboardButton("𝘚𝘢𝘯𝘴", callback_data="style+slant"),
            InlineKeyboardButton("𝖲𝖺𝗇𝗌", callback_data="style+sim"),
            InlineKeyboardButton("Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data="style+circles"),
        ],
        [
            InlineKeyboardButton("🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎", callback_data="style+circle_dark"),
            InlineKeyboardButton("𝔊𝔬𝔱𝔥𝔦𝔠", callback_data="style+gothic"),
            InlineKeyboardButton("𝕲𝖔𝖙𝖍𝖎𝖈", callback_data="style+gothic_bolt"),
        ],
        [
            InlineKeyboardButton("Cloud", callback_data="style+cloud"),
            InlineKeyboardButton("Happy", callback_data="style+happy"),
            InlineKeyboardButton("Sad", callback_data="style+sad"),
        ],
        [
            InlineKeyboardButton("Special", callback_data="style+special"),
            InlineKeyboardButton("Squares", callback_data="style+squares"),
            InlineKeyboardButton("Bold Squares", callback_data="style+squares_bold"),
        ],
        [
            InlineKeyboardButton("Andalucia", callback_data="style+andalucia"),
            InlineKeyboardButton("Manga", callback_data="style+manga"),
            InlineKeyboardButton("Stinky", callback_data="style+stinky"),
        ],
        [
            InlineKeyboardButton("Bubbles", callback_data="style+bubbles"),
            InlineKeyboardButton("Underline", callback_data="style+underline"),
            InlineKeyboardButton("Ladybug", callback_data="style+ladybug"),
        ],
        [
            InlineKeyboardButton("Rays", callback_data="style+rays"),
            InlineKeyboardButton("Birds", callback_data="style+birds"),
            InlineKeyboardButton("Slash", callback_data="style+slash"),
        ],
        [
            InlineKeyboardButton("Stop", callback_data="style+stop"),
            InlineKeyboardButton("Skyline", callback_data="style+skyline"),
            InlineKeyboardButton("Arrows", callback_data="style+arrows"),
        ],
        [
            InlineKeyboardButton("Qvnes", callback_data="style+qvnes"),
            InlineKeyboardButton("Strike", callback_data="style+strike"),
            InlineKeyboardButton("Frozen", callback_data="style+frozen"),
        ],
        [InlineKeyboardButton("✖️ Close", callback_data="close_reply")]
    ]

    await m.reply_text(f"`{text}`", reply_markup=InlineKeyboardMarkup(buttons), quote=True)


@app.on_callback_query(filters.regex("^style"))
async def style(c, m):
    await m.answer()
    _, style = m.data.split('+')

    font_map = {
        "typewriter": Fonts.typewriter,
        "outline": Fonts.outline,
        "serif": Fonts.serief,
        "bold_cool": Fonts.bold_cool,
        "cool": Fonts.cool,
        "small_cap": Fonts.smallcap,
        "script": Fonts.script,
        "script_bolt": Fonts.bold_script,
        "tiny": Fonts.tiny,
        "comic": Fonts.comic,
        "sans": Fonts.san,
        "slant_sans": Fonts.slant_san,
        "slant": Fonts.slant,
        "sim": Fonts.sim,
        "circles": Fonts.circles,
        "circle_dark": Fonts.dark_circle,
        "gothic": Fonts.gothic,
        "gothic_bolt": Fonts.bold_gothic,
        "cloud": Fonts.cloud,
        "happy": Fonts.happy,
        "sad": Fonts.sad,
        "special": Fonts.special,
        "squares": Fonts.square,
        "squares_bold": Fonts.dark_square,
        "andalucia": Fonts.andalucia,
        "manga": Fonts.manga,
        "stinky": Fonts.stinky,
        "bubbles": Fonts.bubbles,
        "underline": Fonts.underline,
        "ladybug": Fonts.ladybug,
        "rays": Fonts.rays,
        "birds": Fonts.birds,
        "slash": Fonts.slash,
        "stop": Fonts.stop,
        "skyline": Fonts.skyline,
        "arrows": Fonts.arrows,
        "qvnes": Fonts.rvnes,
        "strike": Fonts.strike,
        "frozen": Fonts.frozen,
    }

    cls = font_map.get(style)
    if not cls:
        return

    try:
        original_text = m.message.reply_to_message.text
        styled = cls(original_text.split(" ", 1)[1])
        await m.message.edit_text(styled, reply_markup=m.message.reply_markup)
    except:
        pass
