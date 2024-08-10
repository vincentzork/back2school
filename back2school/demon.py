import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("demon_stat_blocks.json")) as f:
    demon_stat_blocks = json.load(f)

demogorgon_custom_stat_block = demon_stat_blocks["Demogorgon"]
orcus_custom_stat_block = demon_stat_blocks["Orcus"]
grazzt_custom_stat_block = demon_stat_blocks["Graz'zt"]
baphomet_custom_stat_block = demon_stat_blocks["Baphomet"]
yeenoghu_custom_stat_block = demon_stat_blocks["Yeenoghu"]
zariel_custom_stat_block = demon_stat_blocks["Zariel"]
fraz_urbluu_custom_stat_block = demon_stat_blocks["Fraz-Urb'luu"]
juiblex_custom_stat_block = demon_stat_blocks["Juiblex"]
zuggtmoy_custom_stat_block = demon_stat_blocks["Zuggtmoy"]


class DemonLordStatBlock(StatBlockBase):
    pass
