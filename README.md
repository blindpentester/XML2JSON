# XML2JSON
A XML2JSON alternative that can handle much much larger files and save your PC memory and CPU.

> There is apparently a memory issue with xml2json when handling much larger files. This can hanlde any file size due to it being broken into chunks and not being read all at once, and then processed, then output all at once. Its a pretty nice way to be able to do all of your data processing for XML to JSON conversion.
> Hopefully you find this useful if you are dealing with lots and lots of data.

## Examples of Usage
```
Usage: something.py [-h] [-o OUTPUT]

Convert any XML input to JSON format

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name (default: - for stdout)
```
