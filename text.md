Create a new repository
git clone https://gitlab.com/snikpet2009/db_personev01b.git
cd db_personev01b
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Push an existing folder
cd existing_folder
git init
git remote add origin https://gitlab.com/snikpet2009/db_personev01b.git
git add .
git commit -m "Initial commit"
git push -u origin master

Push an existing Git repository
cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.com/snikpet2009/db_personev01b.git
git push -u origin --all
git push -u origin --tags


…or create a new repository on the command line
echo "# db_personeV01b" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:snikpet2009/db_personeV01b.git
git push -u origin master
…or push an existing repository from the command line
git remote add origin git@github.com:snikpet2009/db_personeV01b.git
git push -u origin master
