# Blogging


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Background

Blogging with notebooks can offer a dramatic quality of life improvement
over writing in Markdown, especially for blog posts that contain code.
Previously, there were no static site generators that supported Jupyter
Notebooks as a first-class authoring medium. This previously led us to
create [fastpages](https://github.com/fastai/fastpages) (now
deprecated), which extended [Jekyll](https://jekyllrb.com/) to enable
blogging directly with Jupyter.

## Enter Quarto

However, there now exists [Quarto](https://quarto.org/), a wonderful
publishing system with rich support for authoring via Jupyter Notebooks.

Some helpful resources on getting started with Quarto:

- [The Quarto Homepage](https://quarto.org/)
- [Creating A Blog With
  Quarto](https://quarto.org/docs/websites/website-blog.html): This page
  helps you get started with creating a blog.
- [A Gallery of Quarto Sites](https://quarto.org/docs/gallery/): Good
  reference examples of using Quarto.
- [The Quarto Website](https://github.com/quarto-dev/quarto-web): The
  Quarto website is built with Quarto and they use some of its advanced
  functionality. It is instructive to look through this project to
  understand how Quarto works.

<div>

> **You don’t need nbdev to blog with notebooks**
>
> You do not need to use nbdev to create a blog with notebooks. However,
> you may wish to:
>
> - Incorporate a blog in your nbdev project’s website
> - Use some nbdev functionality in your blog (testing, exporting etc)
>
> We will discuss these subjects in this article.

</div>

## Migrating from fastpages

If you previously had a fastpages site, we offer some utilities to help
migrate you to Quarto. **The migration is not holistic: you will likely
have to manually correct some things that we are not able to automate.**

Instructions:

1.  [Install Quarto](https://quarto.org/docs/get-started/)

2.  Create a new repo or directory to migrate your blog to

3.  In this new repo, create a quarto blog and install required
    extensions with the following terminal commands. This will create a
    minimal project structure for you:

``` bash
quarto create-project --type website:blog .
quarto install extension quarto-ext/video
```

5.  Your new repo will have a `posts/` directory. This is where you will
    copy all of your notebook and markdown posts from fastpages. For
    example, let’s say your fastpages blog repo is in a sibling
    directory located at `../blog/`, you would copy all the relevant
    posts like this:

<div>

> **Important**
>
> Make sure you are in root of your quarto directory before executing
> the below commands. Furthermore, change the commands as appropriate
> depending on the location of your fastpages repo relative to your
> current directory.

</div>

``` bash
cp -r ../blog/_notebooks/* posts
cp -r ../blog/_posts/* posts
```

6.  Copy all images associated with your posts into the `posts/`
    directory. We have to get our images from several places (due to the
    way Jekyll and fastpages work):

``` bash
cp ../blog/images/* posts
cp -r ../blog/images/copied_from_nb/* posts/
```

7.  Make your posts Quarto compatible with the following command:

``` bash
nbdev_migrate --path posts
```

<div>

> **What does
> [`nbdev_migrate`](https://nbdev.fast.ai/api/migrate.html#nbdev_migrate)
> do?**
>
> [`nbdev_migrate`](https://nbdev.fast.ai/api/migrate.html#nbdev_migrate)
> does the following things:
>
> #### For notebooks
>
> - Migrates markdown front matter to raw cell front matter [as
>   described here](../api/migrate.ipynb#migrateproc).
> - nbdev v1 directives are automatically converted to [Quarto
>   directives](../explanations/directives.ipynb). Note that we convert
>   everything to Quarto directives (nbdev-specific directives are not
>   relevant for this context)
> - Markdown shortcut for embedding youtube videos and callouts are
>   automatically converted to work with Quarto.
>
> #### For markdown and notebooks
>
> - Automatically creates [link
>   aliases](https://quarto.org/docs/reference/formats/html.html#website)
>   so that old links will not break. Jekyll automatically generates
>   URLs differently than Quarto, so this ensures that the Jekyll way is
>   aliased.
> - Automatically corrects image paths
> - Makes front matter compatible with Quarto by changing field names
>   and values where necessary

</div>

8.  Update the following files:

- `./.gitignore`: we suggest adding`_site/` as well as dot files `.*`
- `./about.qmd`: Add some information about yourself.
- `./profile.jpg`: optionally change the profile picture.

9.  Preview your site with the command `quarto preview`, and make any
    necessary adjustments and fix for broken links or Jekyll shortcodes
    (things with `{% ... %}`) that need to be converted to Quarto.
    Search the [the Quarto documentation](https://quarto.org/) if you
    need help locating specific Quarto features.

### Configuration options: fastpages vs. Quarto

fastpages (which is based on Jekyll) and Quarto offer different options
and configurations for individual posts and at a site level. The tables
below enumerate some of the most important features of fastpages and how
they map to Quarto. Each link in the last column is specific to the
relevant feature.

#### Post-level options

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Jekyll Front Matter</th>
<th>Quarto</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>toc: false</td>
<td>Same</td>
<td>There are more options in the <a
href="https://quarto.org/docs/reference/formats/pdf.html#table-of-contents">Quarto
docs</a></td>
</tr>
<tr>
<td>badges: true</td>
<td>n/a</td>
<td>No support yet</td>
</tr>
<tr>
<td>comments: true</td>
<td>see notes</td>
<td><a
href="https://quarto.org/docs/output-formats/html-basics.html#commenting">Quarto
docs</a></td>
</tr>
<tr>
<td>categories: [fastpages, jupyter]</td>
<td>Same</td>
<td><a
href="https://quarto.org/docs/websites/website-listings.html#categories">Quarto
docs</a></td>
</tr>
<tr>
<td>image: images/some_folder/your_image.png</td>
<td>Same</td>
<td><a
href="https://quarto.org/docs/websites/website-listings.html#listing-fields">Quarto
docs</a></td>
</tr>
<tr>
<td>hide: false</td>
<td>draft: true</td>
<td><a
href="https://quarto.org/docs/websites/website-blog.html#drafts">Quarto
docs</a></td>
</tr>
<tr>
<td>search_exclude: true</td>
<td>see notes</td>
<td><a
href="https://quarto.org/docs/websites/website-search.html#disabling-search">Quarto
docs</a></td>
</tr>
<tr>
<td>title</td>
<td>Same</td>
<td> </td>
</tr>
<tr>
<td>description</td>
<td>Same</td>
<td> </td>
</tr>
<tr>
<td>sticky_rank</td>
<td>Not supported</td>
<td><a
href="https://quarto.org/docs/websites/website-listings.html#sorting-items">Quarto
docs</a></td>
</tr>
</tbody>
</table>

#### Site-level options

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Jekyll site config</th>
<th>Quarto</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>title</td>
<td>see notes</td>
<td><a href="https://quarto.org/docs/websites/#getting-started">Quarto
docs</a></td>
</tr>
<tr>
<td>description</td>
<td>see notes</td>
<td><a href="https://quarto.org/docs/websites/website-tools.html">Quarto
docs</a></td>
</tr>
<tr>
<td>github_repo</td>
<td>see notes</td>
<td><a
href="https://quarto.org/docs/websites/website-navigation.html#top-navigation">Quarto
docs</a></td>
</tr>
<tr>
<td>url</td>
<td>n/a</td>
<td>Don’t need this</td>
</tr>
<tr>
<td>baseurl</td>
<td>n/a</td>
<td>Don’t need this</td>
</tr>
<tr>
<td>twitter_username</td>
<td>search page in notes for “twitter”</td>
<td><a
href="https://quarto.org/docs/websites/website-navigation.html#top-navigation">Quarto
docs</a></td>
</tr>
<tr>
<td>use_math</td>
<td>see notes </td>
<td><a
href="https://quarto.org/docs/output-formats/html-basics.html#latex-equations">Quarto
docs</a></td>
</tr>
<tr>
<td>google_analytics</td>
<td>website: google-analytics: “UA-XXXXXXXX”</td>
<td><a
href="https://quarto.org/docs/websites/website-tools.html#google-analytics">Quarto
docs</a></td>
</tr>
<tr>
<td>show_image</td>
<td>n/a</td>
<td><a
href="https://quarto.org/docs/reference/formats/html.html#layout">Quarto
docs</a></td>
</tr>
<tr>
<td>show_tags</td>
<td>see title-block-categories of page in notes</td>
<td><a
href="https://quarto.org/docs/reference/formats/html.html#layout">Quarto
docs</a></td>
</tr>
<tr>
<td>pagination</td>
<td>website: page-navigation: true</td>
<td><a
href="https://quarto.org/docs/websites/website-navigation.html#page-navigation">Quarto
docs</a></td>
</tr>
<tr>
<td>annotations</td>
<td>comments: hypothesis: …</td>
<td><a
href="https://quarto.org/docs/output-formats/html-basics.html#commenting">Quarto
docs</a></td>
</tr>
</tbody>
</table>

## Publishing your blog

<div>

> **Warning**
>
> *This section is for stand-alone blogs that are not part of a nbdev
> documentation site. If you want to create a blog within a nbdev
> documentation site, see [this
> section](#creating-a-blog-within-a-nbdev-project).*

</div>

You can publish your site with the `quarto publish` command. See [the
docs](https://quarto.org/docs/publishing/) for more details.

<div>

> **GitHub Pages**
>
> If using GitHub Pages, commit your files to GitHub before publish your
> site. **No GitHub Actions are needed**, you can use `quarto publish`
> instead. If you want to automate your workflow with GitHub Actions,
> you can follow [these
> instructions](https://quarto.org/docs/publishing/quarto-pub.html#github-action)

</div>

## Creating a blog within a nbdev project

In addition to a stand-alone blog that you might build with Quarto, you
might want to include a blogging site in your nbdev project. This
website has [a blog](../blog/) as well! The easiest way to implement a
blog is to emulate the directory structure of [this
folder](https://github.com/fastai/nbdev/tree/master/nbs/blog). The
general steps are:

1.  **Create a `blog/` directory in your notebooks folder.**
2.  **Create a `index.qmd` file in the root of the `blog/` directory.**
    Here [is an
    example](https://github.com/fastai/nbdev/blob/master/nbs/blog/index.qmd).

The frontmatter the `index.qmd` file signals to Quarto that you intend
to create a blog. For example, here is [our front
matter](https://github.com/fastai/nbdev/blob/master/nbs/blog/index.qmd):

``` yaml
---
title: nbdev Blog
subtitle: News, tips, and commentary about all things nbdev
listing:
  sort: "date desc"
  contents: "posts"
  sort-ui: false
  filter-ui: false
  categories: true
  feed: true
page-layout: full
---
```

The `listing:` field specifies how you want to structure your blog. Feel
free to copy ours as-is, but we encourage you to [consult the
documentation](https://quarto.org/docs/websites/website-blog.html) for
additional options.

3.  **Create a link to your blog on your site’s navbar so people can
    find it**: To add a link to your blog on your site’s navbar, you
    must edit the navbar section of `_quarto.yml` to include a link to
    your blog’s listing page, which is `blog/index.qmd` in our example.
    For nbdev, the relevant part of our
    [`_quarto.yml`](https://github.com/fastai/nbdev/blob/master/nbs/_quarto.yml)
    file looks like this: <span class="column-margin margin-aside">The
    yaml snippet shown below is an abbreviated version of nbdev’s
    [`_quarto.yml`](#%20An%20abbreviated%20version%20of%20https://github.com/fastai/nbdev/blob/master/nbs/_quarto.yml)
    file.</span>

``` yaml
website:
  navbar:
    left:
      - text: "Blog"
        href: blog/index.qmd
```

You can read more about the navbar in the [Quarto
docs](https://quarto.org/docs/websites/website-navigation.html#top-navigation).

4.  **Create a folder for each blog post**: This is not strictly
    required, but we recommend this as a way to keep your blog posts and
    related assets (pictures, videos etc) organized.

5.  **Create your first blog post**: You can emulate our example or
    create your own. In each folder, create a `index.qmd` or
    `index.ipynb` file. You can also put images and related assets in
    the same folder.

### Folder structure

Below is an overview of the general folder structure for a blog within a
nbdev site:

    nbs/blog
    ├── index.qmd
    └── posts
        ├── 2022-07-28-nbdev2
        │   ├── cover.png
        │   ├── index.qmd
        │   ├── ...
        └── 2022-08-25-jupyter-git
            ├── friendly-conflict.png
            ├── index.qmd
            └── ...
        ...

- `nbs/blog`: this is the folder inside your notebook folder that
  contains the blog.
- `index.qmd`: this is at the root of your blog folder and is the
  listings page for your blog.
- `posts/`: this a subdirectory for each blog post.
- `YYYY-MM-DD-.../index.{qmd,ipynb}`: this is where you author the
  content of each individual blog post.

### Special considerations for nbdev blogs

In contrast to standalone Quarto blogs, when you embed a blog in a nbdev
website there are the following differences:

- You can use all [nbdev directives](../explanations/directives.ipynb)
  in addition to Quarto ones. All nbdev features will be available in
  your nbdev blog in the same way they work for other pages.
- Your site will automatically deploy with GitHub Actions or whatever
  deployment mechanism you have for your nbdev site, so you do not have
  to use `quarto publish`.

## Using nbdev features in blogs outside nbdev projects

<div>

> **Warning**
>
> *This section is for stand-alone blogs that are not part of a nbdev
> documentation site. If you create a blog within a nbdev documentation
> site, all nbdev features will automatically work.*

</div>

If you create a standalone blog with Quarto, a limited number of nbdev
features can still assist you. For example, we recommend installing
[Jupyter git hooks](pre_commit.ipynb). A list of nbdev features
available to you are listed in [this article](modular_nbdev.ipynb).

## Creating A New Blog Site From Scratch

You can use the [quarto CLI](https://quarto.org/docs/get-started/) to
setup a new blog project called `myblog` with the following command:

``` bash
quarto create-project myblog --type website:blog
```

You can then preview your blog project with `quarto preview`. You can
also publish your blog using the
[`quarto publish`](https://quarto.org/docs/publishing/quarto-pub.html#publish-command)
command.

<div>

> **Adding a notebook blog post**
>
> To add a notebook blog post to a blog project created with the above
> commands, you can add an additional folder under `posts/` and name the
> notebook `index.ipynb`. You will see existing example blog posts that
> are `index.qmd` files in sibling folders you can look at for examples.
> You will need to add [yaml front
> matter](https://quarto.org/docs/tools/jupyter-lab.html#yaml-front-matter)
> to the first cell of your notebook in the form of a raw cell.

</div>

For more information about creating a blog with Quarto, see [this
guide](https://quarto.org/docs/websites/website-blog.html).

# FAQ

1.  **Do I need to migrate from fastpages?**

    No you do not. However we will not be actively supporting fastpages
    going forward.

2.  **Will migrating from fastpages to Quarto take lots of manual
    effort?**

    You will have to do some manual work to make sure everything looks
    and works the same, including converting Jekyll shortcodes to
    equivalent Quarto commands. However, we have automated the biggest
    aspects for you. Please see [Migrating from
    fastpages](#migrating-from-fastpages) for instructions.

3.  **I cannot find something in Quarto that does what
    `#collapse_output` did in fastpages**

    Correct, this is a feature that isn’t supported in Quarto yet.

4.  **Why am I seeing `{% twitter ...%}` and `{% fn_detail ... %}` and
    other `{%...%}` commands in my Quarto blog posts?**

    These are Jekyll shortcodes that you will have to manually migrate
    to Quarto. For example with the twitter embeds, you can insert the
    appropriate HTML as [recommended by
    Twitter](https://help.twitter.com/en/using-twitter/how-to-embed-a-tweet#:~:text=Click%20the%20icon%20located%20within,by%20clicking%20set%20customization%20options).
    For footnotes, you can see [these
    docs](https://quarto.org/docs/authoring/footnotes-and-citations.html).
    For other items, you should search the [Quarto
    docs](https://quarto.org/docs/websites/website-blog.html) for how to
    enable your desired result.

5.  **I created a new blog post and used `#| hide` but the cell is still
    showing. What is wrong?**

    You must use Quarto directives, not nbdev-specific ones. See the
    difference between the two [in these
    docs](../explanations/directives.ipynb). This is because you are
    blogging with Quarto, not nbdev. The exception to this is you have a
    blog site in your nbdev project – in that case, nbdev-specific
    directives will work.

6.  **How do I enable comments on my blog posts?**

    In general, Quarto offers all of the same features and much more
    than fastpages did, including comments. If you search the [Quarto
    docs](https://quarto.org/) for comments, you will see a [page for
    enabling
    comments](https://quarto.org/docs/output-formats/html-basics.html#commenting).

7.  **How do I sort and hide posts? What about the publishing date since
    that’s not in the filename?**

    See the Quarto docs on [creating a
    blog](https://quarto.org/docs/websites/website-blog.html) as well as
    [listing
    pages](https://quarto.org/docs/websites/website-listings.html).

8.  **How do I customize my site?**

    See the [Quarto
    docs](https://quarto.org/docs/websites/website-blog.html)

9.  **How do I do set up RSS Feeds and add particular features to my
    site?**

    See the [Quarto
    docs](https://quarto.org/docs/websites/website-blog.html)

10. **What does nbdev have to do with Quarto?**.

    For just blogging, nothing! You can use Quarto for blogging without
    worrying about nbdev. In the past, we maintained a nbdev related
    project called [fastpages](https://github.com/fastai/fastpages), and
    are recommending that people migrate to Quarto if possible.
    Furthermore, nbdev is built on top of Quarto which means much of the
    functionality is similar. Finally, you can incorporate blogs into a
    nbdev project site, which we discuss in [this
    section](#creating-a-blog-within-a-nbdev-project).

11. **For stand alone blogs, why are you directing us to Quarto, can I
    just use nbdev?**

    nbdev is built on top of Quarto. For the purposes of blogging,
    adding nbdev is of little additional benefit if all you want to do
    is to blog. We decided to keep things simple and let people use
    Quarto directly instead of trying to abstract aspects of Quarto for
    blogging. Furthermore, having some knowledge of Quarto can be very
    helpful in using nbdev!. Lastly, you can still use some nbdev
    features in your blog, which are listed in [this
    article](modular_nbdev.ipynb).