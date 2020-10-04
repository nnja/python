Local setup instructions:

1. Install Hugo version v0.54.0 for the site to render properly
1. clone hugo learn theme from https://github.com/matcornic/hugo-theme-learn, update `themesdir` in config.toml
1. `cd python` then, `hugo server -D` to run local server

Note: the file and folder names don't contribute to order, and may not always be accurate. Sorted by chapter and individual page weight.

If you move things around or delete chapters, you may have to restart the server for the chapters to appear correctly.

How to use the theme: https://learn.netlify.com/en/cont/
More about theme shortcodes: https://learn.netlify.com/en/shortcodes/

use `git lfs` for tracking binary types.

```bash
$ git lfs track "*.psd"
git add .gitattributes
```

Currently tracked types:
 - .png
 - .jpg
 - .jpeg
 - .pdf
 - .mp4
 - .gif