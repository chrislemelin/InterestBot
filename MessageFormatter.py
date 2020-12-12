import discord
import textwrap

max_description_size = 300

title = "{user} wants to play {game}"
board_game_geek_url = "https://boardgamegeek.com/boardgame/{id}/"


def format_description(description):
    if len(description) > max_description_size:
        return textwrap.wrap(description, max_description_size)[0] + "..."
    return description


def format_creation_embed(author, game):
    #    print(dir(game))
    embed = discord.Embed(title=title.format(user=author.name, game=game.name),
                          url=board_game_geek_url.format(id=game.id))
    embed.description = format_description(game.description)
    embed.set_thumbnail(url=game.thumbnail)
    embed.add_field(name="Number of players",
                    value=str(game.min_players) + "-" + str(game.max_players), inline=True)
    embed.add_field(name="Average Playtime",
                    value=game.playing_time, inline=True)

    return embed


def modify_content(current_content, user, reaction):
    broken_up_context = current_content.split(" ")
    reaction_and_user_list = []

    for current_index in range(len(broken_up_context)//2):
        reaction_and_user_list.append((
            broken_up_context[current_index*2], broken_up_context[current_index*2+1]))

    list_without_user = list(filter(lambda content_pair: mention_string_to_user_id(
        content_pair[1]) != str(user.id), reaction_and_user_list))
    if (len(list_without_user) == len(reaction_and_user_list)):
        list_without_user.append(
            (reaction.emoji, user_id_to_mention_string(user.id)))
    return reaction_and_user_list_to_string(list_without_user)


def user_id_to_mention_string(user_id):
    return "<@" + str(user_id) + ">"


def mention_string_to_user_id(mention):
    return mention[2:len(mention)-1]


def reaction_and_user_list_to_string(reaction_and_user_list):
    content_string = ""
    for reaction_and_user in reaction_and_user_list:
        content_string = content_string + \
            str(reaction_and_user[0]) + " " + str(reaction_and_user[1])
    return content_string
