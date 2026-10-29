# Palau: law history in git

The law of the Republic of Palau as a git history: one file per section or article, one commit per law on the day its change took effect (or, for the Palau National Code, the day the Code Commission's edition first shows it), and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a section; `tools/on.py` gives the text on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `pw/`. Every text comes from the **Palau Code Commission**, the body that "shall compile, revise, codify and publish" the laws of Palau (1 PNC § 1002), and its Publication And Law Access Unit (the "PALAU Office"): the Constitution and the *Palau National Code Annotated* (PNCA) as PDFs with a text layer, from the Code Commission's public Google Drive linked from its site [palaulaw.gov.pw](https://palaulaw.gov.pw/).

**What is in it**

| Folder | Act | Versions | History | Latest version |
| --- | --- | ---: | --- | --- |
| `constitution/` | Constitution of the Republic of Palau | 5 | 1981-01-01 to 2020-11-17 | the Code Commission's text, current as of 13 May 2026 |
| `title-17-penal-code/` | Palau National Code, Title 17: Penal Code | 6 | 1994-09-30 to 2026-09-30 | PNC Title 17, current as of 30 September 2026 |
| `title-01-general-provisions/` | Palau National Code, Title 1: General Provisions | 6 | 1994-09-30 to 2026-09-30 | PNC Title 1, current as of 30 September 2026 |

- **Constitution.** The Code Commission prints the Constitution as adopted (Preamble, Articles I-XV) and appends every amendment after it, as the US Constitution is printed; it does not merge amendments into the Articles. This record keeps that arrangement: the first commit (1 January 1981, art. XV § 1: "This Constitution shall take effect on January 1, 1981") holds the Preamble and Articles; each amendment then arrives as its own file (`amend-01.md` ... `amend-28.md`) on the day its Code Commission note says it was enacted: the First Amendment on 4 November 1992 (the referendum; the note names only RPPL 3-76), the Second to Fifth on 6 November 2004, the Sixth to Twenty-Seventh on 19 November 2008, and the Twenty-Eighth on 17 November 2020. So the Article files keep their 1981 wording; read the amendments for what changed them.
- **Penal Code and General Provisions.** Six full editions of each title from the Code Commission's archive: the PNCA First Edition (through 30 September 1994), the 15th, 16th, 17th and 18th Supplements (14 May 2021, 26 May 2021, 2 June 2022, 25 April 2023) and the current title (30 September 2026). The 1994 Penal Code is the old Trust Territory-derived code; the 2021 edition is the Penal Code enacted by RPPL 9-21 and later laws.

Each folder's `README.md` lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did 17 PNC § 107 say on 2022-01-01? | `python tools/on.py 2022-01-01 title-17-penal-code s-0107` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2022-01-01T23:59:59Z" main -- title-17-penal-code/s-0107.md):title-17-penal-code/s-0107.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2022-01-01T23:59:59Z" main -- title-17-penal-code/s-0107.md; git show "$($r):title-17-penal-code/s-0107.md"` |
| Which law wrote each line? | `git blame title-17-penal-code/s-0621.md` |
| Every change, word by word | `git log -p --word-diff title-17-penal-code/s-0107.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/<key>` (tags `law/<key>`, e.g. `law/rppl-11-028`) |
| What did the Constitution say in 2005? | `python tools/on.py 2005-01-01 constitution` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Pacific/Palau, on its version's day**. The day is also in the `In-force:` trailer, which the tools read.
- **Constitution:** the Constitution's own effective date, and each amendment's enactment date from the Code Commission's "Source" note (art. XIV: an amendment takes effect when approved, or on certification of the results). The First Amendment's date comes from the public record of the 4 November 1992 referendum, because the Code Commission's note gives no date.
- **Palau National Code:** the source gives no in-force date per change, only editions. Each version is dated by its edition's **"through" date**, the day to which the Code Commission certifies the edition as its approved version (the First Edition's Certificate of Authenticity: "through September 30, 1994"). A change dated 14 May 2021 therefore took effect on some day after 30 September 1994 and by 14 May 2021. That is the main limit of this record.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day; use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on its day and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Word check against the official PDFs:** every paragraph of every PNC edition and of the current Constitution is searched for, word for word, in a second, independent text extraction of the same PDF (poppler's `pdftotext`; the build itself reads the PDFs with PyMuPDF). Of 22,971 paragraphs, 3 are not found as runs of words, all explained by layout: a table of senatorial districts (Constitution art. XV § 13), and two words broken across a page foot ("de-listing", "sixty-day").
- **Credits** come only from the Code Commission's "Source(s)" notes. Anything they do not explain is committed by the publisher and labelled "unexplained": for example the Code Commission's 2022 renaming of "Minister of Health" to "Minister of Health and Human Services" and its 2026 restyling of the Penal Code ("this chapter" to "this Act", lower-case list items, renumbered designations).
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Constitution:** the first commit is the Constitution itself; each amendment's commit is that amendment.
- **PNC titles:** the first commit is the oldest version available (the 1994 First Edition), credited to the publisher. A section that changed between two editions is credited to the RPPL(s) (Republic of Palau Public Laws) that its "Sources" note names in the later edition and not in the earlier. When several are named the section goes in the commit of the highest-numbered one, which names them all. RPPL dates are not in the source, so these laws carry no enactment date.
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words each change made.

## What it does not show

- **The true in-force day of PNC changes** (see Dates), and the **3rd to 14th Supplements** (1998-2020), which are not in the Code Commission's archive: every change between the 1994 First Edition and the 15th Supplement of 2021 is folded into the 2021 commits, including the replacement of the whole Penal Code. The 1st and 2nd Supplements (1996, 1997) are pocket parts that hold only changed sections and are not used.
- **The Palauan text.** The Constitution is official in Palauan and English; the Code Commission publishes both. This record holds the English text.
- **Annotations.** The Code Commission's notes (Sources, Amended, Repealed, Notes, Cross-references, Commission Comments, Supreme Court Cases), running heads, page feet, chapter tables of contents and Division, Chapter and Subchapter headings are left out; each section file starts with its own heading. Spacing, quotes and dashes are normalised. The words of the law are not changed.
- **Scanned laws.** Session laws (RPPL) are not replayed; many are scans, and nothing here reads text off a page image (no OCR).

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code splits titles into sections and credits changes; Lexifina's code writes `corpus.json`. Lexifina's code is the word check.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Palau Code Commission](https://palaulaw.gov.pw/) / Publication And Law Access Unit: [public Google Drive](https://drive.google.com/drive/folders/1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox) | The Constitution (English and Palauan), PNC titles 1-42 current as of 30 September 2026, RPPL, regulations; Archives: PNCA First Edition (1994) and Supplements 1, 2 and 15-18 | All text, dates and credits |
| [palaulaw.gov.pw](https://palaulaw.gov.pw/) (Code Commission) | About page: "a project of the Republic of Palau Code Commission ... free, open, and reliable access to the laws of the Republic of Palau" | Provenance |
| [PALAU Office transition report (2020)](https://www.palaugov.pw/wp-content/uploads/2020/12/Publication-and-Law-Access-Unit.pdf), palaugov.pw | The PALAU Office, under the Code Commission, keeps the laws and PNCA supplements on Google Drive | Provenance |

The Drive's "Disclaimer" file is the Judiciary Branch website disclaimer together with 1 PNC § 1002 and the PALAU Law Search CD disclaimer, and its "Palau Law Website Link" file points to palaulaw.gov.pw. The Judiciary's old host palausupremecourt.net no longer answers; its Internet Archive copies hold court decisions and rules but no Code. Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). The PNC front matter reads "Copyright © Republic of Palau, Publication And Law Access Unit". The Code Commission publishes the texts for free public access and states that they "are for informational purposes only and do not constitute official legal advice." No licence to republish is given, so this repository is private. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice. The laws of Palau are published in English (the Constitution also in Palauan), so there is no summary in another language.
