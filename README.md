# lmstat_tools

# Some tools for dealing with FLEXlm lmstat output

This repository was started to address the occasional discrepencies between
the number of Abaqus licenses reported as in use by Slurm's license feature
and the number reported by FLEXlm's `lmstat` (or `lmutil lmstat`) command.

## Background

Slurm provides a way to add a license feature to the Slurm database that will
set the maximum number of licenses for a particular licensed package that can
be used.  The user is expected to request the correct number of licenses in
their job script.

This works, so long as the user both requests the licenses and requests the
correct number.  Some users do not request licenses, usually because they
do not know they need to, or they request an insufficient number.  Abaqus
does not start its license count at one and increment.

Instead, it starts at five and increments using a bizarre formula, which
could be calculated using the Linux `calc` utility

```
$ calc 'i=8 ; int(5 * i^0.422)'
	12
```

That makes for a number of circumstances in which the Slurm license counter
and the FLEXlm reported tokens in use disagree.

Further, there are circumstances in which the number of tokens reported in use
by `lmstat` may be misleading; notably, when an externally compiled solver
is invoked from within Abaqus, if it takes a long time to compute the solution,
Abaqus will return tokens, assuming they will be available when the solver
returns.  However, they are also then available for another user.

When Abaqus tries to check out tokens but not enough are available, it will
pause and wait for tokens to become available.  This is undesirable in a job
because the idling Abaqus is doing no work but is consuming time that will be
billed to the user's account.

The files in this repository are intended to provide a way to compare what
Slurm and `lmstat` report so that appropriate action can be taken if needed.


