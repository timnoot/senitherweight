# senitherweight

[![discord](https://img.shields.io/discord/840150806682664970?logo=discord&style=for-the-badge)](https://discord.gg/ej92B474Ej)
[![license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![pypi](https://img.shields.io/pypi/v/senitherweight?style=for-the-badge)](https://pypi.org/project/senitherweight/)

Hypixel SkyBlock Weight Calculator

## Information

Written without any external libraries other than `aiohttp` which is used to fetch data from the Hypixel API.

This requires a Hypixel API key. You may obtain one by logging onto `hypixel.net` with your Minecraft client and typing
/api new.

## Credits

- [Senither](https://github.com/Senither/) - Original author of the calculator
- [timnoot](https://github.com/timnoot) - Ported the calculator to Python.

## Usage

```py
from senitherweight import SenitherWeight
import asyncio

senither = SenitherWeight("API-KEY-HERE")


async def main():
    # using a UUID
    print(await senither.get_weight("e710ff36fe334c0e8401bda9d24fa121"))

    # using a username
    print(await senither.get_weight_from_name("timnoot"))

    # functions for if you wish to see a certain profile instead of the most recently used profile
    print(await senither.get_weight_from_name("MooshiMochi", "Orange"))
    print(await senither.get_weight("0ce87d5afa5f4619ae78872d9c5e07fe", "Mango"))

    # get raw weight from raw data, read the JSDoc for more information
    # this does not return the uuid and username fields but it does not make any requests
    print(SenitherWeight.get_weight_raw(
        {
            'mining': 183102234.88907138, 'foraging': 61906511.969001345, 'enchanting': 508444404.0935615,
            'farming': 136267563.7507943, 'combat': 418778146.1766783, 'fishing': 110893816.12596695,
            'alchemy': 112877401.723031, 'taming': 488698175.13185537
        },
        {
            'healer': {'experience': 129196634.63940006},
            'mage': {'experience': 156073711.0390862},
            'berserk': {'experience': 304167530.58791596},
            'archer': {'experience': 235720208.66076514},
            'tank': {'experience': 192383702.58436698}
        },
        900529694,
        {
            'zombie': {'xp': 2115212},
            'spider': {'xp': 1913691},
            'wolf': {'xp': 1200006},
            'enderman': {'xp': 1000500},
            'blaze': {'xp': 255}
        },
    ))


asyncio.run(main())
```

Example output of one of the functions, in JSON:

```json
{
  "total": 5902.302984602829,
  "skill_weight": 3013.6795988302724,
  "dungeon_weight": 2357.485394537336,
  "slayer_weight": 531.1379912352199
}
```

[//]: # (## API)

[//]: # ()
[//]: # (If you aren't using Python or JavaScript and you need an API, take a look)

[//]: # (at [lilyweight-worker]&#40;https://lilydocs.antonio32a.com/&#41;.)
