# -*- coding: utf8 -*-
import discord, time, random
import json, requests
import os

api = "?token=" + 'token'
api_leaderboard= "&token=" + 'token'

vw_ranks = ['PLAYER', 'VIP', 'PREMIUM', 'HOLY', 'IMMORTAL', 'BUILDER', 'MAPLEAD', 'YOUTUBE', 'DEV', 'ORGANIZER', 'MODER', 'WARDEN', 'CHIEF', 'ADMIN']

leaderboard_sort = ['level', 'online', 'total_coins', 'kills', 'wins', 'bedBreaked', 'total_wins', 'total_games', 'rate', 'points', 'total_blocks', 'earned_money', 'wins_as_maniac', 'tamed_sheep']
leaderboard_type = ['user', 'guild', 'ann', 'ann_monthly', 'bb', 'bb_monthly', 'bp', 'bp_monthly', 'bw', 'bw_monthly', 'cp', 'cp_monthly', 'dr', 'dr_monthly', 'duels', 'duels_monthly', 'gg', 'gg_monthly', 'hg', 'hg_monthly', 'kpvp', 'kpvp_monthly', 'mw', 'mw_monthly', 'prison', 'prison_season', 'sw', 'sw_monthly', 'arc', 'arc_monthly', 'bridge', 'jumpleague', 'murder', 'paintball', 'sheep', 'tntrun', 'tnttag', 'turfwars', 'luckywars']


guild_ranks = ['LEADER', 'OFFICER', 'MEMBER']
guild_ranks_ru = ['Лидер', 'Офицер', 'Участник']

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

color_id = ["&0", "&1", "&2", "&3", "&4", "&5", "&6", "&7", "&8", "&9", "&a", "&b", "&c", "&d", "&e", "&f"]
color = ["черный", "темно-синий", "зелёный", "бирюзовый", "бордовый", "фиолетовый", "оранжевый", "серый", "темно-серый", "синий", "салатовый", "голубой", "красный", "розовый", "желтый", "белый"]
color_hex = [0x000000, 0x0000bf, 0x00be00, 0x00bebe, 0xbe0000, 0xbe00be, 0xD9A334, 0xbebebe, 0x3f3f3f, 0x3f3ffe, 0x3ffe3f, 0x3ffefe, 0xfe3f3f, 0xfe3ffe, 0xfefe3f, 0xffffff]

all_mg = ['DR', 'BWQ', 'KPVP', 'GG']
#в планах добавить BW, BWH, SW, SWT

BW = ['Actuon_4x2', 'Adata_2x4', 'Afine_2x4', 'Alezia_2x4', 'Antropez_5x2', 'Aveport_4x4', 'Bolbody_2x4', 'Castle_1x4', 'Chess_4x4', 'Chestens_1x8', 'Climp_2x4', 'Crossroad_3x4', 'CubeX_2x4', 'Dallas_1x4', 'Desert_4x4', 'Egipt_1x4', 'Elzen_5x4', 'Erevan_3x4', 'Favol_4x4', 'Fenazid_3x4', 'Fernigad_4x2', 'Festios_3x4', 'Flamax_2x4', 'Fortis_4x2', 'Frokus_4x2', 'Geometria_2x4', 'Gossamer_2x4', 'Grand_5x2', 'GreenDay_2x4', 'GreenPark_2x4', 'Gridis_4x2', 'Hestern_4x2', 'Hordor_4x2', 'Humanoid_2x4', 'Iletz_2x4', 'Krayvillow_5x4', 'Krimentis_4x2', 'Kritaz_4x2', 'Kvint_5x4', 'Leistes_2x4', 'Liberia_3x4', 'Luveris_4x4', 'Mastebr_4x4', 'Mega_10x2', 'Melion_1x8', 'Minimass_2x8', 'Minzol_1x4', 'Mirt_2x8', 'Mozes_1x4', 'Nexium_4x4', 'Nezelit_2x4', 'Norzis_4x2', 'Ominios_1x4', 'Osmantum_4x4', 'Pacman_3x4', 'Paleantog_2x4', 'Radial_3x4', 'Reklas_4x2', 'Rius_10x2', 'Rodos_4x4', 'Shosul_4x4', 'Sitrel_2x4', 'Snake_1x4', 'SnowBad_2x4', 'Stronghold_4x4', 'Strozb_4x4', 'Tangens_4x2', 'Taxol_1x4', 'Teralist_2x4', 'Texas_1x4', 'Tradeland_2x4', 'Tronez_2x4', 'Tropicana_2x4', 'Troster_4x2', 'Vaners_5x2', 'Venecia_2x4', 'Virto_2x4', 'Yavner_1x4', 'Zimdex_3x4', 'Zimperia_4x2']
BWH = ['Actuon2.0_4x2H', 'Actuon_4x2H', 'Adata_2x4H', 'Afine_2x4H', 'Alezia_2x4H', 'Aliatra_10x2H', 'Antropez_5x2H', 'Aquarium_4x2H', 'Aveport_4x4H', 'Bolbody_2x4H', 'Castle_1x4H', 'Castle_4x2H', 'Chess_4x4H', 'Chestens_1x8H', 'Climp_2x4H', 'Crossroad_3x4H', 'CubeX_2x4H', 'Dallas_1x4H', 'Desert_4x4H', 'Egipt_1x4H', 'Elzen_5x4H', 'Erevan_3x4H', 'Favol_4x4H', 'Fenazid_3x4H', 'Fernigad_4x2H', 'Festios_3x4H', 'Flamax_2x4H', 'Fortis_4x2H', 'Frokus_4x2H', 'Geometria_2x4H', 'Gossamer_2x4H', 'Grand_5x2H', 'GreenDay_2x4H', 'GreenPark_2x4H', 'Gridis_4x2H', 'Hestern_4x2H', 'Hordor_4x2H', 'Humanoid_2x4H', 'Iletz_2x4H', 'Jungleos_4x2H', 'Krayvillow_5x4H', 'Krimentis_4x2H', 'Krintaliz_6x4H', 'Kritaz_4x2H', 'Kromed_4x2H', 'Kvint_5x4H', 'Lastword_6x4H', 'Leistes_2x4H', 'Liberia_3x4H', 'Luveris_4x4H', 'Mastebr_4x4H', 'Mega_10x2H', 'Melion_1x8H', 'Merbes_6x2H', 'Minimass_2x8H', 'Minzol_1x4H', 'Mirt_2x8H', 'Mozes_1x4H', 'Nexium_4x4H', 'Nezelit_2x4H', 'Norzis_4x2H', 'Ominios_1x4H', 'Osmantum_4x4H', 'Pacman_3x4H', 'Paleantog_2x4H', 'Pluntrum_6x2H', 'Probuzhdeniye_4x2H', 'Radial_3x4H', 'Reklas_4x2H', 'Rius_10x2H', 'Rodos_4x4H', 'Sakura_10x2H', 'Shosul_4x4H', 'Sitrel_2x4H', 'Snake_1x4H', 'SnowBad_2x4H', 'Stronghold_4x4H', 'Strozb_4x4H', 'Tangens_4x2H', 'Taxol_1x4H', 'Teralist_2x4H', 'Texas_1x4H', 'Tradeland_2x4H', 'Tronez_2x4H', 'Tropicana_2x4H', 'Troster_4x2H', 'Unona_4x2H', 'Valencia_6x2H', 'Vaners_5x2H', 'Venecia_2x4H', 'Virto_2x4H', 'Yavner_1x4H', 'Zelnes_4x2H', 'Zimdex_3x4H', 'Zimperia_4x2H']
BWQ = ['Aezakmi_3x4Q', 'Aquinzer_3x4Q', 'Arcade_4x4Q', 'Atlantis_3x4Q', 'Blice_1x4Q', 'Cerkuz_2x4Q', 'Climp_3x4Q', 'Dallas_1x4Q', 'Dzebres_4x4Q', 'Ethronus_2x4Q', 'Flamax_2x4Q', 'Gribquick_4x4Q', 'Hlenius_3x4Q', 'Icepeak_2x4Q', 'Igneoz_2x4Q', 'Izbusha_4x4Q', 'Kletra_3x4Q', 'Kuaris_4x4Q', 'Lazuli_3x4Q', 'Leonas_4x4Q', 'Magic_3x4Q', 'Medilion_4x4Q', 'Mirt_2x8Q', 'Nebius_1x4Q', 'Neireliuz_3x4Q', 'Pacman_4x4Q', 'Reds_2x4Q', 'Reneva_3x4Q', 'Smokemert_3x4Q', 'Strozb_2x4Q', 'Teapart_1x4Q', 'Toytrain_2x8Q', 'Tropicana_2x4Q', 'Valert_2x4Q', 'Whitrees_3x4Q']
BW_ru = ['Актуон', 'Адата', 'Афины', 'Алезия', 'Антропез', 'Авепорт', 'Болбоду', 'Крепость', 'Шахматы', 'Честенс', 'Климп', 'Перекресток', 'Кубы X', 'Даллас', 'Десерт', 'Египет', 'Эльзен', 'Ереван', 'Фавол', 'Феназид', 'Фернигад', 'Фэстиос', 'Фламакс', 'Фортис', 'Фрокус', 'Геометрия', 'Госсамэр', 'Гранд', 'Гриндей', 'Зеленый Сад', 'Гридис', 'Хестерн', 'Хордор', 'Гуманоид', 'Илетз', 'Крайвиллоу', 'Криментис', 'Критаз', 'Квинт', 'Лейтрес', 'Либерия', 'Луверис', 'Мастебр', 'Мега', 'Мэлион', 'Минимасс', 'Минзол', 'Мирт', 'Мозес', 'Нексиум', 'Незелит', 'Норзис', 'Оминиус', 'Османтум', 'Пакман', 'Палеантог', 'Радиал', 'Реклас', 'Риус', 'Родос', 'Шосул', 'Ситрел', 'Змейка', 'Сноубад', 'Стронгхольд', 'Строзб', 'Тангенс', 'Таксол', 'Тералист', 'Техас', 'Треадлэнд', 'Тронез', 'Тропикана', 'Тростер', 'Ванерс', 'Венеция', 'Вирто', 'Явнер', 'Зимдекс', 'Зимперия']
BWH_ru = ['Актуон 2.0', 'Актуон', 'Адата', 'Афины', 'Алезия', 'Алиатра', 'Антропез', 'Аквариум', 'Авепорт', 'Болбоду', 'Крепость', 'Замки', 'Шахматы', 'Честенс', 'Климп', 'Перекресток', 'Кубы X', 'Даллас', 'Десерт', 'Египет', 'Эльзен', 'Ереван', 'Фавол', 'Феназид', 'Фернигад', 'Фэстиос', 'Фламакс', 'Фортис', 'Фрокус', 'Геометрия', 'Госсамэр', 'Гранд', 'Гриндей', 'Зеленый Сад', 'Гридис', 'Хестерн', 'Хордор', 'Гуманоид', 'Илетз', 'Джунглиос', 'Крайвиллоу', 'Криментис', 'Кринтализ', 'Критаз', 'Кромэд', 'Квинт', 'Ластворд', 'Лейтрес', 'Либерия', 'Луверис', 'Мастебр', 'Мега', 'Мэлион', 'Мэрбес', 'Минимасс', 'Минзол', 'Мирт', 'Мозес', 'Нексиум', 'Незелит', 'Норзис', 'Оминиус', 'Османтум', 'Пакман', 'Палеантог', 'Плунтрум', 'Пробуждение', 'Радиал', 'Реклас', 'Риус', 'Родос', 'Сакура', 'Шосул', 'Ситрел', 'Змейка', 'Сноубад', 'Стронгхольд', 'Строзб', 'Тангенс', 'Таксол', 'Тералист', 'Техас', 'Треадлэнд', 'Тронез', 'Тропикана', 'Тростер', 'Юнона', 'Валенсия', 'Ванерс', 'Венеция', 'Вирто', 'Явнер', 'Зелнес', 'Зимдекс', 'Зимперия']
BWQ_ru = ['Аезакми', 'Аквинзер', 'Аркада', 'Атлантис', 'Блайс', 'Церкуз', 'Климп', 'Даллас', 'Дзебрес', 'Этронус', 'Фламакс', 'Грибквик', 'Хлениус', 'Айспик', 'Игнеоз', 'Избуша', 'Клетра', 'Куарис', 'Лазули', 'Леонас', 'Мейджик', 'Медильон', 'Мирт', 'Небиус', 'Нейрелиуз', 'Пакман', 'Редс', 'Ренева', 'Смоукмерт', 'Строзб', 'Теапарт', 'Тойтрейн', 'Тропикана', 'Валерт', 'Вайтрис']
BW_jpg = [] #soon
BWH_jpg = [] #soon
BWQ_jpg = ['https://i.imgur.com/6ojCkTr.jpg', 'https://i.imgur.com/c0PKx2w.jpg', 'https://i.imgur.com/ZmYMB6g.jpg', 'https://i.imgur.com/AhuA6WF.jpg', 'https://i.imgur.com/rOJ4DVU.jpg', 'https://i.imgur.com/0vm30La.jpg', 'https://i.imgur.com/UKgOUys.jpg', 'https://i.imgur.com/uTuTkpf.jpg', 'https://i.imgur.com/e5kop4h.jpg', 'https://i.imgur.com/ImT8IXQ.jpg', 'https://i.imgur.com/x6j0L8E.jpg', 'https://i.imgur.com/MvRL82Q.jpg', 'https://i.imgur.com/yTkyUAx.jpg', 'https://i.imgur.com/wKM7TjZ.jpg', 'https://i.imgur.com/JcwyGLV.jpg', 'https://i.imgur.com/rMugKCL.jpg', 'https://i.imgur.com/WVKC5Z5.jpg', 'https://i.imgur.com/tWCsRk8.jpg', 'https://i.imgur.com/hJx5p8p.jpg', 'https://i.imgur.com/w1GxbOr.jpg', 'https://i.imgur.com/cp2jZm5.jpg', 'https://i.imgur.com/Rf52x7F.jpg', 'https://i.imgur.com/urW6eIS.jpg', 'https://i.imgur.com/ZJSZ2gQ.jpg', 'https://i.imgur.com/FHrdEZy.jpg', 'https://i.imgur.com/yJnqe7G.jpg', 'https://i.imgur.com/wcrTyVH.jpg', 'https://i.imgur.com/UvcAfqP.jpg', 'https://i.imgur.com/UvcAfqP.jpg', 'https://i.imgur.com/7JgzXu1.jpg', 'https://i.imgur.com/FNUM5Dp.jpg', 'https://i.imgur.com/BGJelY6.jpg', 'https://i.imgur.com/PWcDHpM.jpg', 'https://i.imgur.com/5mPZk3y.jpg', 'https://i.imgur.com/R9Dh02V.jpg']

