```
sphinx-autobuild . _build/html
```

To render CV:
```
pandoc _static/Dann-cv.md -o _static/Dann-cv.pdf --css=_static/css/one-column-paged.css --css=https://use.fontawesome.com/releases/v5.7.2/css/all.css -t html5
```