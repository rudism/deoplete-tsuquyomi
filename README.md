deoplete-tsuquyomi
==================

Heavily based on/stolen from deoplete-omnisharp: https://gitlab.com/mixedCase/deoplete-omnisharp

### Required

- Neovim
- deoplete.nvim: https://github.com/neovim/neovim/
- tsuquyomi: https://github.com/Quramy/tsuquyomi

### Installation

Instructions are for vim-plug and were only tested on Linux:

	" Installs deoplete.nvim:
	Plug 'Shougo/deoplete.nvim'
	" Installs tsuquyomi
	Plug 'Quramy/tsuquyomi'
	" Installs and builds vimproc (required to launch tsserver)
	Plug 'Shougo/vimproc.vim', {'do': 'make'}
	" Installs this source
	Plug 'rudism/deoplete-tsuquyomi'

### License

The MIT License. Full copy of the license included.
