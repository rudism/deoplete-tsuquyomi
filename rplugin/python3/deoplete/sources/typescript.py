import re

from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'typescript'
        self.mark = '[TS]'
        self.filetypes = ["typescript"]
        self.input_pattern = '\.'
        self.is_bytepos = True
        self.rank = 500

    def get_complete_position(self, context):
        try:
            return self.vim.call('tsuquyomi#complete', 1, 0)
        except:
            return 0

    def gather_candidates(self, context):
        bufpath = context['bufpath']
        line = context['position'][1]
        offset = context['position'][2]

        # get all completions
        completions = []
        try:
            completions = self.vim.call('tsuquyomi#tsClient#tsCompletions', bufpath, line, offset, 0)
        except:
            completions = []
        items = []
        for item in completions:
            candidate = {'word': item['name'], 'kind': item['kind']}
            items.append(candidate)

        return items
