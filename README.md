# gradle_scan
Scan build.gradle files for executables

## Usage
Pass in a `.gradle` file to scan. By default, other files will be rejected.

1. `git clone git@github.com:schordas/gradle_scan.git`
2. `cd gradle_scan`
3. `chmod +x gradle_scan.py`
4. `./gradle_scan.py path/to/build.gradle path/to/second/build.gradle`

```
build.gradle is a valid file

Scanning for suspicious content...

## Example output
WARNING: suspicious line found in build.gradle

line in question:

line 3      "evil_script.go"

##############
```
