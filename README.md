# Pandas

## Datatypes

- Series
- DataFrame

### Series

      import pandas as pd
      names = ['Rodrigo', 'Fernando', 'Jéssica']
      data = pd.Series(names)
      print(data)

## Dataframes

      import pandas as pd

      d1 = pd.DataFrame({"1":"Primeira","2":"segunda"})

      print(d1)

## Importing CSV files
      data = pd.read_csv('path', encoding='utf-8', index=False)
