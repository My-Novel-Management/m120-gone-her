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
from src.chapter.e1_vanish import ep_vanished
from src.chapter.e2_reason import ep_reason
from src.chapter.e3_feelname import ep_feelingnama

## define alias
W = Writer
_ = W.getWho()

## chapter
def ch_main(w: World):
    return w.chapter("main",
            ep_vanished(w),
            ep_reason(w),
            ep_feelingnama(w),
            ## NOTE
            ##  - 彼女が消えた
            ##  - その事情を探り、どうやら誰かの心ない書き込みにより転校したことを知る
            ##  - そこまで必死に探した自分の気持に、名前をつけた
            note="憧れていた$arisuが突然学校からいなくなり、ぽっかりと開いたところに残っていた気持ちを見つけた")
