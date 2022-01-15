# Mark Hibbing CIS 345 Tues/Thurs 12:00 - 1:15pm Project Project Submission

import discord
from discord.ext import commands
import youtube_dl

# The string list that is required to link the GUI to this music bot. Currently not functioning
tracklist = []


class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("No users in a voice channel")

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()

        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        # track is correctly recorded as a string with the correct url
        track = url
        ctx.voice_client.stop()
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        ydl_options = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            vc.play(source)

        # The breaking point of the project. If this return statement worked as intended, the GUI could function
        return track

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Paused!')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Resumed!')


def setup(client):
    client.add_cog(music(client))

