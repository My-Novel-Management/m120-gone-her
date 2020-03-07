# -*- coding: utf-8 -*-
"""Episode: title
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_real_feeling(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女の本心",
            yuki.come(),
            yuki.do("彼女の机に座り、ここで彼女がどんな気持ちだったのかを想像する"),
            yuki.do("机に触れる",
                "普段の彼女を想像する", "目を閉じる"),
            yuki.think("教室を埋める同じ制服の、女子たち",
                "それに囲まれ、休み時間になれば青春時代特有の体臭をまとった生徒が寄ってきては、彼女を汚す",
                "笑顔を吸い上げる"),
            yuki.think("けれどそれを彼女は笑顔で受け流すのだ",
                "彼女の周囲には、だから笑顔が溢れていた",
                "誰に対しても同じように、まるで性善説しか信じていない純粋さで、彼女は接していた"),
            yuki.think("その、周囲の一人に、なりたかった"),
            yuki.think("でも、ユダがいたのだ",
                "それはおそらくどんな集団にも潜む、一点だけの漆黒",
                "太陽に黒点があるように、どんなに眩しい世界にも暗い影は存在する"),
            yuki.think("その誰かが、彼女に、毒矢を放った",
                "届かないはずだった言葉は、けれど彼女を射止め、致命傷になった"),
            yuki.do("部屋でゴミ箱から盗んだ紙を広げる",
                "そこには『誰かに迷惑をかける存在には、なりたくない』と書かれていた"),
            yuki.think("そのときの彼女の気持ちを考える"),
            camera=w.yuki,
            stage=w.on_classroom_int,
            day=w.in_findfeel, time=w.at_evening,
            )

def sc_naming(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    outside = W(w.outside)
    return w.scene("気持ちの名前",
            yuki.be(),
            yuki.do("立ち上がり、窓に立つ"),
            outside.look("夕暮れに染まる、気持ち悪い空"),
            yuki.think("自分の気持ちに今更に気づいて"),
            yuki.talk("どうしてなのよ！",
                "あなたさえいなければ、こんな気持ちになることなかったのに！",
                "この世界に最初から存在してなければ、こんな気持ちに"),
            yuki.do("校庭で遊んでいた女子生徒がちらと見たけど気にせず"),
            yuki.talk("$meは！　……$meは、$meなんか、全然、全然違う",
                "あなたとは違う",
                "目立たない、誰からも頼られない、惨めさすら認められず、存在感なんて皆無",
                "それなのに、どうしてそんな$meのことを、あなたは見ていたの？",
                "見てくれていたの？"),
            yuki.think("そっと送られていたメッセージを思い出す"),
            yuki.talk("デッド・リリィ……",
                "この気持ち、デッド・リリィだ"),
            yuki.do("そこには皺くしゃになった百合の栞が握られていた"),
            )

## episode
def ep_feelingnama(w: World):
    return w.episode("気持ちの名前",
            sc_real_feeling(w),
            sc_naming(w),
            ## NOTE
            ##  - 真実を手にして彼女の本当の姿（弱さ）と、その気持ちを知った由季
            ##  - 自分がずっと彼女を恋でも愛でもない気持ちを向けていたことに気づいた
            ##  - 自分の気持に名前をつけた
            note="真実を知った$yukiは自分がこんなに必死になった気持ちは何なのかと考え込む")
