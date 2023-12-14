from telethon.tl.custom import Button

__help__ = """
*Admins Only*

 /nightmode*:* Adds Group to NightMode Chats
 /rmnight*:* Removes Group From NightMode Chats

*Note:* Night Mode chats get Automatically closed at 12 am(IST) and Automatically opened at 6 am(IST) to Prevent Night Spam.

*Additional Options:*
 - `/nightmodehelp`: Show additional commands for Night Mode settings
"""

# Add URL buttons under the message
__help__ += "\n*Additional Options:*"
__help__ += f"\n - {Button.inline('Enable Night Mode', data='enable_night_mode')}"
__help__ += f"\n - {Button.inline('Disable Night Mode', data='disable_night_mode')}"
__help__ += f"\n - {Button.url('Visit our Website', url='http://yourwebsite.com')}"
__help__ += f"\n - {Button.url('GitHub Repository', url='https://github.com/your_username/your_repo')}"

__mod_name__ = "Night mode"
