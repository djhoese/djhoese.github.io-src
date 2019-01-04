# Notes on creating the site

```
$ conda create -n pelican-blog python=3.6 jupyter notebook pelican markdown ghp-import
$ source activate pelican-blog
$ pelican-quickstart
$ mkdir plugins
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule add git://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
```
