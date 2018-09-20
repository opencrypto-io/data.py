# opencrypto-data.py (ocd)

Basic usage:

```python
>>> import ocd
>>> ocd.get('project', 'ethereum')
```

Use with custom options:

```python
>>> import ocd
>>> client = ocd.ocd({ "data_url": "http://localhost:1234/data/dist/data.json" })
>>> client.get('project', 'ethereum')
```

## License
MIT
