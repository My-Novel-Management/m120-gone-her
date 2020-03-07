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
def sc_noher_days(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女のいない日々",
            yuki.be("つまらない顔で授業を受けている"),
            yuki.do("国語の授業", "誰も聞いていない",
                "$arisuがいなくなった、という噂には色々な尾ひれがついていた"),
            yuki.do("でも今朝、誰かが言っていた",
                "退学した、と"),
            yuki.think("理由も何も分からないし、誰にも事情を伝えていないらしい"),
            yuki.think("おそらく数日、せめて一月くらい経てば誰も話題にしなくなる",
                "話題の流行の移り変わりは早い",
                "もう明日には別の話題で盛り上がっている",
                "そんな場所だ"),
            yuki.think("でも、なぜだろう",
                "$Sはぽっかりと穴が開いたように、そこにまるで彼女が埋まっていたかのように、",
                "しくしくと胸が痛んだ"),
            camera=w.yuki,
            stage=w.on_classroom_int,
            day=w.in_noherday, time=w.at_midmorning,
            )

def sc_searching(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    suzaki = W(w.suzaki)
    return w.scene("捜索",
            yuki.come("三年生の教室にやってくる"),
            yuki.explain("昼休み"),
            yuki.do("教室の様子を見つめる",
                "彼女がいた頃はいつも休憩時間になれば回りに生徒が集まった",
                "でも今はそれぞれの小さな島を守るようにして、ひっそりとしている"),
            yuki.think("彼女一人消えても何も変わらない",
                "そんな風に同級生が言っていたが、そうでもないらしい",
                "明らかに空気が淀んでいた",
                "それだけ彼女の存在が大きかったのだ"),
            yuki.hear("と、生徒の一人が声をあげる"),
            suzaki.be(),
            suzaki.talk("誰が$arisuさんを追い出したんだよ！"),
            yuki.think("どういうことなんだろう、と思う"),
            yuki.explain("話の内容を聞くと、彼女の人気に嫉妬した誰かが彼女を傷つけたんじゃないのか、という話だった",
                "けれどそんな兆候はなく、確かに陰口こそあったろうが、彼女は誰も傷つけない",
                "そういう聖母みたいな女性だった",
                "もちろんそれでも嫉妬心は生まれるだろう",
                "でも、彼女がそういった陰口で突然消えるとは思えなかった"),
            suzaki.talk("じゃあ、どうして$arisuさんはいなくなったの？"),
            yuki.do("誰も答えられない",
                "答えは誰も知らないのだ"),
            stage=w.on_school,
            day=w.in_search, time=w.at_noon,
            )

def sc_underground(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    fran = W(w.fran)
    return w.scene("裏掲示板の存在",
            yuki.come("放課後、図書室にやってくる"),
            yuki.do("利用率はあまり高くない",
                "場所が遠いし、暗くて、あまり歓迎されない",
                "何より司書の男の人が誰も苦手だった"),
            fran.be(),
            fran.do("ぎょろっと大きな目が$CSを見た"),
            yuki.do("会釈だけしてカウンターを過ぎる"),
            _.do("何かあれば図書室に籠もる", "それがいつもの$Sの自己防衛方法だった"),
            yuki.do("そういえば、最初に$arisuの存在を見つけたのも、ここだった",
                "まだ一年の頃のことだ"),
            yuki.think("あの時はただ綺麗な人だとしか思わなかった",
                "彼女は当時から人気はあったが、それが爆発的人気を得るようになったのは、彼女の企画だ",
                "それは紹介文代筆サービス"),
            yuki.explain("教室の外に貼られたそれぞれの写真付きの自己紹介文",
                "その文章を彼女は実に巧みに書き上げた",
                "何度も校内の論文や作文の賞を貰っていたし、外部のコンクールでも常連入賞者だった彼女にとって、それはずっと楽なものだったろう"),
            yuki.think("$S自身の紹介文は自分で書いたものだ",
                "そういえば一度その前に立ち止まって$arisuがじっと眺めているのを目撃した",
                "他の生徒に用事があったみたいだったけれど、あれは心臓がおかしくなりそうだった"),
            yuki.do("図書館の一番奥、そこに貸出禁止の書棚がある",
                "学校の歴史や分厚い資料",
                "今までの学生の記録など",
                "そういったものは貸し出せないようになっていた"),
            yuki.do("その中に、名前のない本を見つける",
                "ただそこから飛び出ている栞を見つけた",
                "百合の栞だ"),
            yuki.do("その本を引き抜く",
                "こっそり中身を見てみると、そこには色々な人の字で、色々な人間の愚痴、悪口、陰口に誹謗中傷が書き込まれていた"),
            yuki.talk("何これ……"),
            yuki.do("思わず落として大きな音がして、びっくりする"),
            fran.talk("何だ？"),
            yuki.do("$franがやってくる気配に、慌てて棚に戻す"),
            yuki.talk("手が当たって落としてしまって。すみません"),
            fran.talk("大事なものばかりだから、丁寧に扱って下さいね"),
            fran.do("行ってしまう"),
            yuki.do("もう一度見る",
                "そこにある沢山の闇",
                "その中に見つけてしまう",
                "名指しで書かれていた「紹介文代筆」批判を"),
            yuki.do("そしてもうひとつ",
                "それは明らかに$arisuの字と分かる細く丁寧な文字で、何故か$Sの名前があった"),
            yuki.do("それをちぎり取って、逃げ出す"),
            stage=w.on_library_int,
            day=w.in_research, time=w.at_afterschool,
            )

def sc_one_word(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女への一言",
            yuki.come("慌てて自分の部屋に戻ってくる"),
            yuki.do("破ってきたページを見てみる",
                "それを見て、あの言葉が彼女を傷つけたと知る"),
            stage=w.on_myroom_int,
            )

## episode
def ep_reason(w: World):
    return w.episode("消えた理由",
            sc_noher_days(w),
            sc_searching(w),
            sc_underground(w),
            sc_one_word(w),
            ## NOTE
            ##  - 退学届けが出て、部屋から全ての荷物が引き払われていると知った
            ##  - ネットのない学内で、裏掲示板の存在を知る
            ##  - みんなの憧れだと思っていた彼女への、たった一行の、心無い毒矢のような言葉が書き込まれていた
            note="$yukiは彼女が消えたことが信じられず、その事情の調査を勝手に始める。しかしそこで浮かび上がった意外な事実に言葉を失った")
