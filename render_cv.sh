#!/usr/bin/env bash
# Render both CV versions from the single source _static/Dann-cv.md
#
#   Dann-cv.pdf          -> website version   (no trainee marks, no References,
#                                               excludes the unlinked in-press papers)
#   Dann-cv-academic.pdf -> academic version  (everything)
#
# Content differences are driven by class-tagged Div/Span blocks in the
# markdown, selected by _static/cv-version.lua.
set -euo pipefail
cd "$(dirname "$0")"

SRC=_static/Dann-cv.md
FILTER=_static/cv-version.lua
CSS_MAIN=_static/css/one-column-paged.css
CSS_LETTER=_static/css/us-letter.css
CSS_FA=https://use.fontawesome.com/releases/v5.7.2/css/all.css

render() {
  local version=$1 out=$2
  local extra_css=()
  # The academic version prints on US Letter to match the cover letter and
  # research statement; the website version stays A4.
  [[ $version == academic ]] && extra_css=(--css="$CSS_LETTER")
  pandoc "$SRC" \
    --lua-filter="$FILTER" \
    -M version="$version" \
    --css="$CSS_MAIN" \
    ${extra_css[@]+"${extra_css[@]}"} \
    --css="$CSS_FA" \
    -t html5 \
    --pdf-engine=weasyprint \
    -o "$out"
  echo "wrote $out ($version)"
}

render website  _static/Dann-cv.pdf
render academic _static/Dann-cv-academic.pdf
