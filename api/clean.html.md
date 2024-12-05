# clean


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

To avoid pointless conflicts while working with jupyter notebooks (with
different execution counts or cell metadata), it is recommended to clean
the notebooks before committing anything (done automatically if you
install the git hooks with
[`nbdev_install_hooks`](https://nbdev.fast.ai/api/clean.html#nbdev_install_hooks)).
The following functions are used to do that.

## Trust

------------------------------------------------------------------------

<a href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L25"
target="_blank" style="float:right; font-size:smaller">source</a>

### nbdev_trust

>  nbdev_trust (fname:str=None, force_all:bool=False)

*Trust notebooks matching `fname`*

<table>
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
<td>fname</td>
<td>str</td>
<td>None</td>
<td>A notebook name or glob to trust</td>
</tr>
<tr>
<td>force_all</td>
<td>bool</td>
<td>False</td>
<td>Also trust notebooks that haven’t changed</td>
</tr>
</tbody>
</table>

## Clean

------------------------------------------------------------------------

<a href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L86"
target="_blank" style="float:right; font-size:smaller">source</a>

### clean_nb

>  clean_nb (nb, clear_all=False, allowed_metadata_keys:list=None,
>                allowed_cell_metadata_keys:list=None, clean_ids=True)

*Clean `nb` from superfluous metadata*

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
<td>nb</td>
<td></td>
<td></td>
<td>The notebook to clean</td>
</tr>
<tr>
<td>clear_all</td>
<td>bool</td>
<td>False</td>
<td>Remove all cell metadata and cell outputs?</td>
</tr>
<tr>
<td>allowed_metadata_keys</td>
<td>list</td>
<td>None</td>
<td>Preserve the list of keys in the main notebook metadata</td>
</tr>
<tr>
<td>allowed_cell_metadata_keys</td>
<td>list</td>
<td>None</td>
<td>Preserve the list of keys in cell level metadata</td>
</tr>
<tr>
<td>clean_ids</td>
<td>bool</td>
<td>True</td>
<td>Remove ids from plaintext reprs?</td>
</tr>
</tbody>
</table>

Jupyter adds a trailing <code></code> to images in cell outputs.
Vscode-jupyter does not.  
Notebooks should be brought to a common style to avoid unnecessary
diffs:

``` python
test_nb = read_nb('../../tests/image.ipynb')
assert test_nb.cells[0].outputs[0].data['image/png'][-1] == "\n" # Make sure it was not converted by acccident
clean_nb(test_nb)
assert test_nb.cells[0].outputs[0].data['image/png'][-1] != "\n"
```

The test notebook has metadata in both the main metadata section and
contains cell level metadata in the second cell:

``` python
test_nb = read_nb('../../tests/metadata.ipynb')

assert {'meta', 'jekyll', 'my_extra_key', 'my_removed_key'} <= test_nb.metadata.keys()
assert {'meta', 'hide_input', 'my_extra_cell_key', 'my_removed_cell_key'} == test_nb.cells[1].metadata.keys()
```

After cleaning the notebook, all extra metadata is removed, only some
keys are allowed by default:

``` python
clean_nb(test_nb)

assert {'jekyll', 'kernelspec'} == test_nb.metadata.keys()
assert {'hide_input'} == test_nb.cells[1].metadata.keys()
```

We can preserve some additional keys at the notebook or cell levels:

``` python
test_nb = read_nb('../../tests/metadata.ipynb')
clean_nb(test_nb, allowed_metadata_keys={'my_extra_key'}, allowed_cell_metadata_keys={'my_extra_cell_key'})

assert {'jekyll', 'kernelspec', 'my_extra_key'} == test_nb.metadata.keys()
assert {'hide_input', 'my_extra_cell_key'} == test_nb.cells[1].metadata.keys()
```

Passing `clear_all=True` removes everything from the cell metadata:

``` python
test_nb = read_nb('../../tests/metadata.ipynb')
clean_nb(test_nb, clear_all=True)

assert {'jekyll', 'kernelspec'} == test_nb.metadata.keys()
test_eq(test_nb.cells[1].metadata, {})
```

Passing `clean_ids=True` removes `id`s from plaintext repr outputs, to
avoid notebooks whose contents change on each run since they often lead
to git merge conflicts. For example:

    <PIL.PngImagePlugin.PngImageFile image mode=L size=28x28 at 0x7FB4F8979690>

becomes:

    <PIL.PngImagePlugin.PngImageFile image mode=L size=28x28>

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L109"
target="_blank" style="float:right; font-size:smaller">source</a>

### process_write

>  process_write (warn_msg, proc_nb, f_in, f_out=None, disp=False)

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L132"
target="_blank" style="float:right; font-size:smaller">source</a>

### nbdev_clean

>  nbdev_clean (fname:str=None, clear_all:bool=False, disp:bool=False,
>                   stdin:bool=False)

*Clean all notebooks in `fname` to avoid merge conflicts*

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
<td>fname</td>
<td>str</td>
<td>None</td>
<td>A notebook name or glob to clean</td>
</tr>
<tr>
<td>clear_all</td>
<td>bool</td>
<td>False</td>
<td>Remove all cell metadata and cell outputs?</td>
</tr>
<tr>
<td>disp</td>
<td>bool</td>
<td>False</td>
<td>Print the cleaned outputs</td>
</tr>
<tr>
<td>stdin</td>
<td>bool</td>
<td>False</td>
<td>Read notebook from input stream</td>
</tr>
</tbody>
</table>

By default (`fname` left to `None`), all the notebooks in
`config.nbs_path` are cleaned. You can opt in to fully clean the
notebook by removing every bit of metadata and the cell outputs by
passing `clear_all=True`.

If you want to keep some keys in the main notebook metadata you can set
`allowed_metadata_keys` in `settings.ini`. Similarly for cell level
metadata use: `allowed_cell_metadata_keys`. For example, to preserve
both `k1` and `k2` at both the notebook and cell level adding the
following in `settings.ini`:

    ...
    allowed_metadata_keys = k1 k2
    allowed_cell_metadata_keys = k1 k2
    ...

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L147"
target="_blank" style="float:right; font-size:smaller">source</a>

### clean_jupyter

>  clean_jupyter (path, model, **kwargs)

*Clean Jupyter `model` pre save to `path`*

This cleans notebooks on-save to avoid unnecessary merge conflicts. The
easiest way to install it for both Jupyter Notebook and Lab is by
running
[`nbdev_install_hooks`](https://nbdev.fast.ai/api/clean.html#nbdev_install_hooks).
It works by implementing a `pre_save_hook` from Jupyter’s [file save
hook
API](https://jupyter-server.readthedocs.io/en/latest/developers/savehooks.html).

## Hooks

------------------------------------------------------------------------

<a
href="https://github.com/fastai/nbdev/blob/master/nbdev/clean.py#L189"
target="_blank" style="float:right; font-size:smaller">source</a>

### nbdev_install_hooks

>  nbdev_install_hooks ()

*Install Jupyter and git hooks to automatically clean, trust, and fix
merge conflicts in notebooks*

See
[`clean_jupyter`](https://nbdev.fast.ai/api/clean.html#clean_jupyter)
and [`nbdev_merge`](https://nbdev.fast.ai/api/merge.html#nbdev_merge)
for more about how each hook works.