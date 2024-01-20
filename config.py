import os
token = os.getenv("bot_token")
bot_name = "ᴋᴇᴇᴘᴇʀ [,]"
cmd_prefix = ","
scammers_filename = "scammers.txt"
scammers_list = [line.strip().lower() for line in open(scammers_filename)]
