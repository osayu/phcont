# phcont
control Philips BDM4065UC via rs232c.

# usage
Connect to monitor's RS232c with USB 
https://www.amazon.co.jp/gp/product/B00QUZY4JC

```
FLASK_APP=app.py python -m flask run
```

If it is other than `/dev/ttyUSB0` Please change `tv_rs232.py`.

