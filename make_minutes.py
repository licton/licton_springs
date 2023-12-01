#!/usr/bin/env python
import calendar
import argparse

def get_minutes_contents(year: int, month: int, day: int, docs_link: str) -> str:
    minutes = ""
    minutes += f"Title: Council Meeting Minutes {calendar.month_name[month]} 2022\n"
    minutes += f"Date: {year}-{str(month).zfill(2)}-{str(day).zfill(2)} 18:30\n"
    minutes += "Category: Minutes\n"
    minutes += "\n"
    minutes += f'<embed width=100% style="height: -webkit-fill-available" src="{docs_link}"></embed>\n'
    return minutes


def write_minutes(year: int, month: int, contents: str):
    with open(f"content/{year}_{str(month).zfill(2)}_minutes.md", "w") as f:
        f.write(contents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("make minutes!")
    parser.add_argument('year', type=int)
    parser.add_argument('month', type=int, choices=range(1,13), metavar='month')
    parser.add_argument('day', type=int, choices=range(1,32), metavar='day')
    parser.add_argument('docs_link', type=str, help="link from google docs publish on web dialogue")
    args = parser.parse_args()

    docs_link = args.docs_link
    docs_link = docs_link.removeprefix('<iframe src="')
    docs_link = docs_link.removesuffix('"></iframe>')

    write_minutes(args.year, args.month, get_minutes_contents(args.year, args.month, args.day, docs_link))
