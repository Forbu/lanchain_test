### To launch the site 

```bash
python run.py
```

### To migrate the db (to include confirmed column that we will use later) 

```bash
flask db migrate -m "Add confirmed column to User model"
```

