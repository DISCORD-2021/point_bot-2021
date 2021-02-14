import discord
import asyncio, openpyxl, time, datetime, os #모듈값 불러오기

from discord.ext import commands
from discord.utils import get


client = discord.Client()

command_prefix="."  # 명령어 접두사

@client.event
async def on_ready():
    while True:
        game = discord.Game(".도움")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(str(len(set(client.guilds))) + "개의 서버에서 " + str(len(set(client.get_all_members())))+ "명이 이용중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game("언제든지 .도움 을 채팅에 입력해 포인트 봇(V3)를 편리하게 이용하세요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        
@client.event
async def on_message(message):
    if message.content.startswith(f'{command_prefix}자기소개'):
        await message.channel.send("안녕! 나는 얄룽님이 개발해주신! 포인트봇(V3)야! 반가워~ 채팅창에 **`.도움`** 를 쳐봐!")
        
    #명령어 도움말 페이지 임베드
    if message.content.startswith(f'{command_prefix}도움'):
        embed = discord.Embed(title="도움말", description="**이 봇은 `LeeSin#5693 - 얄룽` 님에 의해 개발 되었습니다.**", color=0xffffff)
        embed.add_field(name="**도움**", value="**이 메시지를 보여줍니다.**", inline=False)
        embed.add_field(name="**정보**", value="**`각자의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**서버 초대하기**", value="**[클릭!](https://discord.com/invite/D7chQKTxTA)**", inline=False)
        embed.add_field(name="**포인트봇(V3) 초대하기**",value="**[바로가기](https://discord.com/api/oauth2/authorize?client_id=805064278469115905&permissions=8&scope=bot)**", inline=False)
        embed.add_field(name='**참고**', value='**포인트봇(V3) Ver 3.0\n명령어: `.`**', inline=False)
        embed.set_author(name="포인트봇(V3) 도움말",icon_url="https://i.imgur.com/uLDnDU3.png")
        embed.set_thumbnail(url="https://i.imgur.com/uLDnDU3.png")
        await message.channel.send(embed=embed)

    #관리자 전용 명령어 도움말 페이지 임베드
    if message.content.startswith(f'{command_prefix}관리'):
        embed = discord.Embed(title="(운영위원회 전용) 관리 도움말", description="**이 봇은 `LeeSin#5693 - 얄룽` 님에 의해 개발 되었습니다.**", color=0xffffff)
        embed.add_field(name="**청소**", value="**`청소 (갯수)만큼 채팅이 삭제됩니다.`**", inline=False)
        embed.add_field(name="**킥**", value="**`서버에서 해당 유저를 킥합니다.`**", inline=False)
        embed.add_field(name="**뮤트**", value="**`뮤트 (userid)를 입력할 경우, 해당 유저는 뮤트 됩니다.`**", inline=False)
        embed.add_field(name="**뮤트해제**", value="**`뮤트해제 (userid) 를 입력할 경우, (userid)는 뮤트 해제 됩니다.`**", inline=False)
        embed.add_field(name="**정보**", value="**`각자의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**---> **", value="**`정보(가입일, 이름, 아이디, 닉네임, 온(오프)라인상태)를 보여줍니다.`**", inline=False)
        embed.add_field(name="**---> **", value="**`[자리비움,다른용무중은 오프라인으로 인식됩니다.]`**")
        embed.add_field(name="**서버정보**", value="**`서버의 정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**유저정보**", value="**`서버 내의 유저정보를 보여줍니다.`**", inline=False)
        embed.add_field(name="**업타임(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**벤(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**경고(개발중)**", value="**`어머나 개발중이넹?`**", inline=False)
        embed.add_field(name="**서버 초대링크**", value="**[클릭!](https://discord.com/invite/D7chQKTxTA)**", inline=False)
        embed.add_field(name="**포인트봇(V3) 초대하기**",value="**[바로가기](https://discord.com/api/oauth2/authorize?client_id=805064278469115905&permissions=8&scope=bot)**", inline=False)
        embed.add_field(name='**참고**', value='**포인트봇(V3) Ver 3.0\n명령어: `.`**', inline=False)
        embed.set_author(name="포인트봇(V3) 도움말",icon_url="https://i.imgur.com/uLDnDU3.png")
        embed.set_thumbnail(url="https://i.imgur.com/uLDnDU3.png")
        await message.channel.send(embed=embed)

    #킥 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}킥'):
        if(message.author.guild_permissions.kick_members):
            try:
                user=message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason=message.content[25:]
                if(len(message.content.split(" ")) == 10):
                    reason="None"
                await user.send(embed=discord.Embed(title="킥", description=f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="✅ 킥 성공!", description=f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (킥)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.", color=0xff0000))
     

    #뮤트 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}뮤트'):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, send_messages=False)
                await message.channel.send(embed=discord.Embed(title="✅ 뮤트 성공!", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (뮤트)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color=0xff0000))
            return

    #뮤트해제 명령어 구문
    if(message.content.split(" ")[0] == f'{command_prefix}뮤트해제'):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(
                    int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, overwrite=None)
                await message.channel.send(embed=discord.Embed(title="✅ 뮤트해제 성공!", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="🛑 (뮤트해제)처리 도중 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="💢 권한 부족", description=message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없어요", color=0xff0000))
            return

    #청소 명령어 구문
    if message.content.startswith(f'{command_prefix}청소'):
        num = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=num)
        await message.channel.send(f"✅ {num}개의 메시지를 정상적으로 삭제 했어요!")


    #정보 명령어 구문
    if message.content.startswith(f'{command_prefix}정보'):
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention} 의 디스코드 가입일 : {date.year}년 {date.month}월 {date.day}일 ")
        await message.channel.send(f"{message.author.mention} 의 이름 : {user.name} | 아이디 : {user.id} | 닉네임 : {user.display_name}")
        await message.channel.send(user.status) #온라인, 오프라인 상태 표시


    #업타임 명령어 구문
    if message.content.startswith(f'{command_prefix}업타임'):
        uptime = str(uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"| {hours}시간 {minitues}분 {seconds}초 | 동안 작동되었어요!")


    #인증 명령어 구문
    if message.content.startswith(f'{command_prefix}인증'):
        user = message.author.id
        if user == 677821350114492446:
            await message.channel.send('🔍 정보 조회중...')
            await asyncio.sleep(3)
            await message.channel.send('🔍 ID 검색중...')
            await asyncio.sleep(3)
            await message.channel.send('✅ 로그인 성공!')
            await asyncio.sleep(1)
            await message.channel.send('✨ 환영합니다 ' + f"{message.author.mention}" + '님')
        else:
            await message.channel.send('🔍 정보 조회중...')
            await asyncio.sleep(3)
            await message.channel.send('🔍 ID 검색중...')
            await asyncio.sleep(3)
            await message.channel.send('❌ 로그인 실패!')
            await asyncio.sleep(1)
            await message.channel.send((f"{message.author.mention}")+ '님은 인증되지 않은 유저 입니다 ❗ ' + '인증채널에서 .인증 을 입력해서 인증해주세요! 💨💨')

    #(아이템) 상점 명령어 구문
    if message.content.startswith(f'{command_prefix}회의생성'):
        embed = discord.Embed(title="아이템 상점 🔖", description="🛒 아이템 목록! 다같이 쇼핑하자!!", color=0x00aaaa)
        embed.add_field(name="💴 등급 UP!", value="등급업을 하기 위한 일회용 아이템! - 1개당 5BP ||| 나중에 모아서! 등급업 해봐! 😆", inline=False)
        embed.add_field(name="💵 등급 UP!", value="등급업을 하기 위한 일회용 아이템! - 1개당 5BP ||| 나중에 모아서! 등급업 해봐! 😆", inline=False)
        embed.add_field(name="💶 등급 UP!", value="등급업을 하기 위한 일회용 아이템! - 1개당 5BP ||| 나중에 모아서! 등급업 해봐! 😆", inline=False)
        embed.add_field(name="💷 등급 UP!", value="등급업을 하기 위한 일회용 아이템! - 1개당 5BP ||| 나중에 모아서! 등급업 해봐! 😆", inline=False)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("💴")
        await msg.add_reaction("💵")   
        await msg.add_reaction("💶")
        await msg.add_reaction("💷")


@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1:  # 봇이면 패스
        return None
    if str(reaction.emoji) == "💴":
        await reaction.message.channel.send(user.name + "님이 💴 등급 UP! 아이템을 구매")
    if str(reaction.emoji) == "💵":
        await reaction.message.channel.send(user.name + "님이 💴 등급 UP! 아이템을 구매")
    if str(reaction.emoji) == "💶":
        await reaction.message.channel.send(user.name + "님이 💴 등급 UP! 아이템을 구매")
    if str(reaction.emoji) == "💷":
        await reaction.message.channel.send(user.name + "님이 💴 등급 UP! 아이템을 구매")


client.run("ODA1MDY0Mjc4NDY5MTE1OTA1.YBVciQ.knxd49yeesq6UmjSRg3yOAyKJsI")
