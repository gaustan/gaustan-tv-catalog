import json,pathlib
p=pathlib.Path(__file__).parent
c=json.loads((p/'catalogo.json').read_text(encoding='utf-8'))
lines=['#EXTM3U']
for s in c['sources']:
    for e in s['entries']:
        if e['type']=='stream':
            name=e['name'].replace('\n',' ')
            group=e['group'].replace('"',"'").replace('\n',' ')
            lines.extend([f'#EXTINF:-1 tvg-id="{e["id"]}" group-title="{group}",{name}',e['url']])
(p/'catalogo.m3u').write_text('\n'.join(lines)+'\n',encoding='utf-8')
