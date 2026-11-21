/**
 * Creates the lead-capture form + a Google Sheet for the responses.
 *
 * HOW TO USE (details in SETUP_GUIDE.md, Step 2):
 *  1. Go to https://script.google.com  ->  New project.
 *  2. Delete the sample code, paste this whole file, and click Save.
 *  3. Change DOWNLOAD_URL (and optionally STORE_URL) below.
 *  4. Select the function  createLeadForm  and click Run. Approve the permissions.
 *  5. Open View -> Logs (or Execution log). Copy the "Form link to share".
 */

// <-- the Lite file link printed by setup.py (or https://USERNAME.github.io/REPO/downloads/S-Curve_Gantt_Planner_Vol2_FREE_LITE.xlsx)
const DOWNLOAD_URL = 'PASTE_THE_DOWNLOAD_LINK_HERE';
// <-- optional: your store page for the full pack. Leave '' to skip.
const STORE_URL = '';
const CONTACT_EMAIL = 'engrkit.support@gmail.com';

function createLeadForm() {
  if (DOWNLOAD_URL.indexOf('PASTE_') === 0) {
    throw new Error('Edit DOWNLOAD_URL at the top of the script first.');
  }

  const form = FormApp.create('Free S-Curve & Gantt Planner for Excel (Lite) - Download');

  form.setDescription(
    'Get the free Lite edition: weekly Gantt, S-curve, SPI/CPI and forecast finish in one Excel file ' +
    '(10 activities, 26 weeks, amounts in USD). The download link appears after you submit this form.'
  );

  form.setCollectEmail(true);          // adds a required Email field
  form.setProgressBar(false);
  form.setShowLinkToRespondAgain(false);

  let msg = 'Thank you! Download your free file here:\n' + DOWNLOAD_URL + '\n\n' +
    'Tip: open it in Microsoft Excel and click "Enable Editing". Then overwrite the yellow cells with your own project.\n\n';
  if (STORE_URL) {
    msg += 'Need more than 10 activities or 26 weeks? See the full pack: ' + STORE_URL + '\n\n';
  }
  msg += 'Questions? ' + CONTACT_EMAIL;
  form.setConfirmationMessage(msg);

  form.addTextItem().setTitle('Your name').setRequired(true);

  form.addListItem()
    .setTitle('What best describes your role?')
    .setChoiceValues([
      'Project engineer / project manager',
      'Planner / scheduler',
      'Quantity surveyor / cost engineer',
      'Contractor / subcontractor owner',
      'Student',
      'Other'
    ])
    .setRequired(true);

  form.addListItem()
    .setTitle('What kind of projects will you track?')
    .setChoiceValues([
      'CCTV / IP / ELV / security systems',
      'Electrical / mechanical / MEP',
      'Building or civil works',
      'IT / network roll-out',
      'Fit-out / renovation',
      'Other'
    ])
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle('How do you make S-curves today?')
    .setChoiceValues([
      'By hand in Excel',
      'MS Project / Primavera',
      'Other software',
      "I don't make S-curves yet"
    ])
    .setRequired(false);

  form.addCheckboxItem()
    .setTitle('Consent')
    .setChoiceValues([
      'I agree to receive the free file and occasional emails about project-control templates. I can ask to be removed at any time.'
    ])
    .setRequired(true);

  // Responses go to a new Google Sheet.
  const ss = SpreadsheetApp.create('S-Curve Lite - Leads');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  Logger.log('Form link to share : ' + form.getPublishedUrl());
  Logger.log('Edit the form here : ' + form.getEditUrl());
  Logger.log('Responses sheet    : ' + ss.getUrl());
}
