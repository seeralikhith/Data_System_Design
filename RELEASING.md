# Releasing a part

The handbook is published one part at a time. Each release does two things:

1. **The site** gains the new part. This happens when `series.yml` marks the part as released and the change reaches `main`.
2. **A GitHub release** announces it. People watching the repository are notified, and the release notes link to the site.

| Part | Folder | Tag | Release notes |
| --- | --- | --- | --- |
| Part 1: Foundations | `docs/part-1-foundations` | `v0.1.0` | `release-notes/part-1.md` |
| Part 2: High-level design (HLD) | `docs/part-2-high-level-design-hld` | `v0.2.0` | `release-notes/part-2.md` |
| Part 3: Low-level design (LLD) | `docs/part-3-low-level-design-lld` | `v0.3.0` | `release-notes/part-3.md` |
| Part 4: Putting it together | `docs/part-4-putting-it-together` | `v1.0.0` | `release-notes/part-4.md` |

## One-time setup

1. Push the repository to GitHub.
2. In the repository, open **Settings → Pages**, and under **Build and deployment** set **Source** to **GitHub Actions**.
3. Open the **Actions** tab and check that the **Publish site** workflow finished. The site is then live at https://seeralikhith.github.io/Data_System_Design/.

## Release a part

The example releases Part 2. Change the part number, folder and tag for the others.

1. **Check the chapters.** Preview every part and read the new one through:

   ```bash
   PREVIEW_ALL=1 .venv/Scripts/python -m mkdocs serve
   ```

   If you changed any diagrams, run `npm run diagrams` and commit the SVG files too.

2. **Mark the part as released.** In `series.yml`, set `released: true` for Part 2.

3. **Update the status.** In `README.md`, change Part 2's status in the series table to **Released**.

4. **Review the release notes** in `release-notes/part-2.md`.

5. **Check the public build:**

   ```bash
   .venv/Scripts/python -m mkdocs build --strict
   ```

6. **Commit and push:**

   ```bash
   git add -A
   git commit -m "Release Part 2: High-level design (HLD)"
   git push origin main
   ```

   Wait for the **Publish site** workflow to finish, then check that Part 2 appears on the site.

7. **Tag the release:**

   ```bash
   git tag -a v0.2.0 -m "Part 2: High-level design (HLD)"
   git push origin v0.2.0
   ```

8. **Create the GitHub release.** On GitHub, open **Releases → Draft a new release**, choose the tag `v0.2.0`, set the title to `Part 2: High-level design (HLD)`, paste in `release-notes/part-2.md`, and select **Publish release**.

   With the GitHub CLI installed, this step is one command instead:

   ```bash
   gh release create v0.2.0 --title "Part 2: High-level design (HLD)" --notes-file release-notes/part-2.md
   ```

## Fix something after a release

Fix it on `main` and push. The site updates on every push, so no new release is needed. For a fix worth announcing, tag a patch release such as `v0.2.1`.
