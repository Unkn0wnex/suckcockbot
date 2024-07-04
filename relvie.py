import discord

TOKEN = "MTI1ODMxOTQ2NDE1NjQ5OTk2OQ.GGcRxu.WCCTxilQTGI-jesVfaAB-PjCG62Ny6GmM2wZM0"

img = "[...](https://otvet.imgsmail.ru/download/291681843_837cc2b425571d15e43761dc873a3ed2_800.jpg)"

bot = discord.Bot()

@bot.command(description="Сосу член") 
async def suckcock(ctx, arg): 
    await ctx.respond(f"Сосу член {arg}! {img}")

bot.run(TOKEN)