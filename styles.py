CSS = """
:root {
  --twin-gold: #b06a0a;
  --twin-blue: #0e8f86;
  --twin-purple: #0e8f86;
  --twin-bg: #f6f5f1;
  --twin-surface: #ffffff;
  --twin-surface-2: #f0efe9;
  --twin-border: #dedad0;
  --twin-border-strong: #c5c0b3;
  --twin-text: #1c1e24;
  --twin-muted: #666b76;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

/* ---------- Stable layout ---------- */
.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 26px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  border-left: 3px solid var(--twin-gold);
  padding-left: 12px !important;
  margin: 4px 0 8px !important;
  text-align: left !important;
}

/* ---------- Sharp corners on structural pieces ---------- */
.chatbot, .chatbot *, .block, .form,
button, input, textarea,
.examples button {
  border-radius: 0 !important;
}

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  min-height: 460px !important;
  box-shadow: none !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 6px 10px !important;
}

/* ---------- Bubble backgrounds (broad to cover Gradio variants) ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-blue) !important;
  color: #ffffff !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
}

/* ---------- Accent stripe ----------
   Apply to every common bubble class for assistant rows (we don't know which
   one the running Gradio uses), then suppress on any *nested* instance so the
   stripe lands on the outermost matching element only — exactly one stripe. */
.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 2px solid var(--twin-purple) !important;
}

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* ---------- Uniform font size in bubbles ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.55 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
}

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 12px 14px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 0 1px var(--twin-gold) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'IBM Plex Mono', 'SF Mono', Menlo, monospace !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  padding: 0 16px !important;
  min-height: 48px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: background 0.12s ease, color 0.12s ease, border-color 0.12s ease;
}
button:hover { border-color: var(--twin-gold) !important; color: var(--twin-gold) !important; }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-gold) !important;
  border: 1px solid var(--twin-gold) !important;
  color: #fff8ec !important;
  min-height: 48px !important;
  align-self: stretch !important;
  padding: 0 14px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: var(--twin-blue) !important;
  border-color: var(--twin-blue) !important;
  color: #ffffff !important;
}

/* ---------- Submit-button icon ---------- */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #fff8ec !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 14px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  padding: 10px 14px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  background: var(--twin-surface) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--twin-gold) !important; }

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: var(--twin-bg); }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); }
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-gold); color: #fff8ec; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 14px 36px !important; }
  .gradio-container h1 { font-size: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  // Force light mode always, regardless of system preference
  const forceLight = () => {
    document.body.classList.remove('dark');
    document.documentElement.classList.remove('dark');
  };
  forceLight();
  new MutationObserver(forceLight).observe(document.body, { attributes: true, attributeFilter: ['class'] });

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""

EXAMPLES = [
    "What projects have you built?",
    "What are your main skills?",
    "How can I get in touch with you?",
]