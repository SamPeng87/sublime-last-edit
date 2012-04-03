# Sublime LastEdit

A Sublime Text 2 plugin to go to last edited position regardless of the file you were editing

LastEdit can cycle of one file buffer

if last edit point in the other view,LastEdit can jump for this and do your thinks as

this is my first plugin ,if have some bug,please post issues.

Next fearture:

* Sort view buffer by edit count

    wait Sublime provide tab fold api，otherwise no have any purport

* only jump last edit view buffer **[DONE]**
* if have some window edit point,will jump for it.now,LastEdit can't good work for this.I will change it

# Install & Config

Sublime Package Manager will be added soon as installation method, by now checkout from github:

     $ cd Sublime Text 2/Packages
     $ git clone git://github.com/SamPeng87/sublime-last-edit.git

# Usage

##Wherever you are you can use the default key binding for MacOs

command+. (jump for last edit point)

ctrl+[ (jump for last edited view by left)

ctrl+] (jump for last edited view by right)


##Other operating systems(Windows,linux)

control+.

ctrl+[ (jump for last edited view by left)

ctrl+] (jump for last edited view by right)

# Thanks

[GotoLastEdit][1] tell me how to create one edit queue and edit point.
[1]:https://github.com/khrizt/GotoLastEdit.git
