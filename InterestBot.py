import os
import discord
from discord.ext import commands
import GameFetcher
import MessageFormatter
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("api-token")
bot = discord.ext.commands.Bot(command_prefix='!')


thumbs_up = "👍"
can_teach = "📖"
delete = "❌"


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_reaction_add(reaction, user):
    if (user == bot.user):
        return

    await reaction.remove(user)

    if (reaction.emoji != thumbs_up and reaction.emoji != can_teach):
        return

    await reaction.message.edit(content=MessageFormatter.modify_content(reaction.message.content, user, reaction))


@bot.command(content=True, name='create', help='gauge intreset in a game')
async def getGame(ctx, game_name: str):
    game = GameFetcher.fetch(game_name)
    if game is None:
        await ctx.send("Sorry, I cannot find the game {game}, please check the spelling".format(game_name))
    else:
        sent_message = await ctx.send(embed=MessageFormatter.format_creation_embed(ctx.message.author, game))
        print(sent_message)
        await sent_message.add_reaction(thumbs_up)
        await sent_message.add_reaction(can_teach)
        await sent_message.add_reaction(delete)

bot.run(token)
