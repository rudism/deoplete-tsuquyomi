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
        return self.vim.call('tsuquyomi#complete', 1, 0)

    def gather_candidates(self, context):
        bufpath = context['bufpath']
        line = context['position'][1]
        offset = context['position'][2]

        # get all completions
        completions = self.vim.call('tsuquyomi#tsClient#tsCompletions', bufpath, line, offset, 0)
        items = []
        entries = []
        for item in completions:
            candidate = {'word': item['name'], 'kind': item['kind']}
            items.append(candidate)
            entries.append(item['name'])

        # attach signatures
        infos = []
        try:
            infos = self.vim.call('tsuquyomi#makeCompleteMenu', bufpath, line, offset, entries)
        except:
            infos = []

        if len(infos) == len(entries):
            for i in range(len(items)):
                if items[i]['kind'] != 'warning':
                    # remove kind/type names from signatures
                    info = re.sub('^\(?'+items[i]['kind']+'\)? ([a-zA-Z0-9]+\.)?', '', infos[i])
                    items[i]['menu'] = info
                    # allow preview of method signatures
                    if items[i]['kind'] == 'method':
                        items[i]['info'] = info

        return items
