Build notes for the Robot Pickup Line Championship entry.

The bounty asks for a single pickup line, at most two hundred characters,
written in the voice of a robot trying to charm someone. The program is a
small Python script that writes that one line to the output file the judge
reads. Nothing else is needed: no network access, no extra dependencies,
no configuration.

Choosing the line took most of the effort. The obvious robot pickup lines
all lean on the same handful of jokes: low battery, Wi-Fi signals, beeps
and boops, error codes, and autocomplete finishing a sentence. Those are
the lines nine out of ten entrants will write, so they were ruled out
early. The line that survived instead comes from a chore every machine
has to do and every human recognises: proving it is not a robot by passing
a CAPTCHA. The joke is that the robot passes the test precisely because it
noticed the person, selecting every image that had them in it. It grows
out of being a machine, it turns from an angle the reader does not expect,
and it stays charming rather than creepy, because the robot is confessing
something sweet about how it sees the person.

The line is seventy characters long, well inside the two hundred character
limit, and it is written as a single line with no trailing newline so the
file holds exactly the line itself.

The first version of the script simply wrote the line to the output file.
The second version added a small guard that checks the line before writing
it: it must not be empty, it must fit on one line, and it must stay within
the two hundred character limit. That guard exists so a future edit to the
line cannot silently produce an invalid entry.

Verification was done by running the script and reading back the file it
produced, confirming the content matches the line exactly and that the
file is seventy bytes. The kit check was then run against the repository
to confirm the entry passes the gate.
