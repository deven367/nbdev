# processors


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

On this page we’ll be using this private helper to process a notebook
and return the results, to simplify testing:

``` python
def _run_procs(procs=None, return_nb=False, path=_test_file):
    nbp = NBProcessor(path, procs)
    nbp.process()
    if return_nb: return nbp.nb
    return '\n'.join([str(cell) for cell in nbp.nb.cells])
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L32"
target="_blank" style="float:right; font-size:smaller">source</a>

### populate_language

>  populate_language (nb)

*Set cell language based on NB metadata and magics*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L42"
target="_blank" style="float:right; font-size:smaller">source</a>

### insert_warning

>  insert_warning (nb)

*Insert Autogenerated Warning Into Notebook after the first cell.*

This preprocessor inserts a warning in the markdown destination that the
file is autogenerated. This warning is inserted in the second cell so we
do not interfere with front matter.

``` python
res = _run_procs(insert_warning)
assert "<!-- WARNING: THIS FILE WAS AUTOGENERATED!" in res
```

``` python
L('foo', None, 'a').filter(lambda x:x == 1)
_tstre = re.compile('a')
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L71"
target="_blank" style="float:right; font-size:smaller">source</a>

### add_show_docs

>  add_show_docs (nb)

*Add show_doc cells after exported cells, unless they are already
documented*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L64"
target="_blank" style="float:right; font-size:smaller">source</a>

### cell_lang

>  cell_lang (cell)

``` python
res = _run_procs([populate_language, add_show_docs])
assert "show_doc(some_func)'" in res
assert "show_doc(and_another)'" in res
assert "show_doc(another_func)'" not in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L88"
target="_blank" style="float:right; font-size:smaller">source</a>

### fdiv

>  fdiv (attrs='')

*Create a fenced div markdown cell in quarto*

``` python
a = fdiv('.py-2')
test_eq(a.cell_type, 'markdown')
test_eq(a.source, '::: {.py-2}')
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L94"
target="_blank" style="float:right; font-size:smaller">source</a>

### boxify

>  boxify (cells)

*Add a box around `cells`*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L101"
target="_blank" style="float:right; font-size:smaller">source</a>

### mv_exports

>  mv_exports (nb)

*Move `exports` cells to after the
[`show_doc`](https://nbdev.fast.ai/api/showdoc.html#show_doc)*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L123"
target="_blank" style="float:right; font-size:smaller">source</a>

### add_links

>  add_links (cell)

*Add links to markdown cells*

``` python
res = _run_procs(add_links)
assert "[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array)" in res
assert "[`ModuleMaker`](https://nbdev.fast.ai/api/maker.html#modulemaker) but not a link to `foobar`." in res
assert "A link in a docstring: [`ModuleMaker`](https://nbdev.fast.ai/api/maker.html#modulemaker)." in res
assert "And not a link to <code>dict2nb</code>." in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L132"
target="_blank" style="float:right; font-size:smaller">source</a>

### add_fold

>  add_fold (cell)

*Add `code-fold` to `exports` cells*

``` python
res = _run_procs(add_fold)
assert "#| code-fold: show" in res
```

Gets rid of colors that are streamed from standard out, which can
interfere with static site generators:

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L140"
target="_blank" style="float:right; font-size:smaller">source</a>

### strip_ansi

>  strip_ansi (cell)

*Strip Ansi Characters.*

``` python
res = _run_procs(strip_ansi)
assert not _re_ansi_escape.findall(res)
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L146"
target="_blank" style="float:right; font-size:smaller">source</a>

### strip_hidden_metadata

>  strip_hidden_metadata (cell)

*Strips “hidden” metadata property from code cells so it doesn’t
interfere with docs rendering*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L151"
target="_blank" style="float:right; font-size:smaller">source</a>

### hide\_

>  hide_ (cell)

*Hide cell from output*

``` python
res = _run_procs(hide_)
assert 'you will not be able to see this cell at all either' not in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L158"
target="_blank" style="float:right; font-size:smaller">source</a>

### hide_line

>  hide_line (cell)

*Hide lines of code in code cells with the directive
[`hide_line`](https://nbdev.fast.ai/api/processors.html#hide_line) at
the end of a line of code*

``` python
res = _run_procs(hide_line)
assert r"def show():\n    a = 2\n    b = 3" not in res
assert r"def show():\n    a = 2"                in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L165"
target="_blank" style="float:right; font-size:smaller">source</a>

### filter_stream\_

>  filter_stream_ (cell, *words)

*Remove output lines containing any of `words` in `cell` stream output*

``` python
res = _run_procs(filter_stream_)
exp=r"'A line\n', 'Another line.\n'"
assert exp in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L175"
target="_blank" style="float:right; font-size:smaller">source</a>

### ai_magics

>  ai_magics (cell)

*A preprocessor to convert AI magics to markdown*

``` python
res = _run_procs(ai_magics)
assert "'source': 'This is a test.'" in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L184"
target="_blank" style="float:right; font-size:smaller">source</a>

### clean_magics

>  clean_magics (cell)

*A preprocessor to remove cell magic commands*

``` python
res = _run_procs(clean_magics)
assert "%%" not in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L191"
target="_blank" style="float:right; font-size:smaller">source</a>

### rm_header_dash

>  rm_header_dash (cell)

*Remove headings that end with a dash -*

``` python
res = _run_procs(rm_header_dash)
assert 'some words' in res
assert 'A heading to Hide' not in res
assert 'Yet another heading to hide' not in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L200"
target="_blank" style="float:right; font-size:smaller">source</a>

### rm_export

>  rm_export (cell)

*Remove cells that are exported or hidden*

``` python
res = _run_procs(rm_export)
assert 'dontshow' not in res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L211"
target="_blank" style="float:right; font-size:smaller">source</a>

### clean_show_doc

>  clean_show_doc (cell)

*Remove ShowDoc input cells*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L238"
target="_blank" style="float:right; font-size:smaller">source</a>

### exec_show_docs

>  exec_show_docs (nb)

*Execute cells needed for `show_docs` output, including exported cells
and imports*

``` python
res = _run_procs([add_show_docs, exec_show_docs])
assert res
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/processors.py#L271"
target="_blank" style="float:right; font-size:smaller">source</a>

### FilterDefaults

>  FilterDefaults ()

*Override
[`FilterDefaults`](https://nbdev.fast.ai/api/processors.html#filterdefaults)
to change which notebook processors are used*