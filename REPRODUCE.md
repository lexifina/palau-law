# How this repository was made (Palau)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Palau Code Commission / Publication And Law Access Unit: public Google Drive ("Palau Law"), folder 1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox | <https://drive.google.com/drive/folders/1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox> | 2026-10-29 | Copyright Republic of Palau, Publication And Law Access Unit; published by the Code Commission for free public access (palaulaw.gov.pw About page). Informational, not legal advice. |
| Palau Code Commission: Palau Legal Information Access website | <https://palaulaw.gov.pw/> | 2026-10-29 | About page: a project of the Republic of Palau Code Commission "to provide free, open, and reliable access to the laws of the Republic of Palau"; "the official digital repository for the legal corpus of Palau". |
| Republic of Palau National Government (palaugov.pw): Publication And Law Access Unit transition report (2020) | <https://www.palaugov.pw/wp-content/uploads/2020/12/Publication-and-Law-Access-Unit.pdf> | 2026-10-29 | Government publication |
| Internet Archive Wayback Machine (looked up, not used) | <https://web.archive.org/cdx/search/cdx> | 2026-10-29 | Internet Archive terms of use |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

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

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `cff2119bdfa922b01d0c413a0a6f3a145dc3849169b05d25ee9b7c0fae70e057` (4974297 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

17 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

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
- Source choice: PacLII and AustLII were not used (AustLII's terms forbid dataset use). Every text comes from the Palau Code Commission's own publication channel.
- Language: the Constitution is official in English and Palauan; the English version is built (the Code Commission publishes both).
- 17 PNC § 4727 (chemical weapons schedule): the 15th Supplement's text layer renders the ≤ sign as '#', the 16th as nothing; the difference is committed as unexplained on 2021-05-26 and is a typesetting artefact, not a change in the law.
- Word check: every paragraph of every PNC edition and of the current Constitution was found in an independent pdftotext extraction of the same PDF, except 3 explained by layout (Constitution art. XV § 13 table; 17 PNC § 3348 and § 513 words broken across a page foot); results in verification.json.
- Paragraphs in PNC sections are split only where an enumerator such as (a), (1), (A) or (iv) follows the end of a clause, because the typeset and the Word-exported editions space paragraphs differently; unnumbered paragraphs inside one section are joined on one line.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code and found the sources. No model wrote, summarised or corrected any legal text; every provision is extracted by code from the publisher's PDF text layer.
