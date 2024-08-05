import  disnake
from disnake.ext import commands
import asyncio
import random

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.slash_command()
async def ping(ctx):
    await ctx.send('Pong!')
    
@bot.slash_command()
async def information(ctx):
    await ctx.send('sorry this bot is still in development')

@bot.slash_command(description="Mute a member")
@commands.has_permissions(manage_roles=True)
async def mute(inter, member: disnake.Member, duration: int, reason: str = "нет причины"):
    role = disnake.utils.get(member.guild.roles, name="Muted")
    if not role:
        role = await member.guild.create_role(name="Muted")

        for channel in member.guild.channels:
            await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(role, reason=reason)
    await inter.response.send_message(f'{member.mention} был отправлен в  муn на {duration} Минут. Причина: {reason}')

    await asyncio.sleep(duration * 60)
    await member.remove_roles(role, reason="нет")
    await inter.followup.send(f'{member.mention} был размучен.')

@bot.slash_command()
async def rand(ctx, *arg):
    await ctx.send(random.randint(0, 100))

    
    
bot.run('MTI2OTk2MDU4Mjc3ODU4OTIyNQ.G1GSgZ.yhRB5qd3EjGFaDwyaTcw99DuWCmXJJRm1OebYc')