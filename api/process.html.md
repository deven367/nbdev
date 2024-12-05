# process


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Special comments at the start of a cell can be used to provide
information to `nbdev` about how to process a cell, so we need to be
able to find the location of these comments.

``` python
minimal = read_nb('../../tests/minimal.ipynb')
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L29"
target="_blank" style="float:right; font-size:smaller">source</a>

### nb_lang

>  nb_lang (nb)

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L54"
target="_blank" style="float:right; font-size:smaller">source</a>

### first_code_ln

>  first_code_ln (code_list, re_pattern=None, lang='python')

*get first line number where code occurs, where `code_list` is a list of
code*

``` python
_tst = """ 
#|default_exp
 #|export
#|hide_input
foo
"""
test_eq(first_code_ln(_tst.splitlines(True)), 4)
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L67"
target="_blank" style="float:right; font-size:smaller">source</a>

### extract_directives

>  extract_directives (cell, remove=True, lang='python')

*Take leading comment directives from lines of code in `ss`, remove
`#|`, and split*

Comment directives start with `#|`, followed by whitespace delimited
tokens, which
[`extract_directives`](https://nbdev.fast.ai/api/process.html#extract_directives)
extracts from the start of a cell, up until a blank line or a line
containing something other than comments. The extracted lines are
removed from the source.

``` python
exp  = AttrDict(source = """#|export module
#|eval:false
#| hide
# | foo bar
# |woo: baz
1+2
#bar""")

# this one has #|hide: with a colon at the end, wich is quarto compliant
exp2  = AttrDict(source = """#|export module
#|eval:false
#| hide:
# | foo bar
# |woo: baz
1+2
#bar""")

_answer = {'export':['module'], 'hide':[], 'eval:': ['false'], 'foo': ['bar'], 'woo:': ['baz']}

test_eq(extract_directives(exp), _answer)
test_eq(extract_directives(exp2), _answer)
test_eq(exp.source, '#|eval: false\n# |woo: baz\n1+2\n#bar')
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L77"
target="_blank" style="float:right; font-size:smaller">source</a>

### opt_set

>  opt_set (var, newval)

*newval if newval else var*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L82"
target="_blank" style="float:right; font-size:smaller">source</a>

### instantiate

>  instantiate (x, **kwargs)

*Instantiate `x` if it’s a type*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L92"
target="_blank" style="float:right; font-size:smaller">source</a>

### NBProcessor

>  NBProcessor (path=None, procs=None, nb=None, debug=False,
>                   rm_directives=True, process=False)

*Process cells and nbdev comments in a notebook*

Cell processors can be callables (e.g regular functions), in which case
they are called for every cell (set a cell’s source to `None` to remove
the cell):

``` python
everything_fn = '../../tests/01_everything.ipynb'

def print_execs(cell):
    if 'exec' in cell.source: print(cell.source)

NBProcessor(everything_fn, print_execs).process()
```

    ---
    title: Foo
    execute:
      echo: false
    ---
    exec("o_y=1")
    exec("p_y=1")
    _all_ = [o_y, 'p_y']

Comment directives are put in a cell attribute `directive_` as a
dictionary keyed by directive name:

``` python
def printme_func(cell):
    if cell.directives_ and 'printme' in cell.directives_: print(cell.directives_['printme'])

NBProcessor(everything_fn, printme_func).process()
```

    ['testing']

However, a more convenient way to handle comment directives is to use a
*class* as a processor, and include a method in your class with the same
name as your directive, surrounded by underscores:

``` python
class _PrintExample:
    def _printme_(self, cell, to_print): print(to_print)

NBProcessor(everything_fn, _PrintExample()).process()
```

    testing

In the case that your processor supports just one comment directive, you
can just use a regular function, with the same name as your directive,
but with an underscore appended – here `printme_` is identical to
`_PrintExample` above:

``` python
def printme_(cell, to_print): print(to_print)

NBProcessor(everything_fn, printme_).process()
```

    testing

``` python
NBProcessor(everything_fn, _PrintExample()).process()
```

    testing

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/process.py#L132"
target="_blank" style="float:right; font-size:smaller">source</a>

### Processor

>  Processor (nb)

*Base class for processors*

For more complex behavior, inherit from
[`Processor`](https://nbdev.fast.ai/api/process.html#processor), and
override one of more of `begin()` (called before any cells are
processed), `cell()` (called for each cell), and `end()` (called after
all cells are processed). You can also include comment directives (such
as the `_printme` example above) in these subclasses. Subclasses will
automatically have access to `self.nb`, containing the processed
notebook.

``` python
class CountCellProcessor(Processor):
    def begin(self):
        print(f"First cell:\n{self.nb.cells[0].source}")
        self.count=0
    def cell(self, cell):
        if cell.cell_type=='code': self.count += 1
    def end(self): print(f"* There were {self.count} code cells")
```

``` python
NBProcessor(everything_fn, CountCellProcessor).process()
```

    First cell:
    ---
    title: Foo
    execute:
      echo: false
    ---
    * There were 26 code cells