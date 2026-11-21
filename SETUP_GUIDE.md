# Free Lite funnel – setup guide

**Goal:** people click your post → land on your page → fill a Google Form → get the free Lite file → some buy the full pack.

```
Facebook group / LinkedIn post
        │
        ▼
Landing page  (GitHub Pages, free)
        │
        ▼
Google Form   (collects name + email + consent → saves to a Google Sheet)
        │
        ▼
"Thank you" message with the Lite download link  (file hosted on GitHub Pages)
        │
        ▼
3 follow-up emails → full pack  (emails/follow-up-emails.md)
```

Total time: about 45 to 60 minutes the first time.

## What is in this kit

| Item | Purpose |
| --- | --- |
| `site/` | The landing page, images and the Lite file. This is what goes on GitHub. |
| `setup.py` | Fills in your links and patches the store link into the Lite workbook. |
| `google-form/CreateForm.gs` | A script that builds the Google Form and the responses Sheet for you. |
| `emails/follow-up-emails.md` | Three follow-up emails. |

---

## Step 1 – Decide your names (2 minutes)

You need two names. Write them down:

- **GitHub username:** for example `juandelacruz`
- **Repository name:** for example `scurve-lite`

Your page will then be at `https://USERNAME.github.io/REPO/` and the Lite file at
`https://USERNAME.github.io/REPO/downloads/S-Curve_Gantt_Planner_Vol2_FREE_LITE.xlsx`
(replace `USERNAME` and `REPO`, all lower case for the username).

## Step 2 – Create the Google Form (10 minutes)

1. Open <https://script.google.com> and sign in with the Google account that should own the form. Click **New project**.
2. Delete the sample code. Open `google-form/CreateForm.gs`, copy everything, paste it in, and click **Save**.
3. At the top, replace `PASTE_THE_DOWNLOAD_LINK_HERE` with the download link from Step 1. If you have a store page for the full pack, put it in `STORE_URL`.
4. In the function dropdown choose **createLeadForm** and click **Run**.
5. Google asks for permission. Click **Review permissions**, choose your account, and if you see "Google hasn't verified this app", click **Advanced → Go to (project name)**. This is normal for your own script.
6. Open the **Execution log**. You will see three links. Copy **Form link to share** (it starts with `https://docs.google.com/forms/d/e/...`). The other two are the form editor and the responses Sheet; keep them.
7. Open the form link in a private window and submit a test answer. Check:
   - the thank-you message shows the download link and the link is clickable (if it is not, open the form editor → **Settings → Presentation** → edit the confirmation message and paste the link again);
   - your test answer appears in the Sheet.
8. In the form editor, **Responses** tab → three-dot menu → **Get email notifications for new responses**.

**If you prefer to build the form by hand**, create a new Google Form with these questions: Name (short answer, required); Role (dropdown, required); Project type (dropdown); How do you make S-curves today? (multiple choice); a required Consent checkbox ("I agree to receive the free file and occasional emails about project-control templates. I can ask to be removed at any time."). In **Settings → Responses** turn on **Collect email addresses**. In **Settings → Presentation** write the confirmation message with the download link. In **Responses**, click **Link to Sheets**.

## Step 3 – Fill in the page (3 minutes)

You need Python 3 (on a PC, install from python.org; on Termux run `pkg install python`).

1. Open a terminal in this kit folder.
2. Run `python3 setup.py`.
3. Answer the questions: GitHub username, repository name, your Form link from Step 2, your store link (press Enter to skip for now) and contact email.
4. The script writes the finished page and Lite file into the `site/` folder and prints your page link and download link.

Running it again is safe; it always starts from the untouched copy in `site-template/`.

**Check before you upload:** open `site/index.html` by double-clicking it. The page should show the form. (The form only appears once the page is online or you have an internet connection; the embedded form needs the internet.)

## Step 4 – Put it on GitHub Pages (10 minutes)

**Using the website (easiest):**

