Dreamhost DNS updater
=====================

I am dreamhost customer and I want to have a DNS record that is pointing somewhere different
then at their server farm. But it is behind a dynamic ip. I need to update the dns A record 
everytime the ip change. Why not using python to do so.

Configuration
:::::::::::::

Create the hidden folder where the configuration file is created.
    mkdir -p ~/.dhdm/

Edit the file and add your key and domain name to be updated 
    [api]
    key=JG5HF854JF74HD984RH4D9J4D7E4
    
    [domains]
    name=api.example.com
 
If you have multiple domains behind the same ip address you can do a comma separated list.
    [api]
    key=JG5HF854JF74HD984RH4D9J4D7E4

    [domains]
    name=api.example.com,wiki.example.com,git.example.com