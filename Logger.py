#!/usr/bin/python

class Logger:
    def __init__(self):
        self.text = []

    def record(self, str):
        self.text.append(str)