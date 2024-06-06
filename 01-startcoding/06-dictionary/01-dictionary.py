play_data = {
    'result': '승리',
    'champ_name': '나르',
    'kill': 13,
    'assist': 15,
    'death': 3,
}

print('play_data: ', play_data)
print('result: ', play_data['result'])
print('champ_name: ', play_data['champ_name'])
print('kill: ', play_data['kill'])
print('assist: ', play_data['assist'])
print('death: ', play_data['death'])

print('play_data.keys(): ', play_data.keys())
print('play_data.values(): ', play_data.values())
print('play_data.items(): ', play_data.items())

print('### ', list(play_data.items())[0][0], list(play_data.items())[0][1])
