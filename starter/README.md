# U-GAS Project Starter

Use the [runnable U-GAS Project Starter](https://jaabster-dev.github.io/u-gas/starter/) to
start a new project or continue an existing one and copy one ready-to-use prompt into the
AI that should continue the work. The new-project mode defaults to My computer; GitHub and
My server / cloud remain visible but disabled until dedicated end-to-end validation exists.
The existing-project mode accepts a known repository URL, a local path, or an honest
"I don't know" and tells the agent to inspect the real project before changing it.

The first screen offers an optional fictional preview: it does not read or write local files.
To set up a real project, choose **Set up my project**, describe it and copy the prompt.
A copied prompt is **not** permission to write: the receiving AI must first show the
exact intended folder, files and local Git operation, explain that Git initialization
does not upload anything to GitHub, and ask for one explicit yes/no approval before
writing or initializing Git. If the user declines or an OS access prompt is broader
than expected, the agent must not bypass the denial. Plain chat without persistent
file access must hand off honestly rather than pretending setup succeeded.

Feedback is voluntary: GitHub stars indicate interest, not confirmed usage;
[Issue #1](https://github.com/jaabster-dev/u-gas/issues/1) accepts feedback (GitHub sign-in required);
a separate anonymous success-signal page may be opened manually only after actual use.
No feedback prompt is sent automatically.

The Starter preserves the public U-GAS PICA, canonical source, identity/haiku marker,
exact attribution, durable resume artifact, capability escalation, and one-copy executor
return contracts. It does not claim independent validation or make Codex mandatory.

The Starter uses privacy-friendly aggregate counting for page visits and successful Copy
attempts. It sends no project or form values and introduces no cookies or fingerprinting.
