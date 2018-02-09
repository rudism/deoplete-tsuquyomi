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
        entries = []
        try:
            completions = self.vim.call('tsuquyomi#tsClient#tsCompletions', bufpath, line, offset, 0)
        except:
            completions = []
        items = []
        for item in completions:
            candidate = {'word': item['name'], 'kind': item['kind']}
            items.append(candidate)
            if item['kind'] == 'method' or item['kind'] == 'property':
                entries.append(item['name'])

        infos = []
        try:
            infos = self.vim.call('tsuquyomi#makeCompleteMenu', bufpath, line, offset, entries)
        except:
            infos = []

        if len(infos) == len(entries):
            i = 0
            for item in items:
                if item['kind'] == 'method' or item['kind'] == 'property':
                    info = re.sub('^\(?'+items[i]['kind']+'\)? ([a-zA-Z0-9]+\.)?', '', infos[i])
                    item['menu'] = info
                    if item['kind'] == 'method':
                        item['info'] = info
                    i += 1

        return items
