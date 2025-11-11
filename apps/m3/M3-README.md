# Milestone-3

## run the replacer
### task7_replacer.py
Replace all b tags with blockquote tags.
```
cd apps/m3
```
```
python task7_replacer.py example.html
```

## run the test
### task7_replacer.py
Replace all b tags with blockquote tags.
```
cd bs4/tests
```
```
python test_soupreplacer_m3.py
```

## Technical Brief
In Milestone 2, `SoupReplacer` allowed simple tag replacements (`og_tag → alt_tag`) during parsing, which avoids extra tree traversal and improves performance for large HTML/XML files.

In Milestone 3, I extended it to support more flexible transformations using functions:
- `name_xformer` to change tag names
- `attrs_xformer` to modify attributes
- `xformer` for general-purpose side effects

These new options make it easy to apply complex changes while parsing, keeping the API efficient and more reusable.

**Recommendation:** Adopt the Milestone 3 API as the main extension. Provide documentation and examples for common transformations, and consider adding prebuilt transformers for frequent use cases. This API improves both flexibility and performance, making BeautifulSoup more powerful for developers.
