"""读取本地工程资料并检查交付文件之间的关联。"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
FILES = ['plays/main/road.stage', 'plays/main/trench.stage', 'plays/main/escort.stage', 'plays/revised/road.stage', 'plays/waiting/road.stage', 'plays/waiting/trench.stage', 'settings.json', 'tapes.ndjson']


def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def lines(name):
    return [json.loads(line) for line in (ROOT / name).read_text(encoding='utf-8').splitlines() if line.strip()]


def inspect():
    tape = lines('tapes.ndjson')
    assert [r['at'] for r in tape] == sorted(r['at'] for r in tape)
    give, take = tape[4:6]
    assert give['resource'] == take['resource'] == 'escort' and give['at'] == take['at']
    assert set(read('settings.json')['entry']) == {f.stem for f in (ROOT / 'plays/main').glob('*.stage')}
    assert (ROOT / 'plays/main/road.stage').read_bytes() != (ROOT / 'plays/revised/road.stage').read_bytes()
    return f'{len(tape)} 个历史动作，含同一时刻的设施归还与领取'


if __name__ == '__main__':
    print(inspect())
