# FakeDiskDetector
Detects if the space advertised in a partition table really is available (aka. fake flash drives)

# Usage
To use it you first have to get it:
```
PENDING DOC
```

## 1st Arg
The mountpoint

## 2nd Arg
The size that should be checked for in MB (MegaBytes).

```
python FakeDiskDetector.py /Volumes/volume1 526870
# This tests a volume mountend to /Volumes/volume1 for a 526.870 GB size
```
