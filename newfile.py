import discord
from discord.ext import commands

TOKEN = "MTUyMTUwOTM5MTEzODgxNjAxMA.GF-XKp.p1AIp60oPaawGJw1tf4FvEw5Le4G2W45qoG4sk"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def zinko(ctx):
    await ctx.send("Salut! Eu sunt Zinkoo 🤖")
    
@bot.command()
async def salut(ctx):
    await ctx.send(f"Salut, {ctx.author.mention}! 👋")
@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)

    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"**Ping-ul botului este:42`{ping} ms`",
        color=discord.Color.green()
    )

    embed.set_footer(text="Zinkoo Bot")
    await ctx.send(embed=embed)
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title="Informații utilizator",
        color=discord.Color.green()
    )
    embed.add_field(name="Nume", value=member.name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Cont creat", value=member.created_at.strftime("%d/%m/%Y"), inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def profile(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title=f"Profilul lui {member}",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(name="👤 Utilizator", value=member.mention, inline=False)
    embed.add_field(name="💬 Mesaje", value="0", inline=True)
    embed.add_field(name="🎤 Ore pe Voice", value="0 ore", inline=True)

    await ctx.send(embed=embed)
import random

@bot.command()
async def rank(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    level = random.randint(1, 50)
    xp = random.randint(0, 1000)
    next_xp = 1000

    bar = "🟩" * (xp // 100) + "⬜" * (10 - (xp // 100))

    embed = discord.Embed(
        title="📊 Rank Card",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(name="👤 Utilizator", value=member.mention, inline=False)
    embed.add_field(name="⭐ Nivel", value=level, inline=True)
    embed.add_field(name="✨ XP", value=f"{xp}/{next_xp}", inline=True)
    embed.add_field(name="📈 Progres", value=bar, inline=False)

    embed.set_footer(text="Zinkoo Bot")
    await ctx.send(embed=embed)
@bot.command()
async def intro(ctx, *, info=None):
    if info is None:
        await ctx.send(
            "Folosește:\n"
            "`!intro Nume | Vârstă | Descriere | Hobby | Zi de naștere | Oraș`\n\n"
        )
        return

    try:
        nume, varsta, descriere, hobby, zi_nastere, oras = [x.strip() for x in info.split("|")]

        embed = discord.Embed(
            title="👋 Introducere",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=ctx.author.display_avatar.url)

        embed.add_field(name="👤 Nume", value=nume, inline=True)
        embed.add_field(name="🎂 Vârstă", value=varsta, inline=True)
        embed.add_field(name="🏙️ Oraș", value=oras, inline=True)
        embed.add_field(name="🎮 Hobby", value=hobby, inline=False)
        embed.add_field(name="📝 Descriere", value=descriere, inline=False)
        embed.add_field(name="🎉 Zi de naștere", value=zi_nastere, inline=False)

        embed.set_footer(
            text=f"Introducere creată de {ctx.author}",
            icon_url=ctx.author.display_avatar.url
        )

        await ctx.send(embed=embed)

    except ValueError:
        await ctx.send(
            "❌ Ai introdus prea puține sau prea multe informații!\n\n"
            "Format corect:\n"
            "`!intro Nume | Vârstă | Descriere | Hobby | Zi de naștere | Oraș`"
        )
birthdays = {}

@bot.command()
async def birthday(ctx, zi=None):
    if zi is None:
        await ctx.send(
            "🎂 Folosește comanda astfel:\n"
            "`!birthday DD/MM/YYYY`\n\n"
            "Exemplu: `!birthday 15/08/2007`"
        )
        return

    birthdays[ctx.author.id] = zi

    embed = discord.Embed(
        title="🎉 Zi de naștere setată!",
        color=discord.Color.pink()
    )

    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.add_field(name="👤 Utilizator", value=ctx.author.mention, inline=False)
    embed.add_field(name="🎂 Ziua de naștere", value=zi, inline=False)

    await ctx.send(embed=embed)
@bot.command()
async def language(ctx, language=None):
    if language is None:
        embed = discord.Embed(
            title="🌐 Language",
            description="Alege o limbă:",
            color=discord.Color.blue()
        )
        embed.add_field(
            name="Opțiuni",
            value="`!language romanian`\n`!language english`",
            inline=False
        )
        await ctx.send(embed=embed)
        return

    language = language.lower()

    if language == "romanian":
        embed = discord.Embed(
            title="🇷🇴 Limba schimbată",
            description="Limba botului a fost setată pe **Română**.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    elif language == "english":
        embed = discord.Embed(
            title="🇬🇧 Language Changed",
            description="The bot language has been set to **English**.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="❌ Invalid Language",
            description="Folosește:\n`!language romanian`\n`!language english`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
@bot.command()
async def stats(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title="📊 User Stats",
        color=discord.Color.blurple()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(name="👤 Member", value=member.mention, inline=False)
    embed.add_field(name="💬 Messages (Total)", value="0", inline=True)
    embed.add_field(name="📅 Messages (Today)", value="0", inline=True)
    embed.add_field(name="🎤 Voice (Total)", value="0h 0m", inline=True)
    embed.add_field(name="🕒 Voice (Today)", value="0h 0m", inline=True)

    embed.set_footer(text="Zinkoo Bot • Stats")

    await ctx.send(embed=embed)
import random

@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice(["🪙 Cap", "🪙 Pajură"]))
import random
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1520863070472245490)

    embed = discord.Embed(
        title="🎉 Bun venit!",
        description=f"Bine ai venit pe server, {member.mention}!",
        color=discord.Color.green()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="📜 Te rugăm să:",
        value="• Citești regulile 📖\n• Distrează-te! 🎮\n• Respectă membrii ❤️",
        inline=False
    )

    embed.set_footer(text=f"Suntem acum {member.guild.member_count} membri!")

    await channel.send(embed=embed)
GOODBYE_CHANNEL_ID = 123456789012345678

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1520863149430145075)

    if channel is None:
        return

    embed = discord.Embed(
        title="👋 La revedere!",
        description=f"{member.mention} a părăsit serverul.",
        color=discord.Color.red()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="📉 Membri rămași",
        value=f"{member.guild.member_count}",
        inline=False
    )

    embed.set_footer(text="Sperăm să te întorci într-o zi! ❤️")

    await channel.send(embed=embed)
    KICK_LOG_CHANNEL_ID = 1520863243667771502  # Pune ID-ul canalului

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1520863243667771502)

    if channel is None:
        return

    async for entry in member.guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
        if entry.target.id == member.id:
            embed = discord.Embed(
                title="👢 Membru eliminat",
                color=discord.Color.orange()
            )

            embed.set_thumbnail(url=member.display_avatar.url)

            embed.add_field(
                name="👤 Membru",
                value=f"{member.mention} ({member})",
                inline=False
            )

            embed.add_field(
                name="🛡️ Moderator",
                value=entry.user.mention,
                inline=False
            )

            embed.add_field(
                name="📝 Motiv",
                value=entry.reason or "Niciun motiv specificat",
                inline=False
            )

            embed.set_footer(text="Zinkoo Bot • Kick Logs")

            await channel.send(embed=embed)
            break
LEVEL_CHANNEL_ID = 1520866961259499581

@bot.command()
async def level(ctx):
    if ctx.channel.id != LEVEL_CHANNEL_ID:
        await ctx.send("❌ Această comandă poate fi folosită doar în canalul de level.")
        return

    await ctx.send("⭐ Aici vor apărea informațiile despre nivel.")
from discord.ext import commands
bot.run(TOKEN)