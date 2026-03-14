stats = {
"signals":0,
"wins":0,
"loss":0
}

def winrate():

    if stats["signals"]==0:
        return 0

    return (stats["wins"]/stats["signals"])*100
