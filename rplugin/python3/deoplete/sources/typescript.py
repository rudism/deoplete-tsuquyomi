import json

from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'typescript'
        self.mark = '[TS]'
        self.filetypes = ["typescript", "tsx", "typescript.tsx", "javascript", "jsx", "javascript.jsx"]
        self.input_pattern = '\.'
        self.is_bytepos = True
        self.rank = 500

    def get_complete_position(self, context):
        return self.vim.call('tsuquyomi#complete', 1, 0)

    def gather_candidates(self, context):
        def translate_candidate(item):
            item['word'] = item['name']
            return item

        completions = self.vim.call('tsuquyomi#tsClient#tsCompletions', context['bufpath'], context['position'][1], context['position'][2], 0)
        return list(map(translate_candidate, completions))
