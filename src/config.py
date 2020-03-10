# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("yuki", "由季", "加賀美,由季", 17,(2,20), "female", "学生", "me:わたし"),
        ("arisu", "亜里守", "有村,亜里守", 18,(9,9), "female", "学生", "me:私"),
        ## 三年生
        ("suzaki", "須崎", "須崎,麻紀", 18,(1,1), "female", "学生", "me:あたし"),
        ## 学校
        ("fran", "フラン", "", 56,(1,1), "male", "司書", "me:ワタシ"),
        ## その他
        ("teacher", "教師", "", 35,(1,1), "male", "教師", "me:私"),
        ("student", "女子生徒", "", 17,(1,1), "female", "me:私"),
        )
BASE_X = 14135
BASE_Y = 4306

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("Sapporo", "札幌", 14135,4306),
        ("InSchool", "学校内", BASE_X + 10, BASE_Y + 10),
        ("InDormitory", "寄宿舎内", BASE_X + 8, BASE_Y + 10),
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("ryaku_school", "聖女"),
        ("school", "聖部女学院", "Sapporo", "主要舞台"),
        ("dormitory", "寄宿舎", "Sapporo"),
        ## 学校
        ("classroom", "教室", "InSchool"),
        ("herclass", "先輩の教室", "InSchool"),
        ("backyard", "裏庭", "InSchool"),
        ("library", "図書室", "InSchool"),
        ("ground", "校庭", "InSchool"),
        ("corridor", "廊下", "InSchool"),
        ## 寄宿舎
        ("lounge", "談話室", "InDormitory"),
        ("myroom", "由季の部屋", "InDormitory"),
        ("herroom", "亜里守の部屋", "InDormitory"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("schoolday", "学校生活１", 1,20, 2020),
        ("goodbye", "彼女が出ていった日", 2,4,2020),
        ("noherday", "彼女のいない日々", 2,5, 2020),
        ("search", "捜索開始日", 2,8, 2020),
        ("research", "調査日", 2,13, 2020),
        ("findfeel", "気持ちを見つけた日", 2,14, 2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        ("bookmark", "百合の栞"),
        ## 小物
        ("bed", "ベッド"),
        ("blackboard", "黒板"),
        ("book", "本"),
        ("bookshelf", "本棚"),
        ("chair", "椅子"),
        ("chalk", "チョーク"),
        ("desk", "机"),
        ("notebook", "ノート"),
        ("shelf", "棚"),
        ("textbook", "教科書"),
        ("schooluni", "制服"),
        )

WORDS = (
        # Tag / 名前 / 紹介
        ("noteword001", "あの子の代筆自己紹介文、最低だった"),
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        ("揃え", "｜揃《そろ》え"),
        ("捉え", "｜捉《とら》え"),
        ("覗く", "｜覗《のぞ》く"),
        ("顎", "｜顎《あご》"),
        ("抑揚", "｜抑揚《よくよう》"),
        ("滲ま", "｜滲《にじ》ま"),
        ("捲り", "｜捲《めく》り"),
        ("拭う", "｜拭《ぬぐ》う"),
        ("躊躇", "｜躊躇《ちゅうちょ》"),
        ("抽斗", "｜抽斗《ひきだし》"),
        ## 人名
        ("加賀美由季", "｜加賀美《かがみ》｜由季《ゆき》"),
        ("有村亜里守", "｜有村《ありむら》｜亜里守《ありす》"),
        )

LAYERS = (
        # Key / Title / Words
        )