DR = ['BonBon', 'Orbis', 'Skylands', 'Mauti']
DR_ru = ['BonBon', 'Orbis', 'Skylands', 'Mauti']
DR_png = ['https://i.imgur.com/FfsbFec.png', 'https://i.imgur.com/xby18vy.png', 'https://i.imgur.com/LDf5tbf.png', 'https://i.imgur.com/g43vS0F.png']

KPVP = ['Afalia', 'Belnes', 'Finiens', 'Flossin', 'Klion', 'Micelin', 'Ronax', 'Town', 'Valley']
KPVP_ru = ['Афалия', 'Бельнес', 'Финьёнс', 'Флоссин', 'Клион', 'Мицелин', 'Ронакс', 'Город', 'Долина']
KPVP_png = ['https://i.imgur.com/YfdVlDW.png', 'https://i.imgur.com/J2vtQLH.png', 'https://i.imgur.com/xMKdwcu.png', 'https://i.imgur.com/INeK3Sl.png', 'https://i.imgur.com/hLO55I8.png', 'https://i.imgur.com/hLO55I8.png']

GG = ['Vares', 'Acteki', 'Razgez', 'Virios', 'Ruinih', 'Kriolla', 'Gorod', 'Bunker', 'Derevnja', 'Boynja']
GG_ru = ['Варьес', 'Ацтеки', 'Разгез', 'Вириос', 'Руины', 'Криолла', 'Город', 'Бункер', 'Деревня', 'Бойня']
GG_png = ['https://i.imgur.com/D9WEACG.png', 'https://i.imgur.com/4sQApmC.png', 'https://i.imgur.com/on7d8UO.png', 'https://i.imgur.com/QjyA0jq.png', 'https://i.imgur.com/nqINALn.png', 'https://i.imgur.com/hLO55I8.png']

