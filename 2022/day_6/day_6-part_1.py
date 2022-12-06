def locate_marker(packet: str) -> int:
    active = packet[0:4]
    characters_processed = 4

    valid_marker = all([active.count(x) == 1 for x in active])
    while valid_marker == False:
        characters_processed += 1
        active = packet[characters_processed-4:characters_processed]
        valid_marker = all([active.count(x) == 1 for x in active])

    return characters_processed

with open('day_6-input') as f:
    packet = f.readline().rstrip()

print(locate_marker(packet))
