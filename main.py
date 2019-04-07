import random
import threading
import traceback
from math import sqrt

import discord
import asyncio
import json

from pathlib import Path
import urllib.request

import uuid

import os


import requests
import lxml.html, lxml.etree

import mysql_data



client = discord.Client()

def get_value(dict, key):
    if(key in dict):
        return dict[key]
    return ''

def get_channel_object(name):
    #print("=================")
    for server in client.servers:
        for channel in server.channels:
            #print(channel.name+" "+channel.id)
            if(channel.name == name):
                return channel


@client.event
async def on_ready():
    print('Loggid in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    discord.Status
    #bot_game = discord.Game(name="Єдина Україна", url="http://ed.dobrijzmej.org", type=0)
    #await client.change_presence(game=bot_game)

@client.event
async def on_message(message):

    prefix = '!'

    if client.user.mentioned_in(message):
        await on_mention_me(message)

    if message.content.startswith(prefix+"я "):
        await on_safe_cmdr_name(message)

    if "слава україні" in message.content.lower() or "слава украине" in message.content.lower():
        if message.author.id != client.user.id:
            await client.send_message(message.channel, message.author.mention+", героям слава!")

@client.event
async def on_member_join(member):
    if(member.server.name != 'Elite Dangerous Україна'):
        return
    nick = member.nick
    if nick:
        nick = " ("+nick+")"
    else:
        nick = ''
    print(str(member.server.name))
    # await client.send_message(get_channel_object('bots'), "@"+str(member) + nick +", ласкаво просимо до серверу української спільноти гри Elite Dangerous!\r\nЯ можу тобі дещо підказати, якщо ти напишеш `!допомога`")
    await client.send_message(get_channel_object('bots'), member.mention + nick +", ласкаво просимо до серверу української спільноти гри Elite Dangerous!\r\nЯ можу тобі дещо підказати, якщо ти напишеш `!допомога`")
    await client.send_message(get_channel_object('general'), member.mention + nick +", слава Україні!")


""" ================== сохранить имя командира ============================="""
async def on_safe_cmdr_name(message):
    """in_server, in_cmdr_mention, in_cmdr_name"""
    new_name = ""
    message_args = message.content.split()
    for n in message_args[1:]:
        if(new_name!=''):
            new_name += " "
        new_name += n
    print("new_name="+new_name)
    
    site_url = "https://uca.co.ua/pilot/registry/"
    pilots_count = mysql_data.check_pilot(new_name);
    discords_count = mysql_data.check_discord_id(message.author.id);
    if(pilots_count == 0 and discords_count == 0):
        user_uuid = uuid.uuid4().hex
        mysql_data.registry_pilot(new_name, message.author.id, user_uuid)
        await client.send_message(message.author, "Доречі, я підготував для тебе особистий кабінет на сторінці нашої спільноти, можеш зареєструватися щє й там: "+site_url+user_uuid)
        return
    if(pilots_count!=0):
        user_uuid = mysql_data.get_uid_by_pilot(new_name)
        await client.send_message(message.author, "Доречі, я все щє очікую, коли ти зарєструешся у своєму кабінеті на нашому сайті: "+site_url+user_uuid)
        return
    if(discords_count!=0):
        user_uuid = mysql_data.get_uid_by_pilot(new_name)
        await client.send_message(message.author, "Доречі, я все щє очікую, коли ти зарєструешся у своєму кабінеті на нашому сайті: "+site_url+user_uuid)

""" ================== обращение к роботу ============================="""
async def on_mention_me(message):
    print(message.server.name)
    print(message.content)
    print(message.channel.id, message.channel.name)
    if(str(message.server.id) != '276054497716076546'):
        return 0
    args = message.content.split()
    if(args[1] == 'help'):
        await on_help_en(message)
        return

    with open('adages.json', 'r') as f_adages:
        j_adages = json.loads(f_adages.read())
    #print(len(j_adages['adages']))
    adage_index = random.randint(0, len(j_adages['adages'])-1)
    prefix = ["як казав мій батько,", "древні казали:", "колись в космічному просторі почув, що", "у Києві кажуть, що", "чи знаєте ви, що"]
    prefix_index = random.randint(0, len(prefix)-1)
    #print(prefix_index)
    await client.send_message(message.channel, message.author.mention+", "+prefix[prefix_index]+' "'+j_adages['adages'][adage_index]+'"')


client.run('MjkyNzA1OTA2NzIwNzY4MDAx.DkhoUw.FaFJQmelVNJze-uVwkLt12RQh6U')
#await client.connect()
#await client.login(token='MjkyNzA1OTA2NzIwNzY4MDAx.C7wbYQ.s3Wu5gFopQn6zP05Mn-O1WeTpdg', bot=True)

