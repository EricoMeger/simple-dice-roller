import discord
from discord.ext import commands
from random import randint 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents = intents)


@bot.event
async def on_ready():
    print('logado como {0.user}'.format(bot))

@bot.command(help='rola uma quantia x de um dado de x lados, somando o modificador caso tenha. (XdY+Z)', brief='rola um dado setado pelo usuario no modelo XdY+Z', aliases=['roll', 'rolar'])
async def rolaDado(ctx, *, text: str):
    qtd, _, text = text.partition('d')  
    lados, _, mod = text.partition('+') 
    try:
       
        if qtd == '':
            qtd = 1

        qtd = int(qtd)
        lados = int(lados)
        
        if mod != '':
           mod = int(mod)

        else:
           mod = int(0)
    
    except ValueError:
        await ctx.send('utilize o padrão XdY+Z. Ex: 4d6+2')
        raise commands.BadArgument('utilize o padrão XdZ+Y. Ex: 4d6+2')
    
    rolls = [randint(1, lados) for i in range(qtd)]
    embed = discord.Embed(title=f'Rolando: {qtd}d{lados}+{mod}')
    embed.description = '\n'.join((f'#{i+1}º dado: **{dado}**' for i, dado in enumerate(rolls)))
    total = sum(rolls)
    total = total + mod
    embed.add_field(name='Soma', value=f'total = {total}')
    
    await ctx.send(embed=embed)
    

@bot.command(help='Repete o que foi dito', brief="Repete o que tu diziu", aliases=['repeat', 'repita'])
async def repete(ctx, *text):
    msg = ""

    for texto in text:
        msg = msg + " " + texto

    await ctx.send(msg)


bot.run('bot token')
