'''
#Azat will edit this
import asyncio

import nextdiscord as discord

from libs import get_sub


async def command(client, message):
    duration = get_sub(message.content, 0, 10)
    counter = 0
    duration = int(duration)
    if duration > 212:
        duration = 212
    msg = await client.send_message(message.channel,
                                    ":musical_note: Never gonna give you up, never gonna let you down ... ( ͡° ͜ʖ ͡°)")
    try:
        if message.author.voice_channel is not None:
            try:
                voice = await client.join_voice_channel(message.author.voice_channel)
                player = voice.create_ffmpeg_player('./res/rick_roll.mp3')
                player.start()
                while not counter >= duration:
                    await asyncio.sleep(1)
                    counter = counter + 1
                await voice.disconnect()
                player.stop()
            except discord.errors.ClientException:
                await client.edit_message(msg, "{} you let me down, I'm already connected!".format(
                    message.author.mention))
        else:
            await client.edit_message(msg,
                                      "Hey, {} you need to join a voice channel!".format(message.author.mention))
    except AttributeError:
        await client.edit_message(msg, "**You can't use me in your private DMs, you creep.**")


async def help(client, message):
    em = discord.Embed(title="Help: +rickroll",
                       color=discord.Color.blue(),
                       description="""
Plays Rick Astleys 'Never Gonna Give You Up' in current voice channel.
+rickroll *[seconds]* (default is 10)
**Example usage:** +rickroll 10
""")
    await client.send_message(message.channel, embed=em)
    return


async def error(client, message):
    em = discord.Embed(title="Missing required argument:",
                       color=discord.Color.red(),
                       description="""
Plays Rick Astleys 'Never Gonna Give You Up' in current voice channel.
+rickroll *[seconds]* (default is 10)
**Example usage:** +rickroll 10
""")
    await client.send_message(message.channel, embed=em)
    return
