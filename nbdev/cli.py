# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/cli.ipynb.

# %% ../nbs/api/cli.ipynb 2
from __future__ import annotations
import warnings

from .config import *
from .process import *
from .processors import *
from .doclinks import *
from .test import *
from .clean import *
from .quarto import nbdev_readme, refresh_quarto_yml
from .frontmatter import FrontmatterProc

from execnb.nbio import *
from fastcore.meta import *
from fastcore.utils import *
from fastcore.script import *
from fastcore.style import S
from fastcore.shutil import rmtree,move

from urllib.error import HTTPError
from contextlib import redirect_stdout
import os, tarfile, sys

# %% auto 0
__all__ = ['nbdev_filter', 'extract_tgz', 'nbdev_new', 'chelp']

# %% ../nbs/api/cli.ipynb 5
@call_parse
def nbdev_filter(
    nb_txt:str=None,  # Notebook text (uses stdin if not provided)
    fname:str=None,  # Notebook to read (uses `nb_txt` if not provided)
    printit:bool_arg=True, # Print to stdout?
):
    "A notebook filter for Quarto"
    os.environ["IN_TEST"] = "1"
    try: filt = globals()[get_config().get('exporter', 'FilterDefaults')]()
    except FileNotFoundError: filt = FilterDefaults()
    if fname:        nb_txt = Path(fname).read_text()
    elif not nb_txt: nb_txt = sys.stdin.read()
    nb = dict2nb(loads(nb_txt))
    if printit:
        with open(os.devnull, 'w') as dn:
            with redirect_stdout(dn): filt(nb)
    else: filt(nb)
    res = nb2str(nb)
    del os.environ["IN_TEST"]
    if printit: print(res, flush=True)
    else: return res

# %% ../nbs/api/cli.ipynb 8
def extract_tgz(url, dest='.'):
    from fastcore.net import urlopen
    with urlopen(url) as u: tarfile.open(mode='r:gz', fileobj=u).extractall(dest)

# %% ../nbs/api/cli.ipynb 9
def _render_nb(fn, cfg):
    "Render templated values like `{{lib_name}}` in notebook at `fn` from `cfg`"
    txt = fn.read_text()
    txt = txt.replace('from your_lib.core', f'from {cfg.lib_path}.core') # for compatibility with old templates
    for k,v in cfg.d.items(): txt = txt.replace('{{'+k+'}}', v)
    fn.write_text(txt)

# %% ../nbs/api/cli.ipynb 10
def _update_repo_meta(cfg):
    "Enable gh pages and update the homepage and description in your GitHub repo."
    token=os.getenv('GITHUB_TOKEN')
    if token: 
        from ghapi.core import GhApi
        api = GhApi(owner=cfg.user, repo=cfg.repo, token=token)
        try: api.repos.update(homepage=f'{cfg.doc_host}{cfg.doc_baseurl}', description=cfg.description)
        except HTTPError:print(f"Could not update the description & URL on the repo: {cfg.user}/{cfg.repo} using $GITHUB_TOKEN.\n"
                  "Use a token with the correction permissions or perform these steps manually.")

# %% ../nbs/api/cli.ipynb 11
@call_parse
@delegates(nbdev_create_config)
def nbdev_new(**kwargs):
    "Create an nbdev project."
    from ghapi.core import GhApi
    nbdev_create_config.__wrapped__(**kwargs)
    cfg = get_config()
    _update_repo_meta(cfg)

    path = Path()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        tag = GhApi(gh_host='https://api.github.com', authenticate=False).repos.get_latest_release('fastai', 'nbdev-template').tag_name
    url = f"https://github.com/fastai/nbdev-template/archive/{tag}.tar.gz"
    extract_tgz(url)
    tmpl_path = path/f'nbdev-template-{tag}'

    cfg.nbs_path.mkdir(exist_ok=True)
    nbexists = bool(first(cfg.nbs_path.glob('*.ipynb')))
    _nbs_path_sufs = ('.ipynb','.css')
    for o in tmpl_path.ls():
        p = cfg.nbs_path if o.suffix in _nbs_path_sufs else path
        if o.name == '_quarto.yml': continue
        if o.name == 'index.ipynb': _render_nb(o, cfg)
        if o.name == '00_core.ipynb' and not nbexists: move(o, p)
        elif not (path/o.name).exists(): move(o, p)
    rmtree(tmpl_path)

    refresh_quarto_yml()

    nbdev_export.__wrapped__()
    nbdev_readme.__wrapped__()

# %% ../nbs/api/cli.ipynb 15
@call_parse
def chelp():
    "Show help for all console scripts"
    from fastcore.xtras import console_help
    console_help('nbdev')
