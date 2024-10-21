class script(object):
    START_TXT = """𝗩𝗮𝗻𝗮𝗸𝗸𝗮𝗺 𝗡𝗮𝗻𝗯𝗮/𝗡𝗮𝗻𝗯𝗶 {},
𝗠𝘆 𝗡𝗮𝗺𝗲 𝗜𝘀 <a href=https://t.me/{}>{}</a>, 𝗜 𝗖𝗮𝗻 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗦𝗰𝗲𝗻𝗲𝗽𝗮𝗰𝗸𝘀 𝗼𝗳 𝗠𝗼𝘃𝗶𝗲𝘀, 𝗝𝘂𝘀𝘁 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗮𝗻𝗱 𝗚𝗲𝘁 𝗦𝗰𝗲𝗻𝗲𝗽𝗮𝗰𝗸𝘀 ✌️"""
    HELP_TXT = """𝐇𝐞𝐲 {}
𝐇𝐨𝐰 𝐜𝐚𝐧 𝐈 𝐇𝐞𝐥𝐩 𝐘𝐨𝐮."""
    ABOUT_TXT = """🤖 𝗠𝗬 𝗡𝗔𝗠𝗘: {}
🧑‍💻 𝗖𝗥𝗘𝗔𝗧𝗢𝗥: <a href=https://t.me/balafxig>BalaFx</a>
📖 𝗟𝗜𝗕𝗥𝗔𝗥𝗬: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
📜 𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
💾 𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
⚙️ 𝗕𝗢𝗧𝗦𝗘𝗥𝗩𝗘𝗥: KOYEB
🚧 𝗕𝗨𝗜𝗟𝗗 𝗦𝗧𝗔𝗧𝗨𝗦: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- CutsandClipsBot is a open source project. 
- Source - Private

<b>DEVS:</b>
- <a href=https://t.me/balafxig>BalaFx</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. CutsandClipsBot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- CutsandClipsBot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. CutsandClipsBot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/balafxig)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """📂 ​🇹​​🇴​​🇹​​🇦​​🇱​ ​🇫​​🇮​​🇱​​🇪​​🇸​ : <code>{}</code>
👤 ​🇹​​🇴​​🇹​​🇦​​🇱​ ​🇺​​🇸​​🇪​​🇷​​🇸​: <code>{}</code>
💬 ​🇹​​🇴​​🇹​​🇦​​🇱​ ​🇨​​🇭​​🇦​​🇹​​🇸​: <code>{}</code>
🗄️ ​🇺​​🇸​​🇪​​🇩​ ​🇸​​🇹​​🇴​​🇷​​🇦​​🇬​​🇪​: <code>{}</code> 𝙼𝚒𝙱
💾 ​🇫​​🇷​​🇪​​🇪​ ​🇸​​🇹​​🇴​​🇷​​🇦​​🇬​​🇪​: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
