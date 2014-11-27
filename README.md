## Getting Started
Getting started with Cochran is easy (especially compared with getting started with hSpace, its inspiration).  All of its components are independent of Evennia's core, so you can update your game around it without worrying about any compatability issues.

### Import Cochran
Copy each folder in dist/ into game/gamesrc within your Evennia installation.  Obviously, this makes Cochran's classes available to be loaded.

### Prepare Database
Next, run a `manage.py`, followed by `manage.py migrate`.  This should load Cochran's typeclasses and command sets in.

## Ship Maintenance

### Ship Construction
Create a basic Freighter like: `@create/drop Freighter:cochran.ships.generic_ships.Freighter`

Create a new BaseShip like: `@create/drop BaseShip:cochran.ships.ship.Ship`

If these don't both work, there's something going on with the inheritance system.