1. Sign in at <https://github.com>. Click **+ → New repository**.
2. Name it exactly as in Step 1 (for example `scurve-lite`). Choose **Public**. Click **Create repository**.
3. Click **uploading an existing file**. Open the `site/` folder on your computer, select **everything inside it** (`index.html`, `.nojekyll`, the `assets` folder and the `downloads` folder) and drag it onto the GitHub page. Folder drag-and-drop works in Chrome and Edge on a computer. (If `.nojekyll` is hidden on your system, skip it; the page still works.)
4. Click **Commit changes**.
5. Go to **Settings → Pages**. Under **Build and deployment**, set **Source: Deploy from a branch**, **Branch: main**, **Folder: / (root)**, and click **Save**.
6. Wait 1 to 3 minutes and refresh. GitHub shows "Your site is live at …". Open it.

**Using Git on Termux or a PC (alternative):**

```bash
cd site
git init
git add -A
git commit -m "Landing page"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

When Git asks for a password, use a **personal access token** (GitHub → Settings → Developer settings → Personal access tokens), not your account password.

## Step 5 – Test the whole funnel (5 minutes)

Do this in a private browser window:

- [ ] The page loads and the images show.
- [ ] The form appears in the page (or the "open it in a new tab" link works).
- [ ] Submit a test response. The thank-you message appears with the download link.
- [ ] Click the link: the Excel file downloads.
- [ ] Open the file in Excel: it opens on the DASHBOARD; the START HERE sheet shows your store or page link.
- [ ] The test response is in your Google Sheet.
- [ ] Open the page on your phone.
- [ ] Share the page link in a Facebook message to yourself: the title, description and image preview appear. (If the old preview is cached, paste the link into Facebook's Sharing Debugger and scrape again.)

## Step 6 – Promote it

- Use the link in your posts from the campaign document. In groups that dislike links, put it in the first comment, or send it by message when someone asks.
- Add `?src=groupname` to the end of the link for each place you post (for example `…/scurve-lite/?src=pm-group`). The page works the same, and a free analytics counter can show which source brings visits if you add one later. GitHub Pages itself has no visitor statistics.
- Check the Sheet daily for the first week and reply to anyone who writes an interesting answer.
- Send the follow-up emails from `emails/follow-up-emails.md`.

## Things to know before you start

- **The file link is public.** Anyone who has the download link can download the Lite file without the form. That is acceptable for a free lead magnet, but the form is not a lock. If you want the form to be a real gate, send the file by email yourself after each submission instead of showing the link.
- **Google Forms does not email a custom message.** The thank-you message appears on screen only. To also email people, use a mail-merge tool with the Sheet, or send manually. Google's sending limits apply to free Gmail accounts.
- **Privacy.** You are collecting names and emails, including from people in the Philippines, so the Data Privacy Act of 2012 applies to how you handle them. Practical minimum: keep the consent checkbox, use the data only as described, keep the Sheet private, delete a person when they ask, and never add people to your list who did not submit the form. This is not legal advice; ask a professional if you grow.
- **Keep the Lite promise honest.** The page says 10 activities and 26 weeks and states that there are no dependencies or critical path. Do not add claims that the product does not support.
- **Updating the Lite file later.** Replace the file in `site/downloads/` (keep the same name) and upload it to the repository again. The download link stays the same.
- **Custom domain (optional).** In **Settings → Pages** you can connect your own domain later.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Page shows `{{FORM_URL}}` or similar text | You uploaded the template. Run `python3 setup.py` and upload the contents of the `site/` folder again. |
| Page link shows 404 | Wait a few minutes; check **Settings → Pages** is set to branch `main`, folder `/ (root)`; check `index.html` is at the top level of the repository, not inside another folder. |
| Form is blank in the page | Make sure the form is set to accept responses and you used the **published** link (`/forms/d/e/…/viewform`), not the edit link. |
| Images are missing | Check the `assets` folder was uploaded and the names match (lower case). |
| Download link gives 404 | The file name or folder is different. It must be `downloads/S-Curve_Gantt_Planner_Vol2_FREE_LITE.xlsx`. |
| Script error "Edit DOWNLOAD_URL" | Replace the placeholder at the top of the script with your real link and run again. |
| The Excel file opens read-only or formulas show nothing | Click **Enable Editing** at the top of Excel. |
| Facebook shows the wrong preview | Use Facebook's Sharing Debugger to refresh the cache. |
