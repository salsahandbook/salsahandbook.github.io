# salsahandbook.github.io


### Salsa Handbook Website


To edit this site:
```$ cd ~/code/salsahandbook.github.io
$ conda activate blog
$ git pull
```

To inspect this site locally do the following, then browse to http://localhost:8000.   Exit via `ctrl-c`. 

`$ make html && make serve`

To publish modifications:

`$  git add -A && git commit -a -m '<INSERT NEW COMMIT STATEMENT HERE>' && git push --all`

`$ make github`

`$ git push origin master`


_Press Deny on any popups and enter github cred at the command line._



Check link:  http://salsahandbook.github.io


When finished, exit the virtual environment.
`$ conda deactivate`

