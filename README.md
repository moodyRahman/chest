# Chest
## The easy way to manage your inventory

#### What is Chest?
Chest is a open source, self-hostable web application that lets users register, create their characters from their preferred table-top RPG's, and maintain their inventory.  
The app is designed to be lightweight and to maximize support for homebrew characters and items.  
Many other TRPG inventory managers are bulky, heavy, and do questionable things with their userdata, and gear only towards the offical list of items. Chest is designed to be homebrew first, and all of the userdata is self-hosted. 

#### How to use Chest
Go to https://chest-nightly.herokuapp.com/  
Register a new account.  
The source code is open! All passwords are hashed and salted and no other user information is stored other than what is exactly put into Chest.

#### How to self-host Chest
1) `git clone git@github.com:moodyRahman/chest.git`
2) `cd chest`
3) `pip3 install -r requirements.txt` (optionally in a virtual environment)
4) `gunicorn -w 4 wsgi:app`
5) configure your webserver to reverse proxy with the app, on port 800
6) edit your environmental variables such that `$chest_debug` is `"true"` if you wish to connect to a local instance of mongodb, and `$atlasurl` to the URI of a remote mongodb
  6a) These variables are referred to in `app/utils/dbctrl.py` and `app/__init__.py`. If you wish to use different variables, feel free to change it around. 
7) Distribute the URL to your users