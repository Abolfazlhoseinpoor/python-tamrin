import asyncio
async def restoran (name,zaman):
    print(f"raftam restoran va sefaresh {name} ro dadam be restoran!")
    await asyncio.sleep(zaman)
    print(f"sefaresh ghazaye {name} amade shode!!")
async def main():
    await asyncio.gather(
        restoran("pizza", 5 ),
        restoran("chiken" , 3 ),
        restoran("salad" , 2)
    )
asyncio.run(main())