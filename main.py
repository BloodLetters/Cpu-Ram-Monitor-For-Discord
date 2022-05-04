from time import sleep

import psutil
import discord
import JsonReader
import datetime

client = discord.Client()
reload = 1


@client.event
async def on_ready():
    print('[!] Log in as {0.user}'.format(client))
    if JsonReader.getChannelID() == 0:
        await client.close()
        print("[!] Insert Your Discord Channel ID in Config.json")
        quit(0)

    elif JsonReader.getMessageID() == 0:
        await embed()
        await client.close()
        print("[!] Copy The Bot embed in your Channel!")
        quit(0)

    else:
        try:
            while True:
                sleep(reload)
                await embed()
        except KeyboardInterrupt:
            pass


@client.event
async def embed():
    if JsonReader.getMessageID() == 0:
        msgid = client.get_channel(JsonReader.getChannelID())
        dummyEmbed = discord.Embed(title="Dummy Embed",
                                   description="Copy This Embed Id",
                                   color=0xFF5733)
        await msgid.send(embed=dummyEmbed)
    elif JsonReader.getMessageID() != 0:
        cpu = str(psutil.cpu_percent(reload))
        ram = str(psutil.virtual_memory()[2])

        embed_lama = await client.get_channel(JsonReader.getChannelID()).fetch_message(JsonReader.getMessageID())
        embed = discord.Embed(title=JsonReader.getTitle(1), url=JsonReader.getTitle(2),
                              description=JsonReader.getDescription(), color=0x1bf10b,
                              timestamp=datetime.datetime.utcnow())
        embed.set_author(name=JsonReader.getAuthor(1), url=JsonReader.getAuthor(2))
        embed.set_thumbnail(url=JsonReader.getThumbnail())
        embed.add_field(name=JsonReader.getFields("cpu", 1),
                        value=str(JsonReader.getFields("cpu", 2)).replace("{CPU}", cpu), inline=True)
        embed.add_field(name=JsonReader.getFields("ram", 1),
                        value=str(JsonReader.getFields("ram", 2)).replace("{RAM}", ram), inline=True)
        await embed_lama.edit(embed=embed)
    else:
        print("Error with embed!")


client.run(JsonReader.getToken())