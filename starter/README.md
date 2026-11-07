# U-GAS Project Starter

Use the [runnable U-GAS Project Starter](https://jaabster-dev.github.io/u-gas/starter/) to
start a new project or continue an existing one and copy one ready-to-use prompt into the
AI that should continue the work. The new-project mode defaults to My computer; GitHub and
My server / cloud remain visible but disabled until dedicated end-to-end validation exists.
The existing-project mode accepts a known repository URL, a local path, or an honest
"I don't know" and tells the agent to inspect the real project before changing it.

The first screen offers an interactive fictional project-resume example. You can run
it in the browser and copy a read-only sample for an AI chat: no local file access,
Git, installation or permissions are required, and the demonstration does not create
persistent project memory. Copying the sample does **not** send it automatically.
To set up a real durable project, choose **Set up my project**, describe it and review
the proposed file list and target folder **before** copying the prompt.
A copied prompt is **not** permission even to read local project files. The receiving
AI must first explain the exact folder and proposed read/write operations, local Git
and OS permission scope. For a new project it asks once before inspecting or creating
local files. For an existing project it asks before any local read, then requests a
separate write approval after inspection. Git initialization is local private version
history, not a GitHub upload. The suggested folder is `~/U-GAS Projects/<project-name>`,
outside macOS's protected Documents directory; the AI application may nevertheless
ask for other permissions, so users should reject unexpected access or Full Disk Access. If the user declines or an OS access prompt is broader
than expected, the agent must not bypass the denial. Plain chat without persistent
file access must hand off honestly rather than pretending setup succeeded.

Feedback is voluntary: GitHub stars indicate interest, not confirmed usage;
[Issue #1](https://github.com/jaabster-dev/u-gas/issues/1) accepts feedback (GitHub sign-in required);
a separate anonymous success-signal page may be opened manually only after actual use.
No feedback prompt is sent automatically.

The Starter preserves the public U-GAS PICA, canonical source, identity/haiku marker,
exact attribution, durable resume artifact, capability escalation, and one-copy executor
return contracts. It does not claim independent validation or make Codex mandatory.

The page does not transmit the entered project description; it stays in the browser
until copied and deliberately pasted into an AI service, which then receives that text.
The fictional demo copy is not counted as a completed project setup.

The Starter uses privacy-friendly aggregate counting for page visits and successful Copy
attempts. It sends no project or form values and introduces no cookies or fingerprinting.
