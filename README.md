# About

This script will get an `original CSV`, which has `Pack Titles` in the first column and a `Rank` in the second column. This is the rank for _"TotalMixed Meta Rank"_ from the Historic 1.0 sheet. Then the programm will get a second CSV, the `new packs CSV`, which only has the first column.

Now the programm will get the **rank** from the first CSV and, if it finds the same pack on the other CSV, will apply it to the pack in a new column. It will export a new CSV.

Why? It is supposed to keep the sorting of the new CSV.

# Additionally

You can also convert a given `JSON` file to a `CSV`, while the JSON should have such a format:

```json
[{
  "packTitle": "Afro Trap & Vocals Vol 1",
  "publishedMulti": 0
},
// and more such entries...
]
```

Do so by using the `-c` parameter together with a filename: `python3 run.py -c [FILENAME]`. It will try to output a CSV with the same name yet another ending.