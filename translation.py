class Translation(object):
    START_TEXT = """<b>Heya!!\n\nPlease Enter your Telegram Phone Number, to get the APP ID & API HASH from <a href="https://my.telegram.org/apps">Telegram</a></b>\n\n<i>(<b>Note :</b> The Phone No. must include the country code and if something goes wrong, stop the bot and send /start again.)</i>\n\n<i>Example : +91 9*6*3 4*2*1</i>"""
    AFTER_RECVD_CODE_TEXT = """<b>Now enter the code you received :</b>\n\n<b>/start at any stage to re-enter your details</b>"""
    BEFORE_SUCC_LOGIN = "YaY!! Received the code, Scrapping the web page ...\n\nWi8 and rest for a while till I do the rest of work."
    ERRED_PAGE = "Ooops!! SOMETHIN W3NT WRONG 🤔"
    CANCELLED_MESG = "C..YA!! Please re /start the bot conversation."
    IN_VALID_CODE_PVDED = "Sorry, but the input does not seem to be a valid Telegram Web-Login code !! Please re-check and try again."
    IN_VALID_PHNO_PVDED = "Sorry, but the input does not seem to be a valid phone number !! Please re-check and try again."
