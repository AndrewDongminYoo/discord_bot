# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import random
import dotenv

import discord
from discord.ext import commands


dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# 점심 메뉴 30가지
lunch_menu = [
    "비빔밥", "김치찌개", "된장찌개", "칼국수", "불고기", "돈가스", "삼겹살", "순두부찌개",
    "갈비탕", "해물파전", "잡채", "김밥", "라멘", "짬뽕", "짜장면", "토마토 스파게티",
    "버거킹/맥도날드", "샐러드 (시저, 그린 등)", "피자 (미국식? 이태리식?)", "팟타이",
    "쌀국수 (태국식? 베트남식?)", "타코", "파에야", "한솥/편의점 도시락", "크로크무슈",
    "피시 앤 칩스", "샌드위치 (클럽, BLT 등)", "오믈렛", "그릭 요거트", "치킨커리"
]

# 저녁 메뉴 30가지
dinner_menu = [
    "갈비찜", "해물탕", "보쌈", "족발", "꼬리수육", "로스트 치킨", "파스타", "샤브샤브",
    "훠궈/마라탕", "일식 돈부리 (규동, 텐동 등)", "바비큐 (포크, 치킨 등)", "탄두리 치킨",
    "삼겹살", "스테이크", "막창/곱창", "뜨끈 국밥", "리조또 (버섯, 해산물 등)",
    "피시 앤 칩스", "터키시 케밥", "돌솥비빔밥", "태국식 카레 (그린, 레드 등)",
    "매운탕", "냉면", "육회", "타코야키", "스시", "꼬치", "즉석 떡볶이", "닭갈비",
    "김치볶음밥"
]

# 야식 메뉴 30가지
night_menu = [
    "치킨 (후라이드, 양념, 간장 등)", "피자 (고구마, 콤비네이션 등)",
    "라면 (김치라면, 치즈라면 등)", "만두 (군만두, 찐만두)", "순대",
    "떡볶이 (매운맛, 치즈 추가 등)", "족발", "보쌈", "파전 (해물파전, 김치파전)",
    "닭발 (매운맛, 순한맛)", "햄버거", "곱창 (소곱창, 대창, 막창)", "닭강정",
    "탕수육", "새우튀김", "치즈볼", "감자튀김", "나초", "스팸 김밥", "해물순두부",
    "버섯전골", "해물 우동", "김치전", "분식 모듬 (김밥, 떡볶이, 만두)",
    "베이컨 에그 샌드위치", "김치 볶음밥", "오징어 볶음", "밥버거", "미니 핫도그",
    "토스트 (아보카도, 햄&치즈 등)"
]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='점심추천')
async def recommend_lunch(message):
    menu = random.choice(lunch_menu)
    await message.send(f'오늘의 점심 메뉴는 {menu} 어떠세요?!')


@bot.command(name='저녁추천')
async def recommend_dinner(message):
    menu = random.choice(dinner_menu)
    await message.send(f'오늘의 저녁 메뉴는 {menu} 어떠세요?!')


@bot.command(name='야식추천')
async def recommend_night(message):
    menu = random.choice(night_menu)
    await message.send(f'오늘의 야식 메뉴는 {menu} 어떠세요?!')


try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    else:
        bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from"
              "https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
