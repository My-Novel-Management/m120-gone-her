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
            camera=w.yuki,
            stage=w.on_dormitory,
            day=w.in_schoolday, time=w.at_afternoon,
            )

def sc_longing(w: World):
    return w.scene("憧れの彼女",
            )

def sc_vanishing(w: World):
    return w.scene("彼女が消えた日",
            )

## episode
def ep_vanished(w: World):
    return w.episode("彼女が消えた",
            sc_girls_school(w),
            sc_longing(w),
            sc_vanishing(w),
            ## NOTE
            ##  - 女子専用の寄宿学校で、由季は女子同士の群れの生活に慣れられずにいた
            ##  - そんな由季は学校一の人気で誰もが憧れるアリスのことを羨ましく見ていた
            ##  - ある日、彼女が突然、学校から消えた。一週間しても姿を表さず、生徒たちの噂で学校を辞めたと聞いた
            note="女子専用の寄宿学校。そこで絶大な人気を誇る生徒がいた。けれど彼女はある日突然、学校から姿を消してしまう")
