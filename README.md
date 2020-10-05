# Material Design Icons Alfred workflow

[Alfred](https://www.alfredapp.com/) workflow to search for [Material Design
Icons](https://material.io/resources/icons/).

## Installation

Download the `mdi.alfredworkflow` file from
[Releases](https://github.com/thirteen37/alfred-mdi/releases) and open it in
Alfred.

## Updating

This script parses the filenames of icons included in the [Material Design Icons
Github repo](https://github.com/google/material-design-icons). Specifically, it
looks for icons that match the pattern `ic_*_48dp.png`.

To update to the latest iconset, just replace the `material-design-icons`
directory with a new copy:

``` sh
git fetch mdi master
git subtree pull --prefix material-design-icons mdi master --squash
```

Assuming `mdi` is set to the Material Design repo.
