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
def sc_girls_school(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("女子学校",
            yuki.be("放課後になって"),
            yuki.do("誰もが友人と連れ立って、自分たちの席で話したり、どこかに出かけていったり"),
            yuki.do("$Sは一人きり、鞄に教科書を収めて、教室を出る"),
            camera=w.yuki,
            stage=w.on_classroom_int,
            day=w.in_schoolday, time=w.at_afternoon,
            )

def sc_lonely(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("寂しい少女",
            yuki.come("廊下を歩く"),
            yuki.explain("＜学校の説明＞"),
            yuki.do("階段を登る"),
            yuki.do("三年生の教室がある、その廊下を歩いて通り過ぎる"),
            yuki.do("その教室の一つから歓声が上がる"),
            stage=w.on_school,
            )

def sc_longing(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    suzaki = W(w.suzaki)
    return w.scene("憧れの彼女",
            yuki.be("窓から覗き込んで"),
            arisu.be("女子生徒に囲まれ、笑っている"),
            suzaki.come(),
            suzaki.talk("ねえ$arisuさん", "今度は本当に$meの紹介文書いてくれるの？"),
            arisu.talk("ええ、喜んで"),
            suzaki.talk("$arisuさんの紹介文て、その人の本当の魅力を引き出す素晴らしいものばかりだから",
                "どうすればそんな風に他人の素敵な部分を見つけられるの？"),
            arisu.talk("見つけるのではなくて、みんなが気づいていないだけ",
                "最初から全然素敵な部分のない人間なんていないわ",
                "特に$meたちのような可能性に満ちた世代の若者で、女性で、子どもでも大人でもない、そういった存在にはね"),
            yuki.do("教室の外に張り出されている各人の自己紹介を見る",
                "$full_arisu",
                "自分の紹介文は淡々としたものだ",
                "本が好き、人が好き、将来は誰かを素敵にする、そういう仕事に就きたいと"),
            yuki.think("自分とは違いすぎる、と落ち込んで、立ち去る"),
            stage=w.on_herclass_ext,
            )

def sc_vanishing(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女が消えた日",
            yuki.be(),
            yuki.do("授業中から、何だかざわついている"),
            yuki.do("授業を終えると、前の席に集まって女子生徒が話し始める",
                "それを聞いて、$full_arisuが消えたと知った"),
            yuki.talk("え？　あの、今、なんて？"),
            yuki.hear("彼女たちはあの$full_arisuが無断で授業を休んだと言った"),
            yuki.do("慌てて教室に確認に向かう"),
            yuki.do("既に三年の教室では騒動になっていて、部屋は空っぽで、誰もいなくなっていた。本当に消えた、不思議だ、神隠しだと話していた"),
            stage=w.on_school,
            day=w.in_goodbye,
            )

## episode
def ep_vanished(w: World):
    return w.episode("彼女が消えた",
            sc_girls_school(w),
            sc_lonely(w),
            sc_longing(w),
            sc_vanishing(w),
            ## NOTE
            ##  - 女子専用の寄宿学校で、由季は女子同士の群れの生活に慣れられずにいた
            ##  - そんな由季は学校一の人気で誰もが憧れるアリスのことを羨ましく見ていた
            ##  - ある日、彼女が突然、学校から消えた。一週間しても姿を表さず、生徒たちの噂で学校を辞めたと聞いた
            note="女子専用の寄宿学校。そこで絶大な人気を誇る生徒がいた。けれど彼女はある日突然、学校から姿を消してしまう")
