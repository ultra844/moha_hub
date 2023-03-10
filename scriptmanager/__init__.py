import json
from pathlib import Path

from .core import ScriptManager

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


def setup(bot):
    cog = ScriptManager(bot)
    bot.add_cog(cog)
