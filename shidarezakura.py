import discord
import sys


is_debug = True
debug_room_name = 'yuppibot-debug'


class ShidarezakuraClient(discord.Client):
    async def on_ready(self):
        print('login')

        guild = discord.utils.get(self.guilds, name='ProLab++')
        print(guild)

    async def on_message(self, message):
        if ':vote' in message.content:
            for emoji in ('👎', '\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}', '\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}', '\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}', '\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}', '\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}', '👍'):
                await message.add_reaction(emoji)


def main():
    token = ''
    with open('token.tk') as f:
        token = f.read().strip()

    client = ShidarezakuraClient()
    client.run(token)


if __name__ == "__main__":
    main()
