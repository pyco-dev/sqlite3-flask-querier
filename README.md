# Sqlite3 + Flask | Python DB Querier

I made this project to help with my react development. the purpose of it was to be able to query a database so when the user is typing on a search bar, once they type a pattern that's in a movie name in this example, the result will show up.
<br />
for e.g.
<br />
```http://127.0.0.1:5000/query?moviename=inter```
<br />
will output
<br />
```['Interstellar']```
<br />
and
<br />
```http://127.0.0.1:5000/query?moviename=jurr```
<br />
will output
<br />
```['Jurrassic Park', 'Jurrassic Park 2', 'Jurrassic Park 3']```
