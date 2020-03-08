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
    stu = W(w.student)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("女子学校",
            w.comment("携帯電話が使えないことをどこかで示す"),
            yuki.be("放課後になって"),
            stu.be("#教室に残る複数の生徒たち"),
            inside.look("＜教室の様子／高校と分かるもの＞"),
            _.look("黒板に書かれた可愛らしい文字"),
            yuki.do("女子しかいない教室",
                "彼女たちの特有の汗の香りが、閉め切られてエアコンの効いた教室に籠もっている",
                "でもそれに彼女たちは気づかない"),
            _.do("自分たちだけの世界に籠り、楽しそうにしゃべる",
                "しゃべりながらも、目の前の、あるいは隣の、別の席の視線を気にして、",
                "そっと探る",
                "男性のいない世界でも、女子は誰かを愛した",
                "それを百合と世間では呼ぶらしい"),
            _.think("でもその感情を$Sは軽蔑していた"),
            yuki.do("誰もが友人と連れ立って、自分たちの席で話したり、どこかに出かけていったり"),
            yuki.do("$Sはいつも孤独だ",
                "一人で昼ごはん、一人でトイレ、一人で体育の時間を休む",
                "鞄に教科書を収めて立ち上がると、教室を出た"),
            ## NOTE
            ##  英語の授業から始める。ここで「リリィ」という単語を教科書に見つけておく
            ##  はじまりの場所なので彼女の孤独感と他生徒の百合具合を見せる
            camera=w.yuki,
            stage=w.on_classroom_int,
            day=w.in_schoolday, time=w.at_afternoon,
            )

def sc_lonely(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    inside = W(w.inside)
    return w.scene("寂しい少女",
            yuki.come("廊下を歩く"),
            yuki.explain("＜学校の説明＞"),
            yuki.do("階段を登る"),
            inside.look("＜廊下の様子＞"),
            _.look("教室の裏には沢山の自己紹介文が貼り付けられている",
                "写真付きの紹介文はまるで遺影が並ぶみたいに、$CSは感じる"),
            yuki.do("三年生の教室がある、その廊下を歩いて通り過ぎる"),
            yuki.do("沢山の下級生が廊下に集まって、その教室を覗き込んでいる"),
            yuki.do("その教室の一つから歓声が上がる"),
            ## NOTE
            ##  いつもわざと通ってから、寄宿舎に帰る
            ##  多くの下級生たちがそうしている
            stage=w.on_school,
            )

def sc_longing(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    suzaki = W(w.suzaki)
    return w.scene("憧れの彼女",
            yuki.be("窓から覗き込んで"),
            arisu.be("女子生徒に囲まれ、笑っている"),
            arisu.look("＜外見描写＞"),
            _.look("長い黒髪、大きな瞳、しゅっとした顎に小さな唇",
                "美人という言葉よりも美人形という形容がよく似合う"),
            yuki.do("下級生たちは誰もが休み時間や放課後に、彼女を見に訪れる",
                "それに対して嫌な顔ひとつせずに時に手を振り返したり、笑顔を向ける",
                "その仕草から$on_ryaku_schoolの女神と呼称されていた"),
            suzaki.come(),
            suzaki.look("＜外見に特長を持たせる＞"),
            w.eventStart("$arisuの紹介文代筆"),
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
            ## NOTE
            ##  ここでアリスの異常性とカリスマ性を示す
            ##  また他の生徒からの視線と、由季の視線の差を見せる
            stage=w.on_herclass_ext,
            )

def sc_vanishing(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女が消えた日",
            yuki.be(),
            yuki.do("授業中から、何だかざわついている"),
            yuki.do("授業を終えると、前の席に集まって女子生徒が話し始める",
                "それを聞いて、$full_arisuが消えたと知った"),
            w.eventStart("$arisu失踪"),
            yuki.talk("え？　あの、今、なんて？"),
            yuki.hear("彼女たちはあの$full_arisuが無断で授業を休んだと言った"),
            yuki.do("慌てて教室に確認に向かう"),
            yuki.do("既に三年の教室では騒動になっていて、部屋は空っぽで、誰もいなくなっていた。本当に消えた、不思議だ、神隠しだと話していた"),
            stage=w.on_school,
            ## NOTE
            ##  ここで事件開始
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
