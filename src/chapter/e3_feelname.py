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
            camera=w.yuki,
            stage=w.on_dormitory,
            day=w.in_findfeel, time=w.at_evening,
            )

def sc_mymind(w: World):
    return w.scene("私の本心",
            )

def sc_naming(w: World):
    return w.scene("気持ちの名前",
            )

## episode
def ep_feelingnama(w: World):
    return w.episode("気持ちの名前",
            sc_real_feeling(w),
            sc_mymind(w),
            sc_naming(w),
            ## NOTE
            ##  - 真実を手にして彼女の本当の姿（弱さ）と、その気持ちを知った由季
            ##  - 自分がずっと彼女を恋でも愛でもない気持ちを向けていたことに気づいた
            ##  - 自分の気持に名前をつけた
            note="真実を知った$yukiは自分がこんなに必死になった気持ちは何なのかと考え込む")
