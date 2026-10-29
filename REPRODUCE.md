# How this repository was made (Palau)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Palau Code Commission / Publication And Law Access Unit: public Google Drive ("Palau Law"), folder 1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox | <https://drive.google.com/drive/folders/1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox> | 2026-10-29 | 73 | Copyright Republic of Palau, Publication And Law Access Unit; published by the Code Commission for free public access (palaulaw.gov.pw About page). Informational, not legal advice. |
| Palau Code Commission: Palau Legal Information Access website | <https://palaulaw.gov.pw/> | 2026-10-29 | 2 | About page: a project of the Republic of Palau Code Commission "to provide free, open, and reliable access to the laws of the Republic of Palau"; "the official digital repository for the legal corpus of Palau". |
| Republic of Palau National Government (palaugov.pw): Publication And Law Access Unit transition report (2020) | <https://www.palaugov.pw/wp-content/uploads/2020/12/Publication-and-Law-Access-Unit.pdf> | 2026-10-29 | 1 | Government publication |
| Internet Archive Wayback Machine CDX (probe only) | <https://web.archive.org/cdx/search/cdx> | 2026-10-29 | 0 | Internet Archive terms of use |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Palau | 5 | 1981-01-01 to 2020-11-17 |
| `title-17-penal-code` | Palau National Code, Title 17: Penal Code | 6 | 1994-09-30 to 2026-09-30 |
| `title-01-general-provisions` | Palau National Code, Title 1: General Provisions | 6 | 1994-09-30 to 2026-09-30 |

The build made 60 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 50 | one law on its in-force day |
| 7 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 57 laws in the record.
- 61 tags.

## Dates

Each commit is dated at noon (Pacific/Palau) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: ROP Const. art. IX, § 15: "A bill adopted by each house of the Olbiil Era Kelulau shall be presented to the President and shall become law when signed by the President"; constitutional amendments take effect when approved (art. XIV, § 1) or, under a later amendment, on the date the election results are certified unless the amendment prescribes a date. https://drive.google.com/file/d/1hPQSUW9yNyZhFzwSgdRUQTeVRhkE1W-T/view

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/palau-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `4082eac82c7d2f70055215b89f78c9665ed849bcfbd82d0dfa89d8419e9a0f17` (4973552 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `e8822a073783c2bb3a79ff5c01e230beb33e0d48` |
| parse.py | `2957fcba14aed3efe48147791180c5278d184953` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

Not yet run for this build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Constitution: version 1 is dated 1981-01-01 (art. XV: "This Constitution shall take effect on January 1, 1981"); its text is the Preamble and Articles as the Code Commission prints them, credited to the Constitution itself.
- Constitution: each amendment is a file of its own (amend-NN), added on the day its Code Commission "Source" note says it was enacted (2004-11-06, 2008-11-19, 2020-11-17); the Code Commission prints amendments after the Articles rather than merging them into the Articles, and this record keeps that arrangement, so the Article files keep their 1981 wording.
- Constitution: the First Amendment's note gives only "RPPL 3-76 § 3"; it is dated 1992-11-04, the referendum that approved it (art. XIV § 1: effective "when approved"); that date comes from the public referendum record, not from the Code Commission.
- Constitution: Code Commission annotations ("Amended", "Repealed", "Notes", "Supreme Court Cases", "Source") are editorial and are not part of the provision files.
- PNC titles: each version is one full edition of the title from the Code Commission archive (1st Edition through 1994-09-30; 15th-18th Supplements; current as of 2026-09-30) and is dated by that edition's "through" date, the day the Commission certifies the text as current; the true in-force day of each change is earlier and is not given by the source.
- PNC titles: the 1st and 2nd Supplements (1996, 1997) are pocket parts with only the changed sections and the 3rd-14th Supplements are not in the archive, so the record jumps from the 1994 First Edition to the 15th Supplement (2021-05-14).
- PNC titles: a section that changed between editions is credited to the RPPL(s) its "Sources" note names in the later edition and not in the earlier; if the note names none, the change is the publisher's and committed as unexplained. RPPL enactment dates are not in the source, so laws carry no enacted date.
- PNC titles: RPPL keys are zero-padded (rppl-09-021 for RPPL 9-21) so that, with no enactment dates in the source, the builder orders laws named together by their number (Olbiil Era Kelulau, then law).
- PNC titles: Code Commission annotations (Sources, Notes, Cross-references, Supreme Court Cases, Commission Comments) and the chapter tables of contents are not part of the section files.
- Source choice: PacLII and AustLII were not used (AustLII terms forbid scraping and dataset use). Every text comes from the Palau Code Commission's own publication channel.
- Language: the Constitution is official in English and Palauan; the English version is built (the Code Commission publishes both).

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py, layout.py and parse.py and found the sources. No model wrote, summarised or corrected any legal text; every provision is extracted by code from the publisher's PDF text layer.
