# -*- coding: utf-8 -*-
"""Chapter: main
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_tmp(w: World):
    yuki, arisu = W(w.yuki), W(w.arisu)
    return w.scene("Sc: xxx",
            camera=w.yuki,
            stage=w.on_school,
            day=w.in_goodbye, time=w.at_afternoon,
            )

## episode
def ep_tmp(w: World):
    return w.episode("Ep: xxx",
            sc_tmp(w),
            )

## chapter
def ch_main(w: World):
    return w.chapter("main",
            ep_tmp(w),
            )
