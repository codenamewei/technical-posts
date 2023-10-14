### Part 0
```
docker build -t nativeapp .
docker run -p 8000:8000 nativeapp
docker run -it nativeapp /bin/bash
```

### Part 1
```
docker build -t multistageapp01 .
docker run -p 8000:8000 multistageapp01
docker run -it multistageapp01 /bin/bash
```

### Part 2
```
docker build -t multistageapp02 .
docker run -p 8000:8000 multistageapp02
docker run -it multistageapp02 /bin/bash
```