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
def sc_empty_room(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女の部屋は空っぽ",
            camera=w.yuki,
            stage=w.on_dormitory,
            day=w.in_research, time=w.at_morning,
            )

def sc_underground(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("裏掲示板の存在",
            )

def sc_one_word(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("彼女への一言",
            )

## episode
def ep_reason(w: World):
    return w.episode("消えた理由",
            sc_empty_room(w),
            sc_underground(w),
            sc_one_word(w),
            ## NOTE
            ##  - 退学届けが出て、部屋から全ての荷物が引き払われていると知った
            ##  - ネットのない学内で、裏掲示板の存在を知る
            ##  - みんなの憧れだと思っていた彼女への、たった一行の、心無い毒矢のような言葉が書き込まれていた
            note="$yukiは彼女が消えたことが信じられず、その事情の調査を勝手に始める。しかしそこで浮かび上がった意外な事実に言葉を失った")
