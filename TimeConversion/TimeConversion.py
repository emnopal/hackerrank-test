from typing import List


def timeConversion(s: str) -> str:
    s_split: List[str] = s.split(":")

    if 'am' in s_split[-1].lower():
        s_split[-1] = s_split[-1].lower().replace("am", '')
        if '12' in s_split[0]:
            s_split[0] = '00'
    else:
        s_split[-1] = s_split[-1].lower().replace("pm", '')
        if '12' not in s_split[0]:
            s_split[0] = str(int(s_split[0].lstrip("0")) + 12)

    return ':'.join(s_split)

print(timeConversion("12:00:00am"))
print(timeConversion("07:05:45PM"))
