# Deuterium

_Deuterium is in pre-alpha state and not yet fully functional.  At the moment, its repo is an installation with the project installed within it.  Eventually just the project source will be here once it is more properly refactored._

Deuterium is a pluggable space system for Evennia, designed as a replacement for the softcode and mixed hardocde/softcode systems of old.

## Getting Started
Getting started with Dueterium is easy (especially compared with getting started with hSpace, its inspiration).  All of its components are independent of Evennia's core, so you can update your game around it without worrying about any compatibility issues.

### Import Deuterium
Copy each folder in contrib/deuterium into the corresponding folder within game/gamesrc within your Evennia installation.  This makes Deuterium classes available to be loaded.

### Prepare Database
Next, run a `manage.py`, followed by `manage.py migrate`.  This should load Cochran's typeclasses and command sets in.  You may additionally have to `evennia.py -i stop` and `evennia.py -i start`.

Now you're ready!