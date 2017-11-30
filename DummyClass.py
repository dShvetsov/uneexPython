#!/usr/bin/env python3

class Delay:
    def __init__(self, slot):
        self.slot = slot

    def delay(self, new):
        ret = self.slot
        self.slot = new
        return ret
