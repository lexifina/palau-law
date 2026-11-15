# Palau: law history in git


The law of Palau as a git history: one file per section or article, one commit per law on the day its change took effect (for the Palau National Code, the day of the Code Commission's edition that first shows it), and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a section; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Palau's national law, which global-law reads at `palau/national/acts/`.

**What is in it now:** the Constitution of the Republic of Palau with its 28 amendments, in 5 versions from 1981 to 2020; and two titles of the Palau National Code, Title 1 (General Provisions, 64 sections) and Title 17 (the Penal Code, 627 sections), each in 6 editions from 1994 to 2026. Their changes are credited to the amendments and to 19 Republic of Palau Public Laws (RPPL). [`REPRODUCE.md`](REPRODUCE.md) lists each act with its versions; [`data/laws.csv`](data/laws.csv) lists every law the record names.

Each act has its own folder, one file per section, and a `README.md` listing its provisions and their changes (`title-17-penal-code/s-0107.md` is 17 PNC § 107, time limitations). The Code Commission prints the Constitution as adopted, with its amendments after it, and so does this record: each amendment is a file of its own in `constitution/` (`amend-01.md` to `amend-28.md`), and the Article files keep their 1981 wording.

The text is in English, as the Code Commission prints it in its PDFs. The Constitution's Palauan text is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to section 107 of the Penal Code | `git log -p --word-diff -- title-17-penal-code/s-0107.md` |
| Which law wrote each line of section 107? | `git blame title-17-penal-code/s-0107.md` |
| Every version of section 107, with its day and the law credited | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- title-17-penal-code/s-0107.md` |
| Section 107 as it stood on 1 January 2022 | `python tools/on.py 2022-01-01 title-17-penal-code s-0107` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Palau law](https://global-law.lexifina.com/v1/try_claude?country=palau)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=palau)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=theft&jurisdictions=palau)**: a search of Palau law for "theft", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add palau/national/acts
python3 tools/law.py show 2026-01-01 palau/national/acts/title-17-penal-code/s-0107.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Pacific/Palau, on its version's day, and carries it in its `In-force:` trailer:

- for the Constitution, 1 January 1981 (art. XV § 1: "This Constitution shall take effect on January 1, 1981"), and for each amendment the day its Code Commission "Source" note says it was enacted;
- for the First Amendment, whose note names only RPPL 3-76, 4 November 1992, the day of the referendum that approved it, from the public record;
- for the Palau National Code, which gives no in-force day for a change, the "through" date of the edition that first shows it: the First Edition (30 September 1994), the 15th to 18th Supplements (14 May 2021, 26 May 2021, 2 June 2022, 25 April 2023) and the current titles (30 September 2026). A change dated 14 May 2021 took effect on some day after 30 September 1994 and by 14 May 2021.

The Constitution's first commit is credited to the Constitution and each amendment's to that amendment. A Code title's first version, the 1994 First Edition, is the oldest version available, credited to the publisher; a later change is credited to the RPPL that the section's "Sources" note names in the later edition and not in the earlier (the highest-numbered, where it names several), and to the publisher, labelled "unexplained", where no note explains it.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus: 17 versions of 3 acts, 0 mismatches (see [`REPRODUCE.md`](REPRODUCE.md)).
- Every paragraph of every Code edition and of the current Constitution is searched for, word for word, in a second, independent text extraction of the same PDF: of 22,971 paragraphs, 3 are not found, all explained by layout (a table in art. XV § 13 and two words broken across a page foot).
- It also checks git's own rules: no merge commits, no commit date that goes backwards, nothing dated after the build, and every commit's trailers parse.

## What it does not show

- **Most Palau law.** Only the Constitution and two of the Code's 42 titles: no other title, no regulations, no session laws as enacted and no case law.
- **The 3rd to 14th Supplements** (1998 to 2020), which are not in the Code Commission's archive: every change between the 1994 First Edition and 2021, including the replacement of the whole Penal Code by RPPL 9-21, falls on the 2021 commits.
- **The true in-force day of a Code change** (see Dates).
- **The Code Commission's annotations** (Sources, Notes, Cross-references, Commission Comments, Supreme Court Cases), tables of contents and Division, Chapter and Subchapter headings; each section file starts with its own heading.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Palau Code Commission](https://palaulaw.gov.pw/) (Publication And Law Access Unit), its [public Google Drive](https://drive.google.com/drive/folders/1o9b7uIAaNl7qj_yfILpbgstBp6nW90Ox) | The body that compiles and publishes the laws of Palau (1 PNC § 1002): the Palau National Code Annotated and the Constitution, as PDFs | yes, the Code's First Edition (1994) and 15th to 18th Supplements in its archive; the Constitution in one current text | All text, dates and credits |

## Licence

See [`LICENSE`](LICENSE). The texts come from the Code Commission, which publishes them for free public access ("Copyright © Republic of Palau, Publication And Law Access Unit"); no licence to republish is given. Lexifina's arrangement, commit messages, tables and tools are dedicated to the public domain under CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
