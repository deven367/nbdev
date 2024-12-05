# migrate


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

### Migrate notebooks

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L85"
target="_blank" style="float:right; font-size:smaller">source</a>

### MigrateProc

>  MigrateProc (nb)

*Migrate fastpages front matter in notebooks to a raw cell.*

Before you migrate the fastpages notebook, the front matter is specified
in Markdown like this:

``` python
_tst_nb = '../../tests/2020-09-01-fastcore.ipynb'
print(read_nb(_tst_nb).cells[0].source)
```

    # "fastcore: An Underrated Python Library"

    > A unique python library that extends the python programming language and provides utilities that enhance productivity.
    - author: "<a href='https://twitter.com/HamelHusain'>Hamel Husain</a>"
    - toc: false
    - image: images/copied_from_nb/fastcore_imgs/td.png
    - comments: true
    - search_exclude: true
    - hide: true
    - categories: [fastcore, fastai]
    - permalink: /fastcore/
    - badges: true

After migrating the notebook, the front matter is moved to a raw cell,
and some of the fields are converted to be compliant with Quarto.
Furthermore, aliases may be added in order to prevent broken links:

``` python
nbp = NBProcessor('../../tests/2020-09-01-fastcore.ipynb', procs=[FrontmatterProc, MigrateProc])
nbp.process()
_fm1 = _get_raw_fm(nbp.nb)
print(_fm1)
```

    ---
    aliases:
    - /fastcore/
    author: <a href='https://twitter.com/HamelHusain'>Hamel Husain</a>
    badges: true
    categories:
    - fastcore
    - fastai
    date: '2020-09-01'
    description: A unique python library that extends the python programming language
      and provides utilities that enhance productivity.
    draft: 'true'
    image: fastcore_imgs/td.png
    output-file: 2020-09-01-fastcore.html
    permalink: /fastcore/
    search: 'false'
    title: 'fastcore: An Underrated Python Library'
    toc: false

    ---

### Migrate Fastpages Markdown Front Matter

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L93"
target="_blank" style="float:right; font-size:smaller">source</a>

### fp_md_fm

>  fp_md_fm (path)

*Make fastpages front matter in markdown files quarto compliant.*

Here is what the front matter of a fastpages markdown post looks like
before migration:

``` python
print(run('head -n13 ../../tests/2020-01-14-test-markdown-post.md'))
```

    ---

    toc: true
    layout: post
    description: A minimal example of using markdown with fastpages.
    categories: [markdown]
    title: An Example Markdown Post


    ---

    # Example Markdown Post

And this is what it looks like after migration:

``` python
_res = fp_md_fm('../../tests/2020-01-14-test-markdown-post.md')
print(_res[:300])
```

    ---
    aliases:
    - /markdown/2020/01/14/test-markdown-post
    categories:
    - markdown
    date: '2020-01-14'
    description: A minimal example of using markdown with fastpages.
    layout: post
    title: An Example Markdown Post
    toc: true

    ---

    # Example Markdown Post

    ## Basic setup

    Jekyll requires blog post files to b

``` python
#hide
_res = fp_md_fm('../../tests/2022-09-06-homeschooling.md')
test_eq(_res,
"""---
aliases:
- /2022/09/06/homeschooling
author: Rachel Thomas
categories:
- advice
- health
date: '2022-09-06'
description: You can permanently damage your back, neck, and wrists from working without
  an ergonomic setup.  Learn how to create one for less at home.
image: /images/ergonomic1-short.jpg
summary: You can permanently damage your back, neck, and wrists from working without
  an ergonomic setup.  Learn how to create one for less at home.
tags: advice health
title: 'Essential Work-From-Home Advice: Cheap and Easy Ergonomic Setups'

---

Lorem ipsum
""")
```

## Convert nbdev v1 projects to nbdev v2

### Directives

nbdev v2 directives start with a `#|` whereas v1 directives were
comments without a pipe `|`.

``` python
_test_dir = """
#default_exp
 #export
# collapse-show
#collapse-hide
#collapse
# collapse_output
not_dir='#export'
# hide_input
foo
# hide
"""
test_eq(_repl_directives(_test_dir),
"""
#| default_exp
#| export
#| code-fold: show
#| code-fold: true
#| code-fold: true
# collapse_output
not_dir='#export'
#| echo: false
foo
#| include: false
""")
```

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L122"
target="_blank" style="float:right; font-size:smaller">source</a>

### \_repl_v1dir

>  _repl_v1dir (cell)

*Replace nbdev v1 with v2 directives.*

for example, if any of the lines below are valid nbdev v1 directives,
they replaced with a `#|`, but only before the first line of code:

## Callouts

In fastpages, there was a markdown shortuct for callouts for `Note`,
`Tip`, `Important` and `Warning` with block quotes (these only worked in
notebooks). Since Quarto has its own [callout
blocks](https://quarto.org/docs/authoring/callouts.html#callout-types)
with markdown syntax, we do not implement these shortcuts in nbdev.
Instead, we offer a manual conversion utility for these callouts so that
you can migrate from fastpages to Quarto.

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L134"
target="_blank" style="float:right; font-size:smaller">source</a>

### \_convert_callout

>  _convert_callout (s)

*Convert nbdev v1 to v2 callouts.*

For example, the below markdown:

``` python
_callouts="""
## Boxes / Callouts

> Warning: There will be no second warning!

Other text

> Important: Pay attention! It's important.

> Tip: This is my tip.

> Note: Take note of `this.`
"""
```

Gets converted to:


    ## Boxes / Callouts

    :::{.callout-warning}

    There will be no second warning!

    :::

    Other text

    :::{.callout-important}

    Pay attention! It's important.

    :::

## Video Embeds

In fastpages, you could embed videos with a simple markdown shortcut
involving a block quote with the prefix `youtube:`, that looked like
this

`> youtube: https://youtu.be/XfoYk_Z5AkI`

However, in Quarto you can use the [video
extension](https://github.com/quarto-ext/video) to embed videos.

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L141"
target="_blank" style="float:right; font-size:smaller">source</a>

### \_convert_video

>  _convert_video (s)

*Replace nbdev v1 with v2 video embeds.*

``` python
_videos="""
## Videos

> youtube: https://youtu.be/XfoYk_Z5AkI
"""
```

``` python
print(_convert_video(_videos))
```


    ## Videos

    https://youtu.be/XfoYk_Z5AkI

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L154"
target="_blank" style="float:right; font-size:smaller">source</a>

### migrate_nb

>  migrate_nb (path, overwrite=True)

*Migrate Notebooks from nbdev v1 and fastpages.*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L162"
target="_blank" style="float:right; font-size:smaller">source</a>

### migrate_md

>  migrate_md (path, overwrite=True)

*Migrate Markdown Files from fastpages.*

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/migrate.py#L170"
target="_blank" style="float:right; font-size:smaller">source</a>

### nbdev_migrate

>  nbdev_migrate (path:str=None, no_skip:bool=False)

*Convert all markdown and notebook files in `path` from v1 to v2*

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th></th>
<th><strong>Type</strong></th>
<th><strong>Default</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>path</td>
<td>str</td>
<td>None</td>
<td>A path or glob containing notebooks and markdown files to
migrate</td>
</tr>
<tr>
<td>no_skip</td>
<td>bool</td>
<td>False</td>
<td>Do not skip directories beginning with an underscore</td>
</tr>
</tbody>
</table>