locate_req = requests.get("https://api.vimeworld.ru/locale/ru" + api)
locate_info = json.loads(locate_req.text)


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(status= discord.Status.dnd, activity= discord.Game('VimeWorld. /help'))
        print("Запуск бота прошел успешно!")
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == ("/help"):
            emb=discord.Embed(title="Все команды бота", color=0x8080ff)
            emb.add_field(name="Всего команд (13)", value="**" + "`/help` - команды бота. \n`/aeroku` - информация о боте. \n`/support` - поддержка бота. \n`/bugreport` - если вы заметили ошибку, напишите данную команду для получения дальнейшей информации. \n`/color` - все цвета, которые использует бот, и их значения. \n`/online` - онлайн на сервере VimeWorld [MiniGames]. \n`/user [никнейм игрока]` или `/user id [id игрока]` - основную информацию об игроке. \n`/stats [никнейм игрока] [режим]` или `/stats id [id игрока] [режим] - статистика игрока по мини играм.`\n`/friends (или /f) [никнейм игрока] [страница]` или `/friends (или /f) id [id игрока] [страница]` - список друзей игрока.\n`/guild (или /g) [название гильдии]` или `/guild id [id гильдии]` - просмотр гильдий.\n`/map [режим] [название карты]` - предпросмотр карт. \n`/mods` - модераторы, которые онлайн. \n`/streams` - активные стримы на сервере VimeWorld [MiniGames].\n`/leaderboard (или /lb) [режим] [статистика] [страница]` - таблица лидеров." + "**", inline=False)
            await message.channel.send(embed=emb)

        if message.content.lower() == ("/aeroku"):
            emb=discord.Embed(title="Мой создатель FQGM#8426\nКоличество серверов, на которых я есть: " + str(len(client.guilds)) + "\nAeroku v1.2\nОфициальный Discord: https://discord.gg/#######\nСсылка на инвайт: https://discord.com/api/oauth2/authorize?client_id=698933382192562196&permissions=8&scope=bot", color=0x8080ff)
            await message.channel.send(embed=emb)


        if message.content == ("/support"):
            emb=discord.Embed(title="Если вам понравился бот и вы хотите поддержать меня, как автора, то вы можете отправить n-ную сумму вимеров на никнейм FQGM.", color=0x8080ff)
            await message.channel.send(embed=emb)


        if message.content == ("/bugreport"):
            emb=discord.Embed(title="Если вы заметили ошибку (визуальную, техническую и др.), то вы можете отправить сообщение на почту: aerokuproject@gmail.com, написать на официальном сервере по Aeroku боту (https://discord.gg/#######) или написать в телеграм @Statuxia", color=0xffff00)
            await message.channel.send(embed=emb)



        if message.content == ("/color"):
            emb=discord.Embed(title="Все цвета, которые использует бот\n\nКрасный - не в сети. \nЗеленый - в сети. \nСветло-синий - обычное сообщение бота. \nЖелтый - ошибка.\nДругие цвета - цвета тега гильдии.", color=0x8080ff)         
            #Цвета: 0xff0000 - красный; 0x00ff00 - зеленый; 0x8080ff - светло-синий; 0xffff00 - желтый.
            await message.channel.send(embed=emb)


        if message.content == ("/online"):
            req = requests.get("https://api.vimeworld.ru/online" + api)
            info = json.loads(req.text)
            emb=discord.Embed(title="Онлайн на сервере VimeWorld [MiniGames]", color=0x8080ff)
            emb.add_field(name="**Общий онлайн**", value=info["total"], inline=True)
            emb.add_field(name="**Лобби**", value=info["separated"]["lobby"], inline=True)
            emb.add_field(name="**Annihilation**", value=info["separated"]["ann"], inline=True)
            emb.add_field(name="**BuildBattle**", value=info["separated"]["bb"], inline=True)
            emb.add_field(name="**BlockParty**", value=info["separated"]["bp"], inline=True)
            emb.add_field(name="**BedWars**", value=info["separated"]["bw"], inline=True)
            emb.add_field(name="**SkyWars**", value=info["separated"]["sw"], inline=True)
            emb.add_field(name="**ClashPoint**", value=info["separated"]["cp"], inline=True)
            emb.add_field(name="**DeathRun**", value=info["separated"]["dr"], inline=True)
            emb.add_field(name="**Duels**", value=info["separated"]["duels"], inline=True)
            emb.add_field(name="**GunGame**", value=info["separated"]["gg"], inline=True)
            emb.add_field(name="**HungerGames**", value=info["separated"]["hg"], inline=True)
            emb.add_field(name="**KitPvP**", value=info["separated"]["kpvp"], inline=True)
            emb.add_field(name="**MobWars**", value=info["separated"]["mw"], inline=True)
            emb.add_field(name="**Prison**", value=info["separated"]["prison"], inline=True)
            emb.add_field(name="**The Bridge**", value=info["separated"]["bridge"], inline=True)
            emb.add_field(name="**Murder Mystery**", value=info["separated"]["murder"], inline=True)
            emb.add_field(name="**Jump League**", value=info["separated"]["jumpleague"], inline=True)
            emb.add_field(name="**Paintball**", value=info["separated"]["paintball"], inline=True)
            emb.add_field(name="**Turf Wars**", value=info["separated"]["turfwars"], inline=True)
            emb.add_field(name="**Sheep Wars**", value=info["separated"]["sheep"], inline=True)
            emb.add_field(name="**TNT Run**", value=info["separated"]["tntrun"], inline=True)
            emb.add_field(name="**TNT Tag**", value=info["separated"]["tnttag"], inline=True)
            emb.add_field(name="**Lucky Wars**", value=info["separated"]["luckywars"], inline=True)
            await message.channel.send(embed=emb)


        if message.content.startswith("/user"):
            name = "None"
            id_u = "None"
            command_user = message.content.split(" ")
            if len(command_user) == 1:
                emb=discord.Embed(title=" ", color=0x8080ff)
                emb.set_author(name="Для просмотра основной статистики игрока напишите /user (имя игрока без скобок) или /user id (id игрока без скобок).")
                await message.channel.send(embed=emb)

            else:
                if len(command_user) > 3:
                    emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                    await message.channel.send(embed=emb)

                elif len(command_user) == 3:
                    if command_user[1] != "id":
                        emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                        await message.channel.send(embed=emb)

                    if command_user[1] == "id":
                        id_url = requests.get("https://api.vimeworld.ru/user/" + command_user[2] + "/session" + api)
                        id_info = json.loads(id_url.text)
                        if "error" in id_info:
                            emb=discord.Embed(description="Ошибка. Игрока с ID `" + command_user[2] + "` нету в этой вселенной.", colour=0xffff00)
                            await message.channel.send(embed=emb)
                        else:
                            id_u = command_user[2]

                elif len(command_user) == 2 and command_user[1] == "id":
                    emb=discord.Embed(title=" ", color=0x8080ff)
                    emb.set_author(name="Для просмотра основной статистики игрока напишите /user (имя игрока без скобок) или /user id (id игрока без скобок).")
                    await message.channel.send(embed=emb)

                elif len(command_user) == 2 and command_user[1] != "id":
                    name_url =  requests.get("https://api.vimeworld.ru/user/name/" + command_user[1] + api)
                    name_info = json.loads(name_url.text)
                    if name_info == [] or "error" in name_info:
                        if len(command_user[1]) > 8:
                            emb=discord.Embed(description="Ошибка. Игрока с таким ником нету в этой вселенной.", colour=0xffff00)
                        else:
                            emb=discord.Embed(description="Ошибка. Игрока с ником `" + command_user[1] + "` нету в этой вселенной.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                    else:
                        name = command_user[1]


            if id_u != "None":
                name = id_info["user"]["username"]
                name_url = requests.get("https://api.vimeworld.ru/user/name/" + name + api)
                name_info = json.loads(name_url.text)

            if name != "None":
                for ranks in range(14):
                    if vw_ranks[ranks] == name_info[0]["rank"]:
                        break

                days = str(name_info[0]["playedSeconds"] // 86400)
                hours = str(name_info[0]["playedSeconds"] % 86400 // 3600)
                minutes = str(name_info[0]["playedSeconds"] % 86400 % 3600 // 60)
                seconds = str(name_info[0]["playedSeconds"] % 86400 % 3600 % 60)

                if name_info[0]["lastSeen"] == -1:
                    answer = "до зарождения вселенной "
                else:
                    last_seen = time.ctime(name_info[0]["lastSeen"])
                    last_seen = last_seen.split(" ")
                    if last_seen[2] == "":
                        last_seen.pop(2)
                    for i in range(12):
                        if month[i] in last_seen:
                            last_seen.pop(1)
                            last_seen.insert(1, month_num[i])
                            last_seen.pop(0)
                            break
                    if len(last_seen[0]) == 1:
                        last_seen[0] = "0" + last_seen[0]
                    if len(last_seen[1]) == 1:
                        last_seen[1] = "0" + last_seen[1]
                    date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3][2:]
                    time_ls = last_seen[2] + " (МСК)"
                    answer = date_ls + "\nв "  + time_ls

                if id_u != "None":
                    player_info = id_u
                    if id_info["online"]["value"] == False:
                        player_info = 0xff0000
                    else:
                        player_info = 0x00ff00

                else:
                    id_u = name_info[0]["id"]
                    id_url = requests.get("https://api.vimeworld.ru/user/" + str(id_u) + "/session" + api)
                    id_info = json.loads(id_url.text)
                    if id_info["online"]["value"] == False:
                        player_info = 0xff0000
                    else:
                        player_info = 0x00ff00

                player_achievements_url = requests.get("https://api.vimeworld.ru/user/" + str(id_u) + "/achievements" + api)
                player_achievements = json.loads(player_achievements_url.text)

                player_friends_url = requests.get("https://api.vimeworld.ru/user/" + str(id_u) + "/friends" + api)
                player_friends = json.loads(player_friends_url.text)

                emb=discord.Embed(total=" ", colour=player_info)
                emb.set_author(name="Профиль игрока " + name_info[0]["username"] + " (ID: " + str(id_u)    + ")")
                emb.set_thumbnail(url="http://skin.vimeworld.ru/head/" + name_info[0]["username"] + ".png")
                emb.add_field(name="Привилегия:", value=locate_info['ranks'][name_info[0]['rank'].lower()]['name'], inline=True)
                emb.add_field(name="Уровень:", value=str(name_info[0]["level"]) + " ["+ str(round(name_info[0]["levelPercentage"] * 100)) +"%]", inline=True)
                emb.add_field(name="В игре:", value=days + " дн. " + hours + " ч. \n" + minutes + " мин. " + seconds + " сек. ", inline=True)
                emb.add_field(name="Достижений:", value=str(len(player_achievements["achievements"])) + "/165", inline=True)
                emb.add_field(name="Друзей:", value=len(player_friends["friends"]), inline=True)
                emb.add_field(name="Был в сети:", value=answer, inline=True)
                if name_info[0]["guild"] != None:
                    emb.add_field(name="_ _", value="_ _", inline=False)
                    emb.add_field(name="В гильдии:", value=name_info[0]["guild"]["name"], inline=True)
                    if name_info[0]["guild"]["tag"] != None:
                        for i in range(16):
                            if color_id[i] == name_info[0]["guild"]["color"]:
                                save_color = color[i]
                                break
                        emb.add_field(name="Тег:", value=name_info[0]["guild"]["tag"] + " (" + save_color + ")", inline=True)
                    emb.add_field(name="Уровень гильдии:", value=(str(name_info[0]["guild"]["level"])) + " ["+ str(round(name_info[0]["guild"]["levelPercentage"] * 100)) +"%]", inline=True)
                    if name_info[0]["guild"]["avatar_url"] != None:
                        emb.set_image(url=name_info[0]["guild"]["avatar_url"])
                await message.channel.send(embed=emb)

        if message.content.startswith("/friends") or message.content.startswith("/f"):
            name = "None"
            f_list = 1
            friend_n = 0
            friends_check = 12
            id_u = "None"
            command_user = message.content.split(" ")
            if len(command_user) == 1:
                emb=discord.Embed(title=" ", color=0x8080ff)
                emb.set_author(name="Для просмотра списка друзей игрока напишите /friends (имя игрока без скобок) (страница) или /friends id (id игрока без скобок) (страница). \n Каждая страница содержит в себе максимум 12 друзей. Для смены страницы в конце комады напишите цифру страницы.")
                await message.channel.send(embed=emb)

            else:
                if len(command_user) > 4:
                    emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                    await message.channel.send(embed=emb)
                elif len(command_user) == 4 and command_user[1] == "id":
                    if command_user[3].isdigit() != True:
                        emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                    else:
                        f_list = int(command_user[3])
                        command_user.pop(3)
                        print(command_user)


                if len(command_user) == 3:
                    if command_user[1] != "id" and command_user[2].isdigit() != True:
                        emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                    elif command_user[1] != "id" and command_user[2].isdigit() == True:
                        f_list = int(command_user[2])
                        command_user.pop(2)


                    if len(command_user) == 3 and command_user[1] == "id":
                        id_url = requests.get("https://api.vimeworld.ru/user/" + command_user[2] + "/friends" + api)
                        id_info = json.loads(id_url.text)
                        if "error" in id_info:
                            emb=discord.Embed(description="Ошибка. Игрока с ID `" + command_user[2] + "` нету в этой вселенной. ", colour=0xffff00)
                            await message.channel.send(embed=emb)
                        else:
                            id_u = command_user[2]

                if len(command_user) == 2 and command_user[1] == "id":
                    emb=discord.Embed(title=" ", color=0x8080ff)
                    emb.set_author(name="Для просмотра списка друзей игрока напишите /friends (имя игрока без скобок) или /friends id (id игрока без скобок).")
                    await message.channel.send(embed=emb)

                elif len(command_user) == 2 and command_user[1] != "id":
                    name = command_user[1]
                    name_url =  requests.get("https://api.vimeworld.ru/user/name/" + command_user[1] + api)
                    name_info = json.loads(name_url.text)
                    if name_info == [] or name_info == "error":
                        if len(command_user[1]) > 8:
                            emb=discord.Embed(description="Ошибка. Игрока с таким ником нету в этой вселенной.", colour=0xffff00)
                        else:
                            emb=discord.Embed(description="Ошибка. Игрока с ником `" + command_user[1] + "` нету в этой вселенной.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                    else:
                        id_u = str(name_info[0]["id"])
                        id_url = requests.get("https://api.vimeworld.ru/user/" + id_u + "/friends" + api)
                        id_info = json.loads(id_url.text)


            if id_u != "None":
                if name == 'None':
                    name = id_info['user']['username']
                    name_url =  requests.get("https://api.vimeworld.ru/user/name/" + command_user[1] + api)
                    name_info = json.loads(name_url.text)

                emb=discord.Embed(title=" ", color=0x8080ff)
                emb.set_author(name="Друзья " + id_info["user"]["username"] + " (ID: " + id_u + ")", icon_url="http://skin.vimeworld.ru/head/" + id_info["user"]["username"] + ".png")
                if id_info["friends"] == []:
                        emb.add_field(name="_ _", value="У " + id_info["user"]["username"] + " нету друзей. Тут так пусто...", inline=True)
                else:
                    if len(id_info["friends"]) > 12:
                        if len(id_info["friends"]) - friends_check * f_list > 12 and f_list != 1:
                            friend_n = 12 * (f_list - 1)
                            friends_check += friend_n
                        else:
                            if len(id_info["friends"]) - friends_check * f_list < 12:
                                if friends_check * f_list - len(id_info['friends']) > 12:
                                    friend_n = len(id_info['friends']) // 12 * 12
                                    friends_check = len(id_info['friends'])
                                else:

                                    friend_n = 12 * (f_list - 1)
                                    if len(id_info['friends']) - friend_n < 12:
                                        friends_check = len(id_info['friends'])
                                    else:
                                        friends_check = friend_n + 12

                    elif len(id_info["friends"]) < 12:
                        friends_check = len(id_info["friends"])

                    for friends_n in range(friend_n, friends_check):
                        for ranks in range(14):
                            if vw_ranks[ranks] == id_info["friends"][friends_n]["rank"]:
                                break
                        if id_info["friends"][friends_n]["lastSeen"] == -1:
                            answer = "очень давно"
                        else:
                            last_seen = time.ctime(id_info["friends"][friends_n]["lastSeen"])
                            last_seen = last_seen.split(" ")
                            if last_seen[2] == "":
                                last_seen.pop(2)
                            for i in range(12):
                                if month[i] in last_seen:
                                    last_seen.pop(1)
                                    last_seen.insert(1, month_num[i])
                                    last_seen.pop(0)
                                    break
                            if len(last_seen[0]) == 1:
                                last_seen[0] = "0" + last_seen[0]
                            if len(last_seen[1]) == 1:
                                last_seen[1] = "0" + last_seen[1]
                            date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3]
                            answer = date_ls



                        if id_info["friends"][friends_n]["guild"] != None:
                            emb.add_field(name="`" + id_info["friends"][friends_n]["username"] + "`", value="Привилегия: " + locate_info['ranks'][id_info['friends'][friends_n]['rank'].lower()]['name'] + "\nУровень: " + str(id_info["friends"][friends_n]["level"]) + " ["+ str(round(id_info["friends"][friends_n]["levelPercentage"] * 100)) + "%]\nГильдия: " + id_info["friends"][friends_n]["guild"]["name"] + "\nВход: " + answer , inline=True)
                        else:
                            emb.add_field(name="`" + id_info["friends"][friends_n]["username"] + "`", value="Привилегия: " + locate_info['ranks'][id_info['friends'][friends_n]['rank'].lower()]['name'] + "\nУровень: " + str(id_info["friends"][friends_n]["level"]) + " ["+ str(round(id_info["friends"][friends_n]["levelPercentage"] * 100)) + "%]\nВход: " + answer, inline=True)
                await message.channel.send(embed=emb)

        if message.content.startswith("/guild") or message.content.startswith("/g"):
            colourr = 0xffffff
            correct_guild = False
            leader = None
            tagg = None
            m_list = 1
            member_n = 0
            member_check = 12
            command_guild = message.content.split(" ")
            if len(command_guild) == 1:
                emb=discord.Embed(title=" ", color=0x8080ff)
                emb.set_author(name="Для просмотра гильдий напишите /guild [название гильдии (пробелы заменяйте нижним подчеркиванием _)] или /guild id [id гильдии].\nКаждая страница вмещает 24 участника. Для смены страницы в конце комады напишите цифру страницы.")
                await message.channel.send(embed=emb)
            
            if len(command_guild) > 3:
                if command_guild[2] != 'id':
                    emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                    await message.channel.send(embed=emb)
                else:
                    if command_guild[3].isdigit() != True:
                        emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                    else:
                        m_list = int(command_guild[3])
                        command_guild.pop(3)

            elif len(command_guild) == 3:
                if command_guild[1] != 'id' and command_guild[2].isdigit() != True:
                    emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                    await message.channel.send(embed=emb)

                elif command_guild[1] != "id" and command_guild[2].isdigit() == True:
                    m_list = int(command_guild[2])
                    command_guild.pop(2)

                elif command_guild[1] == 'id':
                    req = requests.get("https://api.vimeworld.ru/guild/get?id=" + command_guild[2] + api)
                    info = json.loads(req.text)
                    if 'error' in info:
                        if info['error']['error_code'] == 12 or info['error']['error_code'] == 3:
                            if '_' in command_guild[1]:
                                req = requests.get("https://api.vimeworld.ru/guild/get?name=" + command_guild[1].replace('_', '%20') + api)
                                info = json.loads(req.text)
                                if 'error' in info:
                                    if info['error']['error_code'] == 12 or info['error']['error_code'] == 3:
                                        emb=discord.Embed(description="Ошибка. Некорректно введен ID гильдии.", colour=0xffff00)
                                        await message.channel.send(embed=emb)
                                else:
                                    correct_guild = True
                            else:
                                emb=discord.Embed(description="Ошибка. Некорректно введен ID гильдии.", colour=0xffff00)
                                await message.channel.send(embed=emb)
                    else:
                        correct_guild = True

            if len(command_guild) == 2:
                if command_guild[1] == 'id':
                    emb=discord.Embed(title=" ", color=0x8080ff)
                    emb.set_author(name="Для просмотра гильдий напишите /guild (название гильдии без скобок) или /guild id (id гильдии без скобок).")
                    await message.channel.send(embed=emb)
                else:
                    req = requests.get("https://api.vimeworld.ru/guild/get?name=" + command_guild[1] + api)
                    info = json.loads(req.text)
                    if 'error' in info:
                        if info['error']['error_code'] == 12 or info['error']['error_code'] == 3:
                            if '_' in command_guild[1]:
                                req = requests.get("https://api.vimeworld.ru/guild/get?name=" + command_guild[1].replace('_', '%20') + api)
                                info = json.loads(req.text)
                                if 'error' in info:
                                    if info['error']['error_code'] == 12 or info['error']['error_code'] == 3:
                                        emb=discord.Embed(description="Ошибка. Некорректно введено название гильдии.", colour=0xffff00)
                                        await message.channel.send(embed=emb)
                                else:
                                    correct_guild = True
                            else:
                                emb=discord.Embed(description="Ошибка. Некорректно введено название гильдии.", colour=0xffff00)
                                await message.channel.send(embed=emb)
                    else:
                        correct_guild = True
            

            if correct_guild == True:

                for l in range(len(info['members'])):
                    if info['members'][l]['status'] == 'LEADER':
                        leader = info['members'][l]['user']['username']

                for c in range(len(color_id)):
                    if color_id[c] == info['color']:
                        colourr = color_hex[c]

                if info['tag'] != None:
                    tagg = "< " + info['tag'] + "> "


                if info["created"] == -1:
                    answer = "до зарождения вселенной "
                else:
                    last_seen = time.ctime(info["created"])
                    last_seen = last_seen.split(" ")
                    if last_seen[2] == "":
                        last_seen.pop(2)
                    for i in range(12):
                        if month[i] in last_seen:
                            last_seen.pop(1)
                            last_seen.insert(1, month_num[i])
                            last_seen.pop(0)
                            break
                    if len(last_seen[0]) == 1:
                        last_seen[0] = "0" + last_seen[0]
                    if len(last_seen[1]) == 1:
                        last_seen[1] = "0" + last_seen[1]
                    date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3][2:]
                    time_ls = last_seen[2] + " (МСК)"
                    answer = date_ls + "\nв "  + time_ls



                emb=discord.Embed(title="Лидер: " + leader + "\nУровень гильдии:" + str(info["level"]) + " ["+ str(round(info["levelPercentage"] * 100)) +"%]\nВсего опыта: " + str(info['totalExp']) + '\nВсего коинов: ' + str(info['totalCoins']) + '\nДата создания: ' + answer, color=colourr)
                emb.set_author(name=info['name'] + ' [ID: ' + str(info['id']) + ']')
                if info['avatar_url'] != None:
                    emb.set_thumbnail(url=info['avatar_url'])



                if len(info["members"]) > 12:
                    if len(info["members"]) - member_check * m_list > 12 and m_list != 1:
                        member_n = 12 * (m_list - 1)
                        member_check += member_n
                    else:
                        if len(info["members"]) - member_check * m_list < 12:
                            if member_check * m_list - len(info["members"]) > 12:
                                member_n = len(info["members"]) // 12 * 12
                                member_check = len(info["members"])
                            else:

                                member_n = 12 * (m_list - 1)
                                if len(info["members"]) - member_n < 12:
                                    member_check = len(info["members"])
                                else:
                                    member_check = member_n + 12

                elif len(info["members"]) < 12:
                    member_check = len(info["members"])
                for member_n in range(member_n, member_check):
                    
                    if info["members"][member_n]['user']["lastSeen"] == -1:
                        answer = "очень давно"
                    else:
                        last_seen = time.ctime(info["members"][member_n]['user']["lastSeen"])
                        last_seen = last_seen.split(" ")
                        if last_seen[2] == "":
                            last_seen.pop(2)
                        for i in range(12):
                            if month[i] in last_seen:
                                last_seen.pop(1)
                                last_seen.insert(1, month_num[i])
                                last_seen.pop(0)
                                break
                        if len(last_seen[0]) == 1:
                            last_seen[0] = "0" + last_seen[0]
                        if len(last_seen[1]) == 1:
                            last_seen[1] = "0" + last_seen[1]
                        date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3][:2]
                        answer = date_ls

                    if info["members"][member_n]['joined'] == -1:
                        answer = "очень давно"
                    else:
                        joined = time.ctime(info["members"][member_n]['joined'])
                        joined = joined.split(" ")
                        if joined[2] == "":
                            joined.pop(2)
                        for i in range(12):
                            if month[i] in joined:
                                joined.pop(1)
                                joined.insert(1, month_num[i])
                                joined.pop(0)
                                break
                        if len(joined[0]) == 1:
                            joined[0] = "0" + joined[0]
                        if len(joined[1]) == 1:
                            joined[1] = "0" + joined[1]
                        joined_date_ls = joined[1] + "." + joined[0] + "." + joined[3][:2]
                        answer_joined = joined_date_ls

                    for ranks in range(14):
                        if vw_ranks[ranks] == info["members"][member_n]['user']["rank"]:
                            break
                    for guild_rank in range(3):
                        if guild_ranks[guild_rank] == info["members"][member_n]['status']:
                            break

                    emb.add_field(name="`" + info["members"][member_n]['user']["username"] + "`", value="Привилегия: " + locate_info['ranks'][info['members'][member_n]['user']['rank'].lower()]['name'] + "\nУровень: " + str(info["members"][member_n]['user']["level"]) + " ["+ str(round(info["members"][member_n]['user']["levelPercentage"] * 100)) + "%]\nБыл в сети: " + answer + "\n\nРанг: " + guild_ranks[guild_rank] + "\nКоинов: " + str(info["members"][member_n]['guildCoins']) + "\nОпыта: " + str(info["members"][member_n]['guildExp']) + "\nВступил: " + answer_joined, inline=True)
                emb.set_footer(text="Количество членов гильдии: " + str(info['perks']['MEMBERS']['level']) + '/16.\nЕжедневный лимит коинов: ' + str(info['perks']['COINS']['level']) + '/10.\nСоздание группы: ' + str(info['perks']['PARTY']['level']) + '/1.\nПриветственное сообщение: ' + str(info['perks']['MOTD']['level']) + '/1.\nДополнительный множитель коинов: ' + str(info['perks']['COINS_MULT']['level']) + '/10.\nТег гильдии: ' + str(info['perks']['TAG']['level']) + '/1.\nЦвет гильдии: ' + str(info['perks']['COLOR']['level']) + '/1.\nГильдийные воины: ' + str(info['perks']['GUILD_WAR']['level']) + '/1.')
                await message.channel.send(embed=emb)



        if message.content.startswith('/map'):
            map_error = 0
            mapp = message.content.split(" ")
            if len(mapp) == 1:
                emb=discord.Embed(title="Для просмотра списка карт напишите /map [режим].\nДля просмотра карт напишите /map [режим] [название карт]\nПоддерживаемые режимы: BWQ, DR, KPVP, GG", color=0x8080ff)
                await message.channel.send(embed=emb)

            if len(mapp) == 2:
                if mapp[1].upper() in all_mg:
                    if mapp[1].upper() == 'BWQ':
                        emb=discord.Embed(title="Режим: " + mapp[1].upper() + '.\nПример: /map ' + ' BWQ Аезакми', color=0x8080ff)
                        emb.set_image(url='https://i.imgur.com/xCs1piT.png')
                        await message.channel.send(embed=emb)
                    elif mapp[1].upper() == 'DR':
                        emb=discord.Embed(title="Режим: " + mapp[1].upper() + '.\nПример: /map ' + ' DR Mauti', color=0x8080ff)
                        emb.set_image(url='https://i.imgur.com/K6sYaye.png')
                        await message.channel.send(embed=emb)
                    elif mapp[1].upper() == 'KPVP':
                        emb=discord.Embed(title="Режим: " + mapp[1].upper() + '.\nПример: /map ' + ' KPVP Афалия', color=0x8080ff)
                        emb.set_image(url='https://i.imgur.com/4XgrQC8.png')
                        await message.channel.send(embed=emb)
                    elif mapp[1].upper() == 'GG':
                        emb=discord.Embed(title="Режим: " + mapp[1].upper() + '.\nПример: /map ' + ' GG Варьес', color=0x8080ff)
                        emb.set_image(url='https://i.imgur.com/NV42QuG.png')
                        await message.channel.send(embed=emb)

            if len(mapp) == 3:
                if mapp[1].upper() == 'BWQ':
                    for i in range(len(BWQ_ru)):
                        if mapp[2].lower() == BWQ_ru[i].lower():
                            req = requests.get("https://api.vimeworld.ru/misc/maps" + api)
                            info = json.loads(req.text)
                            emb=discord.Embed(title="Карта: " + BWQ_ru[i] + '.\nФормат: ' + str(info['BWQ'][BWQ[i]]['playersInTeam']) + 'x' + str(info['BWQ'][BWQ[i]]['teams']), color=0x8080ff)
                            emb.set_image(url=BWQ_jpg[i])
                            await message.channel.send(embed=emb)
                        else:
                            map_error += 1
                    if map_error == len(BWQ_ru):
                        emb=discord.Embed(title="Ошибка. Такой карты нету.", color=0xffff00)
                        await message.channel.send(embed=emb)

                if mapp[1].upper() == 'DR':
                    for i in range(len(DR_png)):
                        if mapp[2].lower() == DR_ru[i].lower():
                            req = requests.get("https://api.vimeworld.ru/misc/maps" + api)
                            info = json.loads(req.text)
                            emb=discord.Embed(title="Карта: " + DR_ru[i] + '.\nФормат: ' + str(info['DR'][DR[i]]['playersInTeam']) + ' игроков.', color=0x8080ff)
                            emb.set_image(url=DR_png[i])
                            await message.channel.send(embed=emb)
                        else:
                            map_error += 1
                    if map_error == len(DR_ru):
                        emb=discord.Embed(title="Ошибка. Такой карты нету.", color=0xffff00)
                        await message.channel.send(embed=emb)

                if mapp[1].upper() == 'KPVP':
                    for i in range(len(KPVP)):
                        if mapp[2].lower() == KPVP_ru[i].lower():
                            req = requests.get("https://api.vimeworld.ru/misc/maps" + api)
                            info = json.loads(req.text)
                            if i < 4:
                                emb=discord.Embed(title="Карта: " + KPVP_ru[i] + '.\nФормат: ' + str(info['KPVP'][KPVP[i]]['playersInTeam']) + ' игроков.', color=0x8080ff)
                                emb.set_image(url=KPVP_png[i])
                            else:
                                emb=discord.Embed(title="Карта: " + KPVP_ru[i] + '.\nФормат: ' + str(info['KPVP'][KPVP[i]]['playersInTeam']) + ' игроков. \nНедоступна.', color=0x8080ff)
                                emb.set_image(url=KPVP_png[4])
                            await message.channel.send(embed=emb)
                        else:
                            map_error += 1
                    if map_error == len(KPVP_ru):
                        emb=discord.Embed(title="Ошибка. Такой карты нету.", color=0xffff00)
                        await message.channel.send(embed=emb)
                if mapp[1].upper() == 'GG':
                    for i in range(len(GG)):
                        if mapp[2].lower() == GG_ru[i].lower():
                            req = requests.get("https://api.vimeworld.ru/misc/maps" + api)
                            info = json.loads(req.text)
                            if i < 5:
                                emb=discord.Embed(title="Карта: " + GG_ru[i] + '.\nФормат: ' + str(info['GG'][GG[i]]['playersInTeam']) + ' игроков.', color=0x8080ff)
                                emb.set_image(url=GG_png[i])
                            else:
                                emb=discord.Embed(title="Карта: " + GG_ru[i] + '.\nФормат: ' + str(info['GG'][GG[i]]['playersInTeam']) + ' игроков. \nНедоступна.', color=0x8080ff)
                                emb.set_image(url=GG_png[5])
                            await message.channel.send(embed=emb)
                        else:
                            map_error += 1
                    if map_error == len(GG_ru):
                        emb=discord.Embed(title="Ошибка. Такой карты нету.", color=0xffff00)
                        await message.channel.send(embed=emb)

        if message.content == ("/mods") or message.content == ("/staff"):
            other_mods = []
            all_mods = []
            other_mods_footer = ''
            req = requests.get("https://api.vimeworld.ru/online/staff" + api)
            info = json.loads(req.text)
            if info == []:
                emb=discord.Embed(description="Все модараторы оффлайн.", colour=0xff0000)
                emb.set_author(name="Модераторы оффлайн", icon_url="https://vimetop.ru/assets/img/vimeworld.fix.jpg")
                await message.channel.send(embed=emb)
            else:
                emb=discord.Embed(description="Не рекомендуется писать модераторам, которые в игре. ", color=0x00ff00)
                emb.set_author(name="Модераторы онлайн", icon_url="https://vimetop.ru/assets/img/vimeworld.fix.jpg")

                if len(info) > 25:
                    for m in range(25, len(info)):
                        other_mods.append(info[m]['username'])
                        other_mods_footer = other_mods_footer + other_mods[m] + ', '
                for i in range(len(info)):
                    if i >= 25:
                        emb.set_footer(text="Остальные модераторы: " + other_mods_footer[:-2])
                        break
                    else:
                        emb.add_field(name='`' + info[i]["username"] + '`', value=info[i]["online"]["message"], inline=True)

                await message.channel.send(embed=emb)


        if message.content == ("/streams"):
            req = requests.get("https://api.vimeworld.ru/online/streams" + api)
            info = json.loads(req.text)
            if info == []:
                emb=discord.Embed(title="Сейчас активных стримов нету.", colour=0xff0000)
                emb.set_author(name="Активные стримы", icon_url="https://www.pngjoy.com/pngl/85/1808772_youtube-live-gloucester-road-tube-station-png-download.png")
                await message.channel.send(embed=emb)
            else:
                emb=discord.Embed(description=" ", colour=0x00ff00)
                emb.set_author(name="Активные прямые трансляции", icon_url="https://www.pngjoy.com/pngl/85/1808772_youtube-live-gloucester-road-tube-station-png-download.png")
                for i in range(len(info)):
                    hours = str(info[i]["duration"] % 86400 // 3600)
                    minutes = str(info[i]["duration"] % 86400 % 3600 // 60)
                    emb.add_field(name="Название: " + info[i]["title"] + "\nСсылка:" + info[i]["url"] + " [" + info[i]["platform"] + "]" + "\nЗрителей: " + str(info[i]["viewers"]) + "\nДлительность: " + str(hours + ":" + minutes + "ч."), value="Стример: " + info[i]["owner"], inline=True)
                await message.channel.send(embed=emb)

        
        if message.content.startswith("/stats"):
            stats = message.content.split(" ")
            id_stats = None
            if len(stats) == 1:
                emb=discord.Embed(description="`/stats [никнейм игрока] [режим]` или `/stats id [id игрока] [режим]` - статистика игрока по мини играм.\n**Доступные режимы: ann - Annihilationm bb - BuildBattle, bp - BlockParty, bw - BedWars, cp - ClashPoint, dr - DeathRun, duels - Duels, gg - GunGame, hg - HungerGames, kpvp - KitPVP, mw - MobWars, prison - Prison, sw - SkyWars, arc - Arcade, bridge - The Bridge, jumpleague - JumpLeague, murder - Murder Mystery, paintball - Paintball, sheep - Sheep Wars, turfwars - Turf Wars, tnttag - TNT Tag, tntrun - TNT Run, luckywars - Lucky Wars**", colour=0xffff00)
                await message.channel.send(embed=emb)
            elif len(stats) == 2:
                emb=discord.Embed(description="`/stats [никнейм игрока] [режим]` или `/stats id [id игрока] [режим]` - статистика игрока по мини играм.\n**Доступные режимы: ann - Annihilationm bb - BuildBattle, bp - BlockParty, bw - BedWars, cp - ClashPoint, dr - DeathRun, duels - Duels, gg - GunGame, hg - HungerGames, kpvp - KitPVP, mw - MobWars, prison - Prison, sw - SkyWars, arc - Arcade, bridge - The Bridge, jumpleague - JumpLeague, murder - Murder Mystery, paintball - Paintball, sheep - Sheep Wars, turfwars - Turf Wars, tnttag - TNT Tag, tntrun - TNT Run, luckywars - Lucky Wars**", colour=0xffff00)
                await message.channel.send(embed=emb)
            elif len(stats) == 3 and stats[1] == 'id':
                emb=discord.Embed(description="`/stats [никнейм игрока] [режим]` или `/stats id [id игрока] [режим]` - статистика игрока по мини играм.\n**Доступные режимы: ann - Annihilationm bb - BuildBattle, bp - BlockParty, bw - BedWars, cp - ClashPoint, dr - DeathRun, duels - Duels, gg - GunGame, hg - HungerGames, kpvp - KitPVP, mw - MobWars, prison - Prison, sw - SkyWars, arc - Arcade, bridge - The Bridge, jumpleague - JumpLeague, murder - Murder Mystery, paintball - Paintball, sheep - Sheep Wars, turfwars - Turf Wars, tnttag - TNT Tag, tntrun - TNT Run, luckywars - Lucky Wars**", colour=0xffff00)
                await message.channel.send(embed=emb)
            elif len(stats) == 3  and stats[1] != 'id':
                req = requests.get("https://api.vimeworld.ru/user/name/" + stats[2] + api)
                info = json.loads(req.text)
                if 'error' not in info:
                    id_stats = info[0]['id']
            elif len(stats) == 4 and stats[1] == 'id':
                req = requests.get("https://api.vimeworld.ru/user/" + stats[2] + api)
                info = json.loads(req.text)
                if 'error' not in info:
                    id_stats = info[0]['id']
            else:
                emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                await message.channel.send(embed=emb)

            if id_stats != None:
                stats_req = requests.get("https://api.vimeworld.ru/user/" + str(id_stats) +"/stats?games=" + stats[-1] + api)
                stats_info = json.loads(stats_req.text)
                if 'error' in stats_info:
                    emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                    await message.channel.send(embed=emb)
                else:
                    emb=discord.Embed(total=" ", colour=0x8080ff)
                    
                    if stats[-1].upper() == 'ANN':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Annihilationm", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['ANN']['global']['kills']) + '\nУбийств из лука: ' + str(stats_info['stats']['ANN']['global']['bowkills']) + '\nСрублено дерева: ' + str(stats_info['stats']['ANN']['global']['wood']) + '\nДобыто руды: ' + str(stats_info['stats']['ANN']['global']['ores']) + '\nУдаров по базе: ' + str(stats_info['stats']['ANN']['global']['nexus']) + '\nВскопано земли: ' + str(stats_info['stats']['ANN']['global']['digged']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['ANN']['season']['monthly']['kills']) + '\nУбийств из лука: ' + str(stats_info['stats']['ANN']['season']['monthly']['bowkills']) + '\nСрублено дерева: ' + str(stats_info['stats']['ANN']['season']['monthly']['wood']) + '\nДобыто руды: ' + str(stats_info['stats']['ANN']['season']['monthly']['ores']) + '\nУдаров по базе: ' + str(stats_info['stats']['ANN']['season']['monthly']['nexus']) + '\nВскопано земли: ' + str(stats_info['stats']['ANN']['season']['monthly']['digged']), inline=True)

                    if stats[-1].upper() == 'BB':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме BuildBattle", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['BB']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['BB']['global']['wins']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Игр: ' + str(stats_info['stats']['BB']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['BB']['season']['monthly']['wins']), inline=True)

                    if stats[-1].upper() == 'BP':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме BlockParty", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['BP']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['BP']['global']['wins']) + '\nПройдено уровней: ' + str(stats_info['stats']['BP']['global']['wins']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Игр: ' + str(stats_info['stats']['BP']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['BP']['season']['monthly']['wins']) + '\nПройдено уровней: ' + str(stats_info['stats']['BP']['season']['monthly']['wins']), inline=True)

                    if stats[-1].upper() == 'BW':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме BedWars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['BW']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['BW']['global']['deaths']) + '\nИгр: ' + str(stats_info['stats']['BW']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['BW']['global']['wins']) + '\nКроватей сломано: ' + str(stats_info['stats']['BW']['global']['bedBreaked']) , inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['BW']['season']['monthly']['kills']) + '\nСмертей: ' + str(stats_info['stats']['BW']['season']['monthly']['deaths']) + '\nИгр: ' + str(stats_info['stats']['BW']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['BW']['season']['monthly']['wins']) + '\nКроватей сломано: ' + str(stats_info['stats']['BW']['season']['monthly']['bedBreaked']) , inline=True)

                    if stats[-1].upper() == 'CP':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме ClashPoint", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['CP']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['CP']['global']['deaths']) + '\nИгр: ' + str(stats_info['stats']['CP']['global']['games']) + '\nТочек рес. сломано: ' + str(stats_info['stats']['CP']['global']['resourcePointsBreaked']) , inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['CP']['season']['monthly']['kills']) + '\nСмертей: ' + str(stats_info['stats']['CP']['season']['monthly']['deaths']) + '\nИгр: ' + str(stats_info['stats']['CP']['season']['monthly']['games']) + '\nТочек рес. сломано: ' + str(stats_info['stats']['CP']['season']['monthly']['resourcePointsBreaked']) , inline=True)

                    if stats[-1].upper() == 'DR':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме DeathRun", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['DR']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['DR']['global']['wins']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Игр: ' + str(stats_info['stats']['DR']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['DR']['season']['monthly']['wins']), inline=True)

                    if stats[-1].upper() == 'DUELS':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Duels", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Одиночных побед: ' + str(stats_info['stats']['DUELS']['global']['solo_wins']) + '\nОдиночных игр: ' + str(stats_info['stats']['DUELS']['global']['solo_games']) + '\nКомандных побед: ' + str(stats_info['stats']['DUELS']['global']['team_wins']) + '\nКомандных игр: ' + str(stats_info['stats']['DUELS']['global']['team_games']) + '\nРейтинговых игр: ' + str(stats_info['stats']['DUELS']['global']['ranked_games']) + '\nРейтинговых побед: ' + str(stats_info['stats']['DUELS']['global']['ranked_wins']) + '\nВсего побед: ' + str(stats_info['stats']['DUELS']['global']['total_wins']) + '\nВсего игр: ' + str(stats_info['stats']['DUELS']['global']['total_games']) + '\nПобед Classic: ' + str(stats_info['stats']['DUELS']['global']['wins_classic']) + '\nПобед на луках: ' + str(stats_info['stats']['DUELS']['global']['wins_bow']) + '\nПобед OP: ' + str(stats_info['stats']['DUELS']['global']['wins_op']) + '\nПобед на зельях: ' + str(stats_info['stats']['DUELS']['global']['wins_potion']) + '\nПобед UHC: ' + str(stats_info['stats']['DUELS']['global']['wins_uhc']) + '\nПобед BWH: ' + str(stats_info['stats']['DUELS']['global']['wins_bwh']) + '\nМакс. побед подряд: ' + str(stats_info['stats']['DUELS']['global']['maxstrike']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Одиночных побед: ' + str(stats_info['stats']['DUELS']['season']['monthly']['solo_wins']) + '\nОдиночных игр: ' + str(stats_info['stats']['DUELS']['season']['monthly']['solo_games']) + '\nКомандных побед: ' + str(stats_info['stats']['DUELS']['season']['monthly']['team_wins']) + '\nКомандных игр: ' + str(stats_info['stats']['DUELS']['season']['monthly']['team_games']) + '\nРейтинговых игр: ' + str(stats_info['stats']['DUELS']['season']['monthly']['ranked_games']) + '\nРейтинговых побед: ' + str(stats_info['stats']['DUELS']['season']['monthly']['ranked_wins']) + '\nВсего побед: ' + str(stats_info['stats']['DUELS']['season']['monthly']['total_wins']) + '\nВсего игр: ' + str(stats_info['stats']['DUELS']['season']['monthly']['total_games']) + '\nПобед Classic: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_classic']) + '\nПобед на луках: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_bow']) + '\nПобед OP: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_op']) + '\nПобед на зельях: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_potion']) + '\nПобед UHC: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_uhc']) + '\nПобед BWH: ' + str(stats_info['stats']['DUELS']['season']['monthly']['wins_bwh']) + '\nРейтинг: ' + str(stats_info['stats']['DUELS']['season']['monthly']['rate']) + '\nМакс. рейтинг: ' + str(stats_info['stats']['DUELS']['season']['monthly']['max_rate']), inline=True)

                    if stats[-1].upper() == 'GG':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме GunGame", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['GG']['global']['kills']) + '\nПобед: ' + str(stats_info['stats']['GG']['global']['wins']) + '\nИгр: ' + str(stats_info['stats']['GG']['global']['games']) + '\nНабрано уровней: ' + str(stats_info['stats']['GG']['season']['monthly']['levels']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['GG']['season']['monthly']['kills']) + '\nПобед: ' + str(stats_info['stats']['GG']['season']['monthly']['wins']) + '\nИгр: ' + str(stats_info['stats']['GG']['season']['monthly']['games']) + '\nНабрано уровней: ' + str(stats_info['stats']['GG']['season']['monthly']['levels']), inline=True)

                    if stats[-1].upper() == 'HG':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме HungerGames", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['HG']['global']['kills']) + '\nПобед: ' + str(stats_info['stats']['HG']['global']['wins']) + '\nИгр: ' + str(stats_info['stats']['HG']['global']['games']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['HG']['season']['monthly']['kills']) + '\nПобед: ' + str(stats_info['stats']['HG']['season']['monthly']['wins']) + '\nИгр: ' + str(stats_info['stats']['HG']['season']['monthly']['games']), inline=True)

                    if stats[-1].upper() == 'KPVP':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме KitPVP", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Убийств: ' + str(stats_info['stats']['KPVP']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['KPVP']['global']['deaths']) + '\nОчков: ' + str(stats_info['stats']['KPVP']['global']['points']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Убийств: ' + str(stats_info['stats']['KPVP']['season']['monthly']['kills']) + '\nСмертей: ' + str(stats_info['stats']['KPVP']['season']['monthly']['deaths']), inline=True)

                    if stats[-1].upper() == 'MW':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме MobWars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['MW']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['MW']['global']['wins']) + '\nУбито мобов: ' + str(stats_info['stats']['MW']['global']['mobsKilled']) + '\nПослано  мобов: ' + str(stats_info['stats']['MW']['global']['mobsSended']) + '\nМакс. доход: ' + str(stats_info['stats']['MW']['global']['maxIncome']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Игр: ' + str(stats_info['stats']['MW']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['MW']['season']['monthly']['wins']) + '\nУбито мобов: ' + str(stats_info['stats']['MW']['season']['monthly']['mobsKilled']) + '\nПослано  мобов: ' + str(stats_info['stats']['MW']['global']['mobsSended']), inline=True)

                    if stats[-1].upper() == 'PRISON':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Prison", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Всего блоков: ' + str(stats_info['stats']['PRISON']['global']['total_blocks']) + '\nПолучено денег: ' + str(stats_info['stats']['PRISON']['global']['earned_money']) + '\nУбийств: ' + str(stats_info['stats']['PRISON']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['PRISON']['global']['deaths']) + '\nУбито мобов: ' + str(stats_info['stats']['PRISON']['global']['mobs']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Всего блоков: ' + str(stats_info['stats']['PRISON']['season']['manual']['total_blocks']) + '\nПолучено денег: ' + str(stats_info['stats']['PRISON']['season']['manual']['earned_money']) + '\nУбийств: ' + str(stats_info['stats']['PRISON']['season']['manual']['kills']) + '\nСмертей: ' + str(stats_info['stats']['PRISON']['global']['deaths']) + '\nУбито мобов: ' + str(stats_info['stats']['PRISON']['global']['mobs']), inline=True)

                    if stats[-1].upper() == 'SW':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме SkyWars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Побед: ' + str(stats_info['stats']['SW']['global']['wins']) + '\nИгр: ' + str(stats_info['stats']['SW']['global']['games']) + '\nУбийств: ' + str(stats_info['stats']['SW']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['SW']['global']['deaths']) + '\nСтрел выпущено: ' + str(stats_info['stats']['SW']['global']['arrowsFired']) + '\nБлоков сломано: ' + str(stats_info['stats']['SW']['global']['blocksBroken']) + '\nБлоков поставлено: ' + str(stats_info['stats']['SW']['global']['blocksPlaced']) + '\nСерия побед: ' + str(stats_info['stats']['SW']['global']['currentWinStreak']) + '\nПобед подряд: ' + str(stats_info['stats']['SW']['global']['winStreak']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Побед: ' + str(stats_info['stats']['SW']['season']['monthly']['wins']) + '\nИгр: ' + str(stats_info['stats']['SW']['season']['monthly']['games']) + '\nУбийств: ' + str(stats_info['stats']['SW']['season']['monthly']['kills']) + '\nСмертей: ' + str(stats_info['stats']['SW']['global']['deaths']) + '\nСтрел выпущено: ' + str(stats_info['stats']['SW']['global']['arrowsFired']) + '\nБлоков сломано: ' + str(stats_info['stats']['SW']['global']['blocksBroken']) + '\nБлоков поставлено: ' + str(stats_info['stats']['SW']['global']['blocksPlaced']), inline=True)

                    if stats[-1].upper() == 'ARC':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режимах Arcade", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['ARC']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['ARC']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['ARC']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['ARC']['global']['deaths']), inline=True)
                        emb.add_field(name="`Сезонная статистика`", value='Игр: ' + str(stats_info['stats']['ARC']['season']['monthly']['games']) + '\nПобед: ' + str(stats_info['stats']['ARC']['season']['monthly']['wins']) + '\nУбийств: ' + str(stats_info['stats']['ARC']['season']['monthly']['kills']) + '\nСмертей: ' + str(stats_info['stats']['ARC']['global']['deaths']), inline=True)

                    if stats[-1].upper() == 'BRIDGE':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме The Bridge", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['BRIDGE']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['BRIDGE']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['BRIDGE']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['BRIDGE']['global']['deaths']) + '\nОчков: ' + str(stats_info['stats']['BRIDGE']['global']['points']), inline=True)

                    if stats[-1].upper() == 'JUMPLEAGUE':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме JumpLeague", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['JUMPLEAGUE']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['JUMPLEAGUE']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['JUMPLEAGUE']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['JUMPLEAGUE']['global']['deaths']) + '\nЧекпоинтов: ' + str(stats_info['stats']['JUMPLEAGUE']['global']['checkpoints']), inline=True)

                    if stats[-1].upper() == 'MURDER':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Murder Mystery", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['MURDER']['global']['games']) + '\nВсего побед: ' + str(stats_info['stats']['MURDER']['global']['total_wins']) + '\nПобед мирным: ' + str(stats_info['stats']['MURDER']['global']['wins_as_innocent']) + '\nПобед маньяком: ' + str(stats_info['stats']['MURDER']['global']['wins_as_maniac']) + '\nПобед детективом: ' + str(stats_info['stats']['MURDER']['global']['wins_as_detective']) + '\nУбийств: ' + str(stats_info['stats']['MURDER']['global']['kills']), inline=True)

                    if stats[-1].upper() == 'PAINTBALL':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Paintball", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['PAINTBALL']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['PAINTBALL']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['PAINTBALL']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['PAINTBALL']['global']['deaths']), inline=True)

                    if stats[-1].upper() == 'SHEEP':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Sheep Wars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['SHEEP']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['SHEEP']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['SHEEP']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['SHEEP']['global']['deaths']), inline=True)

                    if stats[-1].upper() == 'TURFWARS':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Turf Wars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['TURFWARS']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['TURFWARS']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['TURFWARS']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['TURFWARS']['global']['deaths']), inline=True)

                    if stats[-1].upper() == 'TNTTAG':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме TNT Tag", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['TNTTAG']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['TNTTAG']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['TNTTAG']['global']['kills']), inline=True)

                    if stats[-1].upper() == 'TNTRUN':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме TNT Run", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['TNTRUN']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['TNTRUN']['global']['wins']) + '\nБлоков сломано: ' + str(stats_info['stats']['TNTRUN']['global']['broken_blocks']), inline=True)

                    if stats[-1].upper() == 'LUCKYWARS':
                        emb.set_author(name="Статистика игрока " + stats_info['user']['username'] + " (ID: " + str(id_stats) + ") в режиме Lucky Wars", icon_url="http://skin.vimeworld.ru/head/" + stats_info["user"]["username"] + ".png")
                        emb.add_field(name="`Основная статистика`", value='Игр: ' + str(stats_info['stats']['LUCKYWARS']['global']['games']) + '\nПобед: ' + str(stats_info['stats']['LUCKYWARS']['global']['wins']) + '\nУбийств: ' + str(stats_info['stats']['LUCKYWARS']['global']['kills']) + '\nСмертей: ' + str(stats_info['stats']['LUCKYWARS']['global']['deaths']) + '\nСломано лаки блоков: ' + str(stats_info['stats']['LUCKYWARS']['global']['lucky_blocks']), inline=True)

                    await message.channel.send(embed=emb)



        if message.content.startswith("/leaderboard") or message.content.startswith("/lb"):
            leaderboard_have_list = True
            lb_list = 0
            if len(leaderboard) == 1:
                leaderboard = message.content.split(" ")
                req = requests.get("https://api.vimeworld.ru/leaderboard/list" + api)
                info = json.loads(req.text)
                emb=discord.Embed(title="Информация в скобках написана только для какого-то режима.", color=0x8080ff)
                emb.set_author(name="Список доступных команд для просмотра таблицы лидеров, а также информация, которую нужно вывести из таблицы. \nДля просмотра топа нужно написать /leaderboard [тип] [варианты]")
                emb.add_field(name="`level`, `online`", value="user", inline=True)
                emb.add_field(name="`level`, `total_coins`", value="guild", inline=True)
                emb.add_field(name="`kills`", value="ann и ann_monthly", inline=True)
                emb.add_field(name="`wins`", value="bb и bb_monthly", inline=True)
                emb.add_field(name="`wins`", value="bp и bp_monthly", inline=True)
                emb.add_field(name=" `wins`, `kills`, `bedBreaked (bw only)`", value="bw и bw_monthly", inline=True)
                emb.add_field(name="`wins`, `kills`", value="cp и cp_monthly", inline=True)
                emb.add_field(name="`wins`", value="dr и dr_monthly", inline=True)
                emb.add_field(name="`total_wins`, `total_games (duels)`, `rate (duels_monthly)`", value="duels и duels_monthly", inline=True)
                emb.add_field(name="`wins`, `kills`", value="gg и gg_monthly", inline=True)
                emb.add_field(name="`wins`", value="hg и hg_monthly", inline=True)
                emb.add_field(name="`points (kpvp)`, `kills`", value="kpvp и kpvp_monthly", inline=True)
                emb.add_field(name="`wins`", value="mw и mw_monthly", inline=True)
                emb.add_field(name="`total_blocks`, `kills`, `earned_money (prison_season)`", value="prison и prison_season", inline=True)
                emb.add_field(name="`wins`, `kills`", value="sw и sw_monthly", inline=True)
                emb.add_field(name="`wins`", value="arc и arc_monthly", inline=True)
                emb.add_field(name="`wins`, `kills`, `points`", value="bridge", inline=True)
                emb.add_field(name="`wins`, `kills`", value="jumpleague", inline=True)
                emb.add_field(name="`wins_as_maniac`, `total_wins`, `kills`", value="murder", inline=True)
                emb.add_field(name="`wins`, `kills`", value="paintball", inline=True)
                emb.add_field(name="`wins`, `kills`, `tamed_sheep`", value="sheep", inline=True)
                emb.add_field(name="`wins`", value="tntrun", inline=True)
                emb.add_field(name="`wins`, `kills`", value="tnttag", inline=True)
                emb.add_field(name="`wins`, `kills`", value="turfwars", inline=True)
                emb.add_field(name="`wins`, `kills`", value="luckywars", inline=True)
                await message.channel.send(embed=emb)

            else:
                if len(leaderboard) != 3:
                    if len(leaderboard) > 3 and leaderboard[3].isdigit() == True:
                        lb_list = int(leaderboard[3])
                        leaderboard.pop(3)
                        leaderboard_have_list = True
                    else:
                        emb=discord.Embed(description="Ошибка. Неправильная команда.", colour=0xffff00)
                        await message.channel.send(embed=emb)
                        leaderboard_have_list = False
                if leaderboard_have_list == True:
                    for l_type in range(len(leaderboard_type)):
                        if leaderboard_type[l_type] == leaderboard[1]:
                            for l_sort in range(len(leaderboard_sort)):
                                if leaderboard_sort[l_sort] == leaderboard[2]:
                                    if lb_list > 1:
                                        lb_list = str(lb_list * 15)
                                        req = requests.get("https://api.vimeworld.ru/leaderboard/get/" + leaderboard[1] + "/" + leaderboard[2] + "?size=15&offset=" + lb_list + '&' + api_leaderboard)
                                    else:
                                        req = requests.get("https://api.vimeworld.ru/leaderboard/get/" + leaderboard[1] + "/" + leaderboard[2] + "?size=15&offset=0" + '&' + api_leaderboard)
                                    info = json.loads(req.text)
                                    namereq = requests.get("https://api.vimeworld.ru/leaderboard/list" + api)
                                    nameinfo = json.loads(namereq.text)
                                    if 'error' in info:
                                        emb=discord.Embed(title=" ", color=0xffff00)
                                        emb.set_author(name="Ошибка. Неправильная команда.")
                                    else:
                                        emb=discord.Embed(title=" ", color=0x8080ff) 
                                        emb.set_author(name=nameinfo[l_type]['description'] + ' [' + leaderboard[2] +']')


                                        if leaderboard[1] == 'user':
                                            if leaderboard[2] == 'level':
                                                for leaderboardz in range(15):
                                                    days = str(info['records'][leaderboardz]['playedSeconds'] // 86400)
                                                    hours = str(info['records'][leaderboardz]['playedSeconds'] % 86400 // 3600)
                                                    minutes = str(info['records'][leaderboardz]['playedSeconds'] % 86400 % 3600 // 60)
                                                    seconds = str(info['records'][leaderboardz]['playedSeconds'] % 86400 % 3600 % 60)
                                                    timee = 'В игре: ' + days + 'д. ' + hours + 'ч.\n' + minutes + 'мин. ' + seconds + 'сек.'
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['username'] + "`", value='Уровень: ' + str(info['records'][leaderboardz]['level']) + '\n' + timee, inline=True)
                                            if leaderboard[2] == 'online':
                                                for leaderboardz in range(15):
                                                    days = str(info['records'][leaderboardz]['playedSeconds'] // 86400)
                                                    hours = str(info['records'][leaderboardz]['playedSeconds'] % 86400 // 3600)
                                                    minutes = str(info['records'][leaderboardz]['playedSeconds'] % 86400 % 3600 // 60)
                                                    seconds = str(info['records'][leaderboardz]['playedSeconds'] % 86400 % 3600 % 60)
                                                    timee = 'В игре: ' + days + 'д. ' + hours + 'ч.\n' + minutes + 'мин. ' + seconds + 'сек.'
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['username'] + "`", value=timee + '\nУровень: ' + str(info['records'][leaderboardz]['level']), inline=True)
                                        if leaderboard[1] == 'guild':
                                            if leaderboard[2] == 'level':
                                                for leaderboardz in range(15):
                                                    
                                                    if info['records'][leaderboardz]['created'] == -1:
                                                        answer = "очень давно"
                                                    else:
                                                        last_seen = time.ctime(info['records'][leaderboardz]['created'])
                                                        last_seen = last_seen.split(" ")
                                                        if last_seen[2] == "":
                                                            last_seen.pop(2)
                                                        for i in range(12):
                                                            if month[i] in last_seen:
                                                                last_seen.pop(1)
                                                                last_seen.insert(1, month_num[i])
                                                                last_seen.pop(0)
                                                                break
                                                        if len(last_seen[0]) == 1:
                                                            last_seen[0] = "0" + last_seen[0]
                                                        if len(last_seen[1]) == 1:
                                                            last_seen[1] = "0" + last_seen[1]
                                                        date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3][:2]
                                                        time_ls = "\n" + last_seen[2] + " (МСК)"
                                                        answer = date_ls + time_ls

                                                    emb.add_field(name="`" + info['records'][leaderboardz]['name'] + "`", value='Уровень: ' + str(info['records'][leaderboardz]['level']) + '\nВнесено коинов: ' + str(info['records'][leaderboardz]['totalCoins']) + '\nЗаработано опыта: ' + str(info['records'][leaderboardz]['totalExp']) + '\nСоздана: ' + answer, inline=True)
                                            if leaderboard[2] == 'total_coins':
                                                for leaderboardz in range(15):
                                                    
                                                    if info['records'][leaderboardz]['created'] == -1:
                                                        answer = "очень давно"
                                                    else:
                                                        last_seen = time.ctime(info['records'][leaderboardz]['created'])
                                                        last_seen = last_seen.split(" ")
                                                        if last_seen[2] == "":
                                                            last_seen.pop(2)
                                                        for i in range(12):
                                                            if month[i] in last_seen:
                                                                last_seen.pop(1)
                                                                last_seen.insert(1, month_num[i])
                                                                last_seen.pop(0)
                                                                break
                                                        if len(last_seen[0]) == 1:
                                                            last_seen[0] = "0" + last_seen[0]
                                                        if len(last_seen[1]) == 1:
                                                            last_seen[1] = "0" + last_seen[1]
                                                        date_ls = last_seen[1] + "." + last_seen[0] + "." + last_seen[3][:2]
                                                        time_ls = "\n" + last_seen[2] + " (МСК)"
                                                        answer = date_ls + time_ls

                                                    emb.add_field(name="`" + info['records'][leaderboardz]['name'] + "`", value='Внесено коинов: ' + str(info['records'][leaderboardz]['totalCoins']) + '\nЗаработано опыта: ' + str(info['records'][leaderboardz]['totalExp']) + '\nУровень: ' + str(info['records'][leaderboardz]['level']) + '\nСоздана: ' + answer, inline=True)

                                        if leaderboard[1] == 'ann' or leaderboard[1] == 'ann_monthly':
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nУбийств с лука: ' + str(info['records'][leaderboardz]['bowkills']) + '\nСрублено дерева: ' + str(info['records'][leaderboardz]['wood']) + '\nУдаров по базе: ' + str(info['records'][leaderboardz]['nexus']) + '\nВскопано земли: ' + str(info['records'][leaderboardz]['digged']) + '\nВскопано руды: ' + str(info['records'][leaderboardz]['ores']), inline=True)

                                        if leaderboard[1] == 'bb' or leaderboard[1] == 'bb_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']), inline=True)

                                        if leaderboard[1] == 'bp' or leaderboard[1] == 'bp_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nНабрано уровней: ' + str(info['records'][leaderboardz]['levels']), inline=True)

                                        if leaderboard[1] == 'bw' or leaderboard[1] == 'bw_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nКроватей: ' + str(info['records'][leaderboardz]['bedBreaked']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) +'\nКроватей: ' + str(info['records'][leaderboardz]['bedBreaked']), inline=True)
                                            if leaderboard[2] == 'bedBreaked' and leaderboard[1] == 'bw':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Кроватей: ' + str(info['records'][leaderboardz]['bedBreaked']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']), inline=True)

                                        if leaderboard[1] == 'cp' or leaderboard[1] == 'cp_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nТочек: ' + str(info['records'][leaderboardz]['resourcePointsBreaked']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) +'\nТочек: ' + str(info['records'][leaderboardz]['resourcePointsBreaked']), inline=True)

                                        if leaderboard[1] == 'dr' or leaderboard[1] == 'dr_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']), inline=True)

                                        if leaderboard[1] == 'duels' or leaderboard[1] == 'duels_monthly':
                                            if leaderboard[2] == 'total_wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Всего побед: ' + str(info['records'][leaderboardz]['total_wins']) + '\nВсего игр: ' + str(info['records'][leaderboardz]['total_games']) + '\nОдиночных побед: ' + str(info['records'][leaderboardz]['solo_wins']) + '\nОдиночных игр: ' + str(info['records'][leaderboardz]['solo_games']) + '\nКомандных побед: ' + str(info['records'][leaderboardz]['team_wins']) + '\nКомандных игр: ' + str(info['records'][leaderboardz]['team_games']) + '\nРейтинговых побед: ' + str(info['records'][leaderboardz]['ranked_wins']) + '\nРейтинговых игр: ' + str(info['records'][leaderboardz]['ranked_games']) + '\nПобед подряд: ' + str(info['records'][leaderboardz]['maxstrike']) + '\nПобед (classic): ' + str(info['records'][leaderboardz]['wins_classic']) + '\nПобед (на луках): ' + str(info['records'][leaderboardz]['wins_bow']) + '\nПобед (OP): ' + str(info['records'][leaderboardz]['wins_op']) + '\nПобед (на зельях): ' + str(info['records'][leaderboardz]['wins_potion']) + '\nПобед (UHC): ' + str(info['records'][leaderboardz]['wins_uhc']) + '\nПобед (BWH): ' + str(info['records'][leaderboardz]['wins_bwh']), inline=True)
                                            if leaderboard[2] == 'total_games' and leaderboard[1] == 'duels':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Всего побед: ' + str(info['records'][leaderboardz]['total_games']) + '\nВсего игр: ' + str(info['records'][leaderboardz]['total_wins']) + '\nОдиночных побед: ' + str(info['records'][leaderboardz]['solo_wins']) + '\nОдиночных игр: ' + str(info['records'][leaderboardz]['solo_games']) + '\nКомандных побед: ' + str(info['records'][leaderboardz]['team_wins']) + '\nКомандных игр: ' + str(info['records'][leaderboardz]['team_games']) + '\nРейтинговых побед: ' + str(info['records'][leaderboardz]['ranked_wins']) + '\nРейтинговых игр: ' + str(info['records'][leaderboardz]['ranked_games']) + '\nПобед подряд: ' + str(info['records'][leaderboardz]['maxstrike']) + '\nПобед (classic): ' + str(info['records'][leaderboardz]['wins_classic']) + '\nПобед (на луках): ' + str(info['records'][leaderboardz]['wins_bow']) + '\nПобед (OP): ' + str(info['records'][leaderboardz]['wins_op']) + '\nПобед (на зельях): ' + str(info['records'][leaderboardz]['wins_potion']) + '\nПобед (UHC): ' + str(info['records'][leaderboardz]['wins_uhc']) + '\nПобед (BWH): ' + str(info['records'][leaderboardz]['wins_bwh']), inline=True)
                                            if leaderboard[2] == 'rate' and leaderboard[1] == 'duels_monthly':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Рейтинг: ' + str(info['records'][leaderboardz]['rate']) + '\nМаксимальный рейтинг: ' + str(info['records'][leaderboardz]['max_rate']) + '\nВсего побед: ' + str(info['records'][leaderboardz]['total_wins']) + '\nВсего игр: ' + str(info['records'][leaderboardz]['total_games']) + '\nОдиночных побед: ' + str(info['records'][leaderboardz]['solo_wins']) + '\nОдиночных игр: ' + str(info['records'][leaderboardz]['solo_games']) + '\nКомандных побед: ' + str(info['records'][leaderboardz]['team_wins']) + '\nКомандных игр: ' + str(info['records'][leaderboardz]['team_games']) + '\nПобед (classic): ' + str(info['records'][leaderboardz]['wins_classic']) + '\nПобед (на луках): ' + str(info['records'][leaderboardz]['wins_bow']) + '\nПобед (OP): ' + str(info['records'][leaderboardz]['wins_op']) + '\nПобед (на зельях): ' + str(info['records'][leaderboardz]['wins_potion']) + '\nПобед (UHC): ' + str(info['records'][leaderboardz]['wins_uhc']) + '\nПобед (BWH): ' + str(info['records'][leaderboardz]['wins_bwh']), inline=True)

                                        if leaderboard[1] == 'gg' or leaderboard[1] == 'gg_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nУровней: ' + str(info['records'][leaderboardz]['levels']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУровней: ' + str(info['records'][leaderboardz]['levels']), inline=True)

                                        if leaderboard[1] == 'hg' or leaderboard[1] == 'hg_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']), inline=True)

                                        if leaderboard[1] == 'kpvp' or leaderboard[1] == 'kpvp_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)
                                            if leaderboard[2] == 'points' and leaderboard[1] == 'kpvp':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Очков: ' + str(info['records'][leaderboardz]['points']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)

                                        if leaderboard[1] == 'mw' or leaderboard[1] == 'mw_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nМобов убито: ' + str(info['records'][leaderboardz]['mobsKilled']) + '\nМобов послано: ' + str(info['records'][leaderboardz]['mobsSended']), inline=True)

                                        if leaderboard[1] == 'prison' or leaderboard[1] == 'prison_season':
                                            if leaderboard[2] == 'total_blocks':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Всего блоков: ' + str(info['records'][leaderboardz]['total_blocks']) + '\nЗаработано денег: ' + str(info['records'][leaderboardz]['earned_money']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nМобов убито: ' + str(info['records'][leaderboardz]['mobs']), inline=True)
                                            if leaderboard[2] == 'earned_money':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Заработано денег: ' + str(info['records'][leaderboardz]['earned_money']) + '\nВсего блоков: ' + str(info['records'][leaderboardz]['total_blocks']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nМобов убито: ' + str(info['records'][leaderboardz]['mobs']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + 'Всего блоков: ' + str(info['records'][leaderboardz]['total_blocks']) + '\nЗаработано денег: ' + str(info['records'][leaderboardz]['earned_money']) + '\nМобов убито: ' + str(info['records'][leaderboardz]['mobs']), inline=True)

                                        if leaderboard[1] == 'sw' or leaderboard[1] == 'sw_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nВыпущено стрел: ' + str(info['records'][leaderboardz]['arrowsFired']) + '\nБлоков сломано: ' + str(info['records'][leaderboardz]['blocksBroken']) + '\nБлоков поставлено: ' + str(info['records'][leaderboardz]['blocksPlaced']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nВыпущено стрел: ' + str(info['records'][leaderboardz]['arrowsFired']) + '\nБлоков сломано: ' + str(info['records'][leaderboardz]['blocksBroken']) + '\nБлоков поставлено: ' + str(info['records'][leaderboardz]['blocksPlaced']), inline=True)

                                        if leaderboard[1] == 'arc' or leaderboard[1] == 'arc_monthly':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)

                                        if leaderboard[1] == 'bridge':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nОчков: ' + str(info['records'][leaderboardz]['points']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nОчков: ' + str(info['records'][leaderboardz]['points']), inline=True)
                                            if leaderboard[2] == 'points':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Очков: ' + str(info['records'][leaderboardz]['points']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)

                                        if leaderboard[1] == 'jumpleague':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nЧекпоинтов: ' + str(info['records'][leaderboardz]['checkpoints']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nЧекпоинтов: ' + str(info['records'][leaderboardz]['checkpoints']), inline=True)

                                        if leaderboard[1] == 'murder':
                                            if leaderboard[2] == 'total_wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Всего побед: ' + str(info['records'][leaderboardz]['total_wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nПобед за мирного: ' + str(info['records'][leaderboardz]['wins_as_innocent']) + '\nПобед за маньяка: ' + str(info['records'][leaderboardz]['wins_as_maniac']) + '\nПобед за детектива: ' + str(info['records'][leaderboardz]['wins_as_detective']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nПобед за мирного: ' + str(info['records'][leaderboardz]['wins_as_innocent']) + '\nПобед за маньяка: ' + str(info['records'][leaderboardz]['wins_as_maniac']) + '\nПобед за детектива: ' + str(info['records'][leaderboardz]['wins_as_detective']) + '\nВсего побед: ' + str(info['records'][leaderboardz]['total_wins']), inline=True)
                                            if leaderboard[2] == 'wins_as_maniac':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед за маньяка: ' + str(info['records'][leaderboardz]['wins_as_maniac']) + '\nПобед за мирного: ' + str(info['records'][leaderboardz]['wins_as_innocent']) + '\nПобед за детектива: ' + str(info['records'][leaderboardz]['wins_as_detective'])  + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nВсего побед: ' + str(info['records'][leaderboardz]['total_wins']), inline=True)


                                        if leaderboard[1] == 'paintball':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nОчков: ' + str(info['records'][leaderboardz]['points']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nОчков: ' + str(info['records'][leaderboardz]['points']), inline=True)

                                        if leaderboard[1] == 'sheep':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПеретащено овец: ' + str(info['records'][leaderboardz]['tamed_sheep']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nПеретащено овец: ' + str(info['records'][leaderboardz]['tamed_sheep']), inline=True)
                                            if leaderboard[2] == 'tamed_sheep':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Перетащено овец: ' + str(info['records'][leaderboardz]['tamed_sheep']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games'])  + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)

                                        if leaderboard[1] == 'tntrun':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nСломано блоков: ' + str(info['records'][leaderboardz]['broken_blocks']), inline=True)

                                        if leaderboard[1] == 'tnttag':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']), inline=True)

                                        if leaderboard[1] == 'turfwars':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']), inline=True)

                                        if leaderboard[1] == 'luckywars':
                                            if leaderboard[2] == 'wins':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Побед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nУбийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nСломано лаки блоков: ' + str(info['records'][leaderboardz]['lucky_blocks']), inline=True)
                                            if leaderboard[2] == 'kills':
                                                for leaderboardz in range(15):
                                                    emb.add_field(name="`" + info['records'][leaderboardz]['user']['username'] + "`", value='Убийств: ' + str(info['records'][leaderboardz]['kills']) + '\nСмертей: ' + str(info['records'][leaderboardz]['deaths']) + '\nПобед: ' + str(info['records'][leaderboardz]['wins']) + '\nИгр: ' + str(info['records'][leaderboardz]['games']) + '\nСломано лаки блоков: ' + str(info['records'][leaderboardz]['lucky_blocks']), inline=True)
                                    await message.channel.send(embed=emb)



client = MyClient()
client.run('token')