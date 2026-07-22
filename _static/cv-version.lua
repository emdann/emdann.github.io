-- cv-version.lua
-- Select CV content for a given version, so one source file (Dann-cv.md)
-- generates both the website and the academic-application PDFs.
--
-- Usage: pandoc ... --lua-filter=_static/cv-version.lua -M version=website
--                                                        -M version=academic
--
-- Content wrapped in a Div or Span with class:
--   .academic-only  -> kept only when version == "academic"
--   .website-only   -> kept only when version == "website"
-- Anything untagged appears in both versions.

function Pandoc(doc)
  local version = "academic"
  if doc.meta.version then
    version = pandoc.utils.stringify(doc.meta.version)
  end

  local function drop(el)
    if el.classes:includes("academic-only") and version ~= "academic" then
      return {}
    end
    if el.classes:includes("website-only") and version ~= "website" then
      return {}
    end
    return nil
  end

  local function drop_span(el)
    local dropped = drop(el)
    if dropped ~= nil then
      return dropped
    end
    -- Trainee names are underlined only in the academic version, where the
    -- explanatory legend appears; keep the plain name text on the website.
    if el.classes:includes("trainee") and version ~= "academic" then
      return el.content
    end
    return nil
  end

  return doc:walk({
    Div = drop,
    Span = drop_span,
  })
